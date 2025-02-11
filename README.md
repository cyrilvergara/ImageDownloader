# Image Downloader

This Python project allows users to download images from a predefined list of URLs. It supports both **serial** and **threaded** downloading modes, allowing you to compare their performance.

## Features

- Downloads images **serially** (one by one) or **using threads** (concurrently).
- Allows specifying a **custom download folder**.
- Measures and logs the **time taken** for each download method.
- Uses **argparse** for command-line argument handling.

## Project Structure

```
📁 image-downloader
├── 📄 main.py              # Main script to execute downloads
├── 📄 download_file.py     # Function to download an image from a URL
├── 📄 download_threads.py  # Implements threaded image downloading
├── 📄 image_urls.py        # Stores a list of image URLs
├── 📄 README.md            # Project documentation
```

## Installation & Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/image-downloader.git
   cd image-downloader
   ```
2. Ensure you have Python installed (>= 3.6).
3. Install required dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line to download images:

### Serial Download (One by One)

```sh
python main.py serial
```

### Threaded Download (Concurrent)

```sh
python main.py threaded
```

### Specify a Custom Download Folder

```sh
python main.py serial -d my_images_folder
```

or

```sh
python main.py threaded -d custom_folder
```

## Example Output

```
With my present internet connection, I got a time of 6820 milliseconds (serial).
With my present internet connection, I got a time of 332 milliseconds (threaded).
```

## Contributing

If you’d like to contribute:

- Fork this repository
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -m "Added new feature"`)
- Push to your branch (`git push origin feature-branch`)
- Open a Pull Request 🎉

## License

This project is licensed under the MIT License

## Author

Developed by **Cy Vergara**.

---

Happy coding! 🚀
