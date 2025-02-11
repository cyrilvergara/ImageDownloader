import time
import threading
from download_file import download_file  # Import function from Part A
from image_urls import image_urls  # Import list of image URLs

def download_images_with_threads():
    """Downloads images using multiple threads and measures execution time."""
    start_time = time.perf_counter()  # Start the timer

    threads = []  # List to keep track of threads

    for idx, url in enumerate(image_urls):
        filename = f"client_download/image_thread_{idx+1}.jpg"
        thread = threading.Thread(target=download_file, args=(url, filename))  # Create a thread
        threads.append(thread)
        thread.start()  # Start the thread

    for thread in threads:
        thread.join()  # Wait for all threads to finish

    end_time = time.perf_counter()  # End the timer
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nWith my present internet connection, I got a time of {elapsed_time:.0f} milliseconds.")

# Run the function
if __name__ == "__main__":
    download_images_with_threads()
