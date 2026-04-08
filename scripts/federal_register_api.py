import requests, json
from datetime import datetime


federal_register_url = "https://www.federalregister.gov/api/v1/documents.json"

date_today = datetime.today().strftime("%Y-%m-%d")

params = {
    "conditions[publication_date][is]": date_today,
    "page": 1,
}


response = requests.get(federal_register_url, params=params)

data = response.json()

page_count = data["total_pages"]

output = []

for i in range(page_count):
    params["page"] = i + 1
    response = requests.get(federal_register_url, params=params)
    data = response.json()

    output.extend(data["results"])

print(len(output))
print(output[:1])
# print(results[:1])
# print(len(results))
