from pytube import YouTube
import os
import requests


# Set up proxy if needed (optional)
# os.environ['http_proxy'] = 'http://your_proxy_address:port'
# os.environ['https_proxy'] = 'http://your_proxy_address:port'

def check_url_access(url):
    """Check if the URL is accessible using the requests library."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL: {e}")
        return False


try:
    link = input("Enter the video link: ")

    # Verify if the URL is accessible
    if not check_url_access(link):
        raise ValueError("The URL is not accessible. Please check your connection or the URL.")

    print("Downloading...")
    yt = YouTube(link)

    # Attempt to download the first stream
    yt.streams.first().download()

    print("Download Successful")
except Exception as e:
    print(f"An error occurred: {e}")