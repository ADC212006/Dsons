import requests
import os

# Dictionary of URLs with their desired new filenames
files_to_download = {
    "http://example.com/recording/assets/mm/Intro_-11.mp3": "Intro.mp3",
    # replace with url  urls with the correct domain in arry and the correct file name
    
}

# Directory to save the downloaded files
save_directory = "downloaded_audio"
os.makedirs(save_directory, exist_ok=True)

# Function to download and save a single file with a new filename
def download_file(url, new_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        file_path = os.path.join(save_directory, new_filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded and saved as {new_filename}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {str(e)}")

# Loop through the dictionary and download each file
for url, new_name in files_to_download.items():
    download_file(url, new_name)

print("All files downloaded and renamed.")
