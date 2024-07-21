import requests
from bs4 import BeautifulSoup
import json

url = "https://www.codechef.com/one_deepak"  # Replace with the actual URL
headers = {
    'authority': 'www.codechef.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"115.0.5790.110"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.110", "Chromium";v="115.0.5790.110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Referer': 'https://codechef.com',
}

response = requests.get(url)
data = response.text
consol

heat_map_data_cursor1 = data.find("var userDailySubmissionsStats =") + len("var userDailySubmissionsStats =")
heat_map_data_cursor2 = data.find("'#js-heatmap") - 9
heat_data_string = data[heat_map_data_cursor1:heat_map_data_cursor2]
heat_map_data = json.loads(heat_data_string)

all_rating_cursor1 = data.find("var all_rating = ") + len("var all_rating = ")
all_rating_cursor2 = data.find("var current_user_rating =") - 6
rating_data_string = data[all_rating_cursor1:all_rating_cursor2]
rating_data = json.loads(rating_data_string)

soup = BeautifulSoup(data, 'html.parser')

profile = soup.select_one(".user-details-container img")['src']
name = soup.select_one(".user-details-container .user-name").text
current_rating = int(soup.select_one(".rating-number").text)
highest_rating = int(soup.select_one(".rating-number").find_next_sibling().text.split("Rating")[1])
country_flag = soup.select_one(".user-country-flag")['src']
country_name = soup.select_one(".user-country-name").text
global_rank = int(soup.select_one(".rating-ranks .global-rank .rank").text)
country_rank = int(soup.select_one(".rating-ranks .country-rank .rank").text)
stars = soup.select_one(".rating").text if soup.select_one(".rating") else "unrated"

result = {
    "success": True,
    "profile": profile,
    "name": name,
    "currentRating": current_rating,
    "highestRating": highest_rating,
    "countryFlag": country_flag,
    "countryName": country_name,
    "globalRank": global_rank,
    "countryRank": country_rank,
    "stars": stars,
    "heatMap": heat_map_data,
    "ratingData": rating_data,
}

print(result)
