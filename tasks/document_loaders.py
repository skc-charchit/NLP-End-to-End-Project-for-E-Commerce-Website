import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

import sys
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

# Create a loader with your target URL
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")

# Load documents (returns a list of Document objects)
docs = loader.load()

# Check the content
for doc in docs:
    print(doc.page_content[:100])