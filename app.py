import streamlit as st
import json
import os
import modal

# Function to process podcast information from a URL
def process_podcast_info(url, path):
    f = modal.Function.lookup("corise-podcast-project", "process_podcast")
    output = f.call(url, path)
    return output

# Set the page title and icon
st.set_page_config(page_title="Podcast Summary App", page_icon="🎙️")

# Top bar section
st.title("🚀 Podcast Summary App")
st.markdown("---")

# Logo
# st.image("path_to_your_logo.png", use_container_width=True)

# Contact information
st.subheader("📧 Contact Us")
st.write("📧 Email: contact@example.com")
st.write("📞 Phone: +1234567890")
st.markdown("---")

# GitHub link
github_link = "https://github.com/yourusername/your-repo"
github_icon = "🔗 [GitHub Repository](" + github_link + ")"
st.subheader("GitHub Repository")
st.write(github_icon)
st.markdown("---")

# Load podcast details
file_names = [filename for filename in os.listdir("json_files") if filename.endswith(".json")]
podcast_data = {}

for file_name in file_names:
    with open(os.path.join("json_files", file_name)) as file:
        podcast = json.load(file)
        podcast_data[podcast['podcast_details']['podcast_title']] = podcast

# Sidebar - Input fields
st.sidebar.header("Podcast RSS Feeds")
st.sidebar.subheader("Available Podcasts Feeds")

# Select podcast title to view podcast details (in the sidebar)
selected_podcast_title = st.sidebar.selectbox("Select Podcast Title", list(podcast_data.keys()))

# Display selected podcast details
if selected_podcast_title:
    selected_podcast = podcast_data[selected_podcast_title]
    
    # Display podcast title and image in the same row using Markdown
    image_url = selected_podcast['podcast_details']['episode_image']
    st.markdown(f"# {selected_podcast['podcast_details']['podcast_title']}")

    col1, col2 = st.columns([7, 3])

    with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.write(selected_podcast['podcast_summary'])

    with col2:
        # Display the podcast cover image
        st.image(selected_podcast['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)
        
    st.subheader("Podcast Guest Information:")
    st.write(selected_podcast['podcast_guest'])
        
    st.subheader("Podcast Highlights:")
    st.write(selected_podcast['podcast_highlights'])
        
    st.subheader("Podcast Chapters:")
    st.write(selected_podcast['podcast_chapters'])

# User Input box in the sidebar
st.sidebar.subheader("Add and Process New Podcast Feed")
url = st.sidebar.text_input("Link to RSS Feed")

process_button = st.sidebar.button("Process Podcast Feed")
st.sidebar.markdown("**Note**: Podcast processing can take up to 5 mins, please be patient.")

if process_button:
    output = process_podcast_info(url, '/content/podcast/')
    podcast_info = output['podcast_details']

    image_url = selected_podcast['podcast_details']['episode_image']
    st.markdown(f"# {selected_podcast['podcast_details']['podcast_title']}")

    col1, col2 = st.columns([7, 3])

    with col1:
        # Display the podcast episode summary
        st.subheader("Podcast Episode Summary")
        st.write(selected_podcast['podcast_summary'])

    with col2:
        # Display the podcast cover image
        st.image(selected_podcast['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)
        
    st.subheader("Podcast Guest Information:")
    st.write(selected_podcast['podcast_guest'])
        
    st.subheader("Podcast Highlights:")
    st.write(selected_podcast['podcast_highlights'])
        
    st.subheader("Podcast Chapters:")
    st.write(selected_podcast['podcast_chapters'])