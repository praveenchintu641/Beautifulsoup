from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Use find instead of find_all_next, and specify the class as a string
table = soup.find('table', class_='wikitable sortable')

# Check if the table is found
if table:
    world_titles = [th.text.strip() for th in table.find_all('th')[1:9]]
    print(world_titles)

    df = pd.DataFrame(columns=world_titles)

    column_data = table.find_all('tr')
    for row in column_data[2:]:
        row_data = row.find_all('td')[:8]
        individual_row_data = [data.text.strip() for data in row_data]
        length = len(df)
        df.loc[length] = individual_row_data

    df.to_csv(r'C:\Users\prave\OneDrive\Desktop\python\final.csv')
else:
    print("Table not found on the page.")


#image


img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Walmart_store_exterior_5266815680.jpg/1200px-Walmart_store_exterior_5266815680.jpg'


image_data = requests.get(img_url).content

with open(r'C:\Users\prave\OneDrive\Desktop\python\downloaded_image.jpg', 'wb') as f:
    f.write(image_data)

print('Image downloaded successfully.')
