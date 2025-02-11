import os
import time
import requests
from download_file import download_file  # Importing the function from download-file.py
from image_urls import image_urls  # Import list of image URLs

def download_images_sequentially():
    """Downloads a set of images sequentially and times the process."""
    start_time = time.perf_counter()  # Start the timer

    for idx, url in enumerate(image_urls):
        filename = f"client_download/image_{idx+1}.jpg"
        download_file(url, filename)  # Invoke the function from download_file.py

    end_time = time.perf_counter()  # End the timer
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nWith my present internet connection, I got a time of: {elapsed_time:.0f} milliseconds")

# Run the function
download_images_sequentially()
