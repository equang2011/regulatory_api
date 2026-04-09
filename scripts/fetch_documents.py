import requests, json
from datetime import datetime
from pathlib import Path


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

model_keys = {
    "title",
    "type",
    "document_number",
    "publication_date",
    "ingested_date",
    "agencies_text",
    "html_url",
    "abstract",
    "excerpts",
}


def process_doc(record):
    result = {}
    for key in record:
        if key == "agencies":

            result["agencies_text"] = ", ".join(
                [a["name"] for a in record.get("agencies", [])]
            )
        else:
            if key in model_keys:
                result[key] = record[key]
    result["ingested_date"] = date_today
    return result


records = []
for obj in output:
    data = process_doc(obj)
    records.append(data)

output_path = Path("data") / f"federal_register_{date_today}.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)
