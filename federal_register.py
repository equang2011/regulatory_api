import requests, json


source_url = "https://www.federalregister.gov/api/v1/documents.json"


response = requests.get(source_url)

data = response.json()

# print(json.dumps(data, indent=2))

# print(data.keys())
# print(f"Top-level keys: {list(data.keys())}")
# print(len(data["results"]))
# print(data["results"][0].keys())


def explore_schema():
    display_fields = {"title", "publication_date", "type", "agencies"}
    for i in range(20):
        obj = data["results"][i]

        print(f"Document {i}:")
        for key, val in obj.items():

            if key in display_fields:
                if key == "agencies":
                    print(val[0]["name"])
                else:
                    print(f"{key}: {val}")
        print("=" * 30)


file = "data/federal_register_response.json"


def process_doc(obj):
    """takes  a python dictionary"""
    result = dict()
    target_fields = {
        "title",
        "type",
        "abstract",
        "html_url",
        "publication_date",
        "agencies",
        "excerpts",
    }

    for key, val in obj.items():
        if key in target_fields:
            if key == "agencies":
                arr = []
                for i in range(len(obj["agencies"])):
                    arr.append(obj["agencies"][i]["name"])
                result[key] = arr
            else:
                result[key] = val

    for field in target_fields:
        if field not in result:
            result[field] = ""
    return result


arr = []
for i in range(20):
    doc = data["results"][i]
    output = process_doc(doc)
    arr.append(output)

file_name = "fr_test_1.json"
with open(f"data/{file_name}", "w", encoding="utf-8") as f:
    json.dump(arr, f)

with open(f"data/{file_name}", "r") as f:
    loaded_arr = json.load(f)

# Pick one document and verify it looks right
print(loaded_arr[0])
print(loaded_arr[-1])
print(len(loaded_arr))
