import requests
from bs4 import BeautifulSoup

# specify the Instagram account username
username = "example_account"  # replace with the desired Instagram account username

# create the URL for the Instagram account's profile page
url = f"https://www.instagram.com/{username}/"

# send a GET request to the Instagram profile page
response = requests.get(url)

# parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find the element that contains the follower count
follower_count_element = soup.find("span", class_="g47SY")

# extract the follower count from the element
follower_count = follower_count_element.text

# print the follower count
print(f"The Instagram account '{username}' has {follower_count} followers.")