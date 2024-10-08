import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets['groq_api_key'])

context = '''You are an AI assistant tasked with generating high-quality blog posts for a blog generation system. The goal is to create AI-driven content with customizable writing styles, industry-specific terminology, content structure, and sentiment analysis. You will also provide SEO optimization, tone consistency, fact-checking, and support multilingual output.'''

def get_blog_completion(user_input):
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": f'{context}\n\n{user_input} That generated content should follow markdown languages'}],
        model="llama3-8b-8192",
    )
    return completion.choices[0].message.content

st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("AI-Powered Blog Generation System")

st.markdown("""
This app generates high-quality blog posts with customizable writing styles, SEO optimization, industry-specific terminology, and sentiment settings.
Simply provide the blog's topic, select preferences for writing style, blog structure, and additional options, and the AI will generate a blog for you.
""")

# Input for the blog topic
blog_topic = st.text_input("Enter the blog topic:")

# Writing style options
style_options = ['Formal', 'Casual', 'Technical', 'Research']
writing_style = st.selectbox("Choose a writing style:", style_options)

# Blog structure options
structure_options = ['How-to', 'Listicle', 'News']
blog_structure = st.selectbox("Select the structure of the blog:", structure_options)

# Sentiment options
sentiment_options = ['Positive', 'Neutral', 'Critical']
blog_sentiment = st.selectbox("Choose the sentiment for the blog:", sentiment_options)

# Option for industry-specific keywords
include_keywords = st.checkbox("Include industry-specific keywords?")

# Additional inputs for customization
use_custom_dictionary = st.checkbox("Use custom dictionary for industry-specific terms?")
generate_seo_meta = st.checkbox("Generate SEO meta descriptions?")
enable_fact_checking = st.checkbox("Enable automatic fact-checking?")

# Multilingual support
languages = ['English', 'Hindi', 'Spanish', 'French', 'German']
selected_language = st.selectbox("Choose language for blog generation:", languages)

# Submit button
if st.button("Generate Blog"):
    if blog_topic:
        with st.spinner("Generating your blog..."):
            # Construct the user input prompt based on selections
            user_input = f"Generate a {blog_structure} blog on '{blog_topic}' with a {writing_style} style and {blog_sentiment} sentiment."

            if include_keywords:
                user_input += " Please include relevant industry-specific keywords."
            if use_custom_dictionary:
                user_input += " Use a custom dictionary for industry-specific terminology."
            if generate_seo_meta:
                user_input += " Generate SEO meta descriptions and analyze keyword density."
            if enable_fact_checking:
                user_input += " Also fact-check the blog content and provide citations."
            
            # Add multilingual support
            user_input += f" The generated blog everthing should be in {selected_language} strictly."

            # Get blog content from the Groq API
            response = get_blog_completion(user_input)
            
            # Display the generated blog content
            st.markdown("### Generated Blog Content:")
            st.write(response)
    else:
        st.error("Please enter a blog topic before submitting.")

# Sidebar information
st.sidebar.title("Blog Generation Features")
st.sidebar.markdown("""
- Customizable Writing Styles
- Industry-Specific Keywords and Terminology
- SEO Meta Descriptions
- Automatic Fact-Checking
- Multilingual Support
""")

# Optional Groq model selection
st.sidebar.title("Choose Blog from Groq Choices")
st.sidebar.markdown("""
If you're unsure, you can select one of the blogs generated by Groq for similar topics.
""")
blog_options = ['Blog 1', 'Blog 2', 'Blog 3']  # Example placeholders for blogs from Groq choices
selected_blog = st.sidebar.selectbox("Select a pre-generated blog:", blog_options)
if st.sidebar.button("Load Selected Blog"):
    # Here, you would retrieve the pre-generated blog content
    st.sidebar.write(f"Loading {selected_blog}...")
