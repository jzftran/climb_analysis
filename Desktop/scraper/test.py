import requests
from bs4 import BeautifulSoup as bs
import lxml

# Page header
head= { 'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# Start Page
url = 'https://www.moonboard.com/'
# Login URL
login_url = 'https://www.moonboard.com/'
# URL behind the login page
url2= 'https://www.moonboard.com/Dashboard/Index'

# Open up a session
s = requests.session()

# Open the login page
r = s.get(url)

# Get the csrf-token from meta tag
soup = bs(r.text,'lxml')
soup
csrf_token = soup.select_one('meta[name="csrf-token"]')['content']

# Get the page cookie
cookie = r.cookies

# Set CSRF-Token
head['X-CSRF-Token'] = csrf_token
head['X-Requested-With'] = 'XMLHttpRequest'

# Build the login payload
payload = {
'username': 'U-zef', #<-- your username
'password': 'Isotoma2viridis3', #<-- your password
}

# Try to login to the page
r = s.post(login_url, data=payload, headers=head)
r
# Try to get a page behind the login page
r = s.get(url2)

# Check if login was successful, if so there have to be an element with the id menu_row2
soup = bs(r.text, 'lxml')
element = soup.select('#menu_row2')
print(element)
