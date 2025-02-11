import os
import requests

def download_file(url, pathname):
    """Downloads a file from the given URL and saves it to the specified pathname."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Ensure the request was successful

        os.makedirs(os.path.dirname(pathname), exist_ok=True)  # Ensure folder exists

        with open(pathname, 'wb') as file:
            for chunk in response.iter_content(chunk_size=50):  # Chunk size
                print('+', end='', flush=True)  # Show progress
                file.write(chunk)

        print(f"\nDownload completed: {pathname}")  # Print final message
    except requests.exceptions.RequestException as e:
        print(f"\nDownload failed: {e}")  # Handle errors gracefully

# Single image
url = "https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7"
download_file(url, "client_download/image.jpg")
