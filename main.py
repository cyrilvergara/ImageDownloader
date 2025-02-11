import argparse
import os
import time
import threading
from download_file import download_file  # Import function
from image_urls import image_urls  # Import URL list

def download_images_serially(data_folder):
    """Downloads images one by one (serial execution)."""
    start_time = time.perf_counter()

    for idx, url in enumerate(image_urls):
        filename = os.path.join(data_folder, f"image_serial_{idx+1}.jpg")
        download_file(url, filename)

    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nWith my present internet connection, I got a time of {elapsed_time:.0f} milliseconds (serial).")

def download_images_with_threads(data_folder):
    """Downloads images using multiple threads."""
    start_time = time.perf_counter()

    threads = []

    for idx, url in enumerate(image_urls):
        filename = os.path.join(data_folder, f"image_thread_{idx+1}.jpg")
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nWith my present internet connection, I got a time of {elapsed_time:.0f} milliseconds (threaded).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images either serially or using threads.")
    parser.add_argument("mode", choices=["serial", "threaded"], help="Choose download mode: 'serial' or 'threaded'")
    parser.add_argument("-d", "--data-folder", default="downloads", help="Specify a folder to save images (default: downloads)")

    args = parser.parse_args()

    os.makedirs(args.data_folder, exist_ok=True)  # Ensure folder exists

    if args.mode == "serial":
        download_images_serially(args.data_folder)
    elif args.mode == "threaded":
        download_images_with_threads(args.data_folder)
