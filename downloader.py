import requests
import os
from concurrent.futures import ThreadPoolExecutor


DOWNLOAD_DIR = 'D:\KnowledgeBase\DownloadedUnarchived\subfolder'


def download_file(url, filename):
    
    try:
        if url.endswith('.rar') or url.endswith('.zip'):  # Add the file extensions you want to allow
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful
            file_path = os.path.join(DOWNLOAD_DIR, filename)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded {filename}")
        else:
            print(f"Skipping download of {url} as it is not a supported file type")

    except requests.exceptions.RequestException as err:
        print(f"Error occurred while downloading {url}: {err}")

def download_files_in_batches(links, batch_size=5):
    with ThreadPoolExecutor(max_workers=batch_size) as executor:
        for i in range(0, len(links), batch_size):
            batch = links[i:i+batch_size]
            for j, url in enumerate(batch):
                filename = links[i+j].split('/')[-1]  # Extract filename from the URL
                executor.submit(download_file, url, filename)

    
# Usage
if __name__ == "__main__":
    with open('links.txt', 'r') as file:
        links = file.read().splitlines()
    download_files_in_batches(links)
    print("all download completed")