# Project Name
Real Debrid downloader

## Description
This project demonstrates how to use the `requests` library to interact with the Real-Debrid API for unrestricting and downloading links.

## File Structure
- `requestTest.py`: Contains the main code for unrestricting and downloading links using the Real-Debrid API.
- `token.txt`: Should contain the API token for accessing the Real-Debrid API.

## Usage
1. Ensure that `token.txt` contains the API token 

2. Find any desire download file from Sanet.st (Need to be rapidgator hoster)

3. Run `Run.py` to unrestrict and download the links specified in `links.txt`.

## Code Explanation
The `requestTest.py` file contains the following key components:
- Reading the API token from `token.txt`.
- Defining a function to unrestrict a link using the API token.
- Reading links from `links.txt` and unrestricting each link.
- Printing the list of unrestricted download links.

## Dependencies
- Python 3.x
- `requests` library

## Additional Notes
- Ensure that the `requests` library is installed. If not, install it using `pip install requests`.

Feel free to customize this template to fit the specific details of your project.