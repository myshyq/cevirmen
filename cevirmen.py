from bs4 import BeautifulSoup
import requests
import time
import sys 

url = "https://dictionary.cambridge.org/dictionary/english-turkish/"+sys.argv[1]
retries = 5
delay = 2  # Seconds between retries
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    trans_elements = soup.find_all('span', class_='trans dtrans dtrans-se')

    print(trans_elements[0].get_text(strip=True))


else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

