import requests

# Replace 'your_api_token' with your actual API token
with open('token.txt', 'r') as file:
    api_token = file.read().strip()

base_url = 'https://api.real-debrid.com/rest/1.0/'

# Function to unrestrict a link and return the download link
def unrestrict_link(api_token, link):
    response = requests.post(base_url + 'unrestrict/link', headers={'Authorization': 'Bearer ' + api_token}, data={'link': link})
    print("link unrestriceted")
    return response.json()['download']

# Read links from links.txt and unrestrict each link
if __name__ == "__main__":
    unrestricted_links = [unrestrict_link(api_token, link.strip()) for link in open('links.txt', 'r')]

    # Print the list of unrestricted download links
    print(unrestricted_links)

