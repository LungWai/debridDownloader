import os
import concurrent.futures
import patoolib
import downloader as d
import requestTest as rt


MAX_THREADS = 15
DOWNLOAD_DIR = 'D:\KnowledgeBase\DownloadedUnarchived\subfolder'
DST_DIR = 'D:\KnowledgeBase\ArchivedUnclassified'
# files_to_keep = ['downloader.py', 'links.txt','run.py', "requestTest.py"]


def extract_rar(file_path, output_dir, thread_num):
    try:
        file_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract the file name without extension
        output_path = os.path.join(output_dir, file_name)  # Create the output directory path
        os.makedirs(output_path, exist_ok=True)  # Create the output directory if it doesn't exist
        patoolib.extract_archive(file_path, outdir=output_path)  # Extract the archive into the output directory
        print(f'Successfully extracted {file_path} in thread {thread_num}')
        return file_path
    except Exception as e:
        print(f'Failed to extract {file_path}. Reason: {e}')
        return None
    


def parallel_unrar(directory, output_dir):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for file_name in os.listdir(directory):
            if file_name.endswith('.part1.rar') or file_name.endswith('.001.rar') or (file_name.endswith('.rar') and '.part' not in file_name):
                file_path = os.path.join(directory, file_name)
                future = executor.submit(extract_rar, file_path, output_dir, len(futures)+1)
                futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            print(f'Unzipped file: {future.result()}')

def delFile(DOWNLOAD_DIR):
    for filename in os.listdir(DOWNLOAD_DIR):
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        if os.path.isfile(file_path) and filename:
            os.remove(file_path)


def unrestrict_and_download(links):
    unrestricted_links = []
    for link in links:
        unrestricted_link = rt.unrestrict_link(rt.api_token, link)  # Use the unrestrict_link function from requestTest.py
        unrestricted_links.append(unrestricted_link)
    return unrestricted_links

# Usage
if __name__ == "__main__":
    with open('links.txt', 'r') as file:
        links = file.read().splitlines()
    unrestricted_links = unrestrict_and_download(links)
    d.download_files_in_batches(unrestricted_links)
    os.system('cls')
    print("all download completed")
    parallel_unrar(DOWNLOAD_DIR, DST_DIR)
    os.system('cls')
    print("All unarchiving completed")
    delFile(DOWNLOAD_DIR)
