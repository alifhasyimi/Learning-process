import requests
from bs4 import BeautifulSoup as bs
import os 

# food images
url = 'https://www.gettyimages.co.uk/photos/malaysian-food?numberofpeople=none&phrase=malaysian%20food&sort=best'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with img tag
image_tags = soup.findAll('img')

# create dictionary for model images
if not os.path.exists('Food'):
    os.makedirs('Food')

# move to new directory
os.chdir('Food')

# writing images
x = 0
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('food-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                x += 1
    except:
        pass
    


