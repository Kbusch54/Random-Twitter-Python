import requests
from bs4 import BeautifulSoup

# Make a GET request to the webpage
response = requests.get('https://twitter.com/tarunchitra/following')

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find the elements containing the account names and the users they follow
account_names = soup.find_all('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
# followed_users = soup.find_all('div', class_='followed-user')

# Extract the data from the elements
account_names_list = [name.text for name in account_names]
# followed_users_list = [user.text for user in followed_users]

# Store the data or perform further processing
# For example, you can save the data to a file or store it in a database
print(account_names_list)