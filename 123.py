import csv
import json
import requests
coffeeurl_content = requests.get("https://api.sampleapis.com/coffee/hot")
coffeeurl_json = coffeeurl_content.json()
coffee_titles = []
for coffee_item in coffeeurl_json:
    coffee_titles.append(coffee_item["title"])
coffee_titles_sorted = sorted(coffee_titles)
print(coffee_titles_sorted)
