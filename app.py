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
st.set_page_config(page_title="Podcast Summary App", page_icon="🎙️", layout="wide")

# Top bar section
st.title("🎙️ Podcast Summary App")
st.markdown("---")

# Logo
# st.image("path_to_your_logo.png", use_container_width=True)

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
# selected_podcast_title = st.sidebar.selectbox("Select Podcast Title", list(podcast_data.keys()))
selected_podcast_title = st.sidebar.selectbox("Select Podcast Title", ["Home"] + list(podcast_data.keys()))

# User Input box in the sidebar
st.sidebar.subheader("Add and Process New Podcast Feed")
url = st.sidebar.text_input("Link to RSS Feed")

process_button = st.sidebar.button("Process Podcast Feed")
st.sidebar.markdown("**Note**: Podcast should be less then 45mins. Processing can take up to 5 mins, please be patient.")

# Home page (default content)
if selected_podcast_title == "Home": #and not process_button:
    st.title("Welcome to the Podcast Summary App")
    st.write("The Podcast Summary App allows you to explore podcast details and summaries in an interactive and user-friendly way. Whether you're a podcast enthusiast, a content creator, or just curious about the latest episodes, this app has you covered.")
    st.write("### Features:")
    st.write("🎙️ **Explore Podcast Details:** View comprehensive information about podcast episodes, including summaries, guest details, highlights, and chapters.")
    st.write("📧 **Contact Us:** Have questions or feedback? Feel free to reach out to us. We'd love to hear from you.")
    st.write("🔗 **GitHub Repository:** Check out our GitHub repository for the latest updates, contribute to the codebase, or explore the inner workings of the app.")
    st.write("### How to Use:")
    st.write("1. Use the sidebar on the left to select a processed podcast from the available options. Click on 'select podcast title' and choose from the list.")
    st.write("2. The main content area will display the selected podcast's details, including episode summary, guest information, highlights, and chapters.")
    st.write("3. If you want to add and process a new podcast feed, enter the RSS feed link in the sidebar and click 'Process Podcast Feed.'")
    st.write("Find the rss to your favorite podcast at [ListenNotes](https://listennotes.com). Feel free to explore and enjoy the podcasting experience!")
    st.markdown("---")
    st.write("**Note:** Podcast processing can take some time, so please be patient after clicking the 'Process Podcast Feed' button. If you have any questions or need assistance, don't hesitate to reach out using the contact information provided.")
    st.subheader("📧 Contact Details ")
    col1, col2, col3, col4 = st.columns([3, 3, 3, 3])
    
    with col1:
        st.write("[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gbotemiB)")
    with col2:
        st.write("[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/_oluwagbotty)")
    with col3:
        st.write("[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/emmanuel-bolarinwa/)")
    with col4:
        st.write("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gbotemibolarinwa@gmail.com)")

    st.markdown("---")
else:
    if process_button:
        try:
            output = process_podcast_info(url, '/content/podcast/')
            selected_podcast = output['podcast_details']

            image_url = selected_podcast['episode_image']
            st.markdown(f"# {selected_podcast['podcast_title']}")

            col1, col2 = st.columns([7, 3])

            with col1:
                # Display the podcast episode summary
                st.subheader("Podcast Episode Summary")
                st.write(output['podcast_summary'])

            with col2:
                # Display the podcast cover image
                st.image(selected_podcast['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)
                
            st.subheader("Podcast Guest Information:")
            st.write(output['podcast_guest'])
                
            st.subheader("Podcast Highlights:")
            st.write(output['podcast_highlights'])
                
            st.subheader("Podcast Chapters:")
            st.write(output['podcast_chapters'])
        except:
            st.write("System is running into error. Please wait a few mins then try again.")

    else:
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