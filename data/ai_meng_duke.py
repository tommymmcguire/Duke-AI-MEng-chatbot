import requests
from bs4 import BeautifulSoup
import re
import csv
import os

# URLs to scrape
urls = [
    'https://ai.meng.duke.edu/degree',
    'https://ai.meng.duke.edu/certificate',
    'https://ai.meng.duke.edu/courses',
    'https://ai.meng.duke.edu/faculty',
    'https://ai.meng.duke.edu/apply',
    'https://ai.meng.duke.edu/why-duke',
    'https://ai.meng.duke.edu/why-duke/career-services',
    'https://ai.meng.duke.edu/why-duke/graduate-outcomes',
    'https://ai.meng.duke.edu/why-duke/tech-leaders'
]

def scrape_and_save(urls):
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            body = soup.find('div', id='content-body')
            body_text = body.get_text(separator='\n')
            cleaned_text = re.sub(r'\n\n', '\n', body_text).strip()

            # Extract the name for the CSV file from the URL
            filename = url.split('/')[-1] if url.split('/')[-1] != '' else url.split('/')[-2]
            path = f'{filename}.txt'

            # Write the cleaned text to a .txt file
            with open(path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            print(f'Content from {url} has been saved to {path}')
        else:
            print(f'Failed to retrieve the webpage {url}. Status code: {response.status_code}')

# Call the function with the list of URLs
scrape_and_save(urls)
