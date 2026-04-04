import json, csv, copy

input_file = "data/federal_register_processed.json"


def safe_load_json(filepath):
    """Load JSON file with error handling."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{filepath}' is not valid JSON")
        return None


file = safe_load_json(input_file)
if file is None:
    print("Cannot proceed without data. Exiting.")
    exit()


def filter_by_agency(data, agency_name):
    """Filter documents by agency name. Returns list of matching docs."""
    if data is None or not data:
        print(f"No data provided")
        return []

    if not agency_name:
        print("No agency name provided")
        return []
    result = []

    for dict in data:
        agency_list = dict.get("agencies", [])
        if agency_name in agency_list:
            result.append(dict)
    print(result)


def filter_by_type(data, doc_type):
    """Filter documents by type. Returns list of matching docs."""
    if data is None or not data:
        print(f"No data provided")
        return []

    if not doc_type:
        print("No document type provided")
        return []
    result = []

    for dict in data:
        type = dict.get("type", [])
        if type == doc_type:
            result.append(dict)
    print(result)
    print(len(result))
    return result


def count_by_agency(data):
    """Returns counter of docs by agency"""
    if not data:
        return {}
    counter = {}
    for obj in data:
        agencies = obj.get("agencies", [])
        if agencies:
            for agency in agencies:
                if agency not in counter:
                    counter[agency] = 0
                counter[agency] += 1

    for key in counter:
        print(f"{key} has {counter[key]} results")


def count_by_type(data):
    """Returns a count per doc type"""
    if not data:
        return {}
    counter = {}
    for obj in data:
        doc_type = obj.get("type", [])
        if not doc_type:
            return  # just for safety

        if doc_type not in counter:
            counter[doc_type] = 1
        else:
            counter[doc_type] += 1
    return counter


def sort_by_date(data, ascending=False):
    if not data:
        return
    result = []
    for obj in data:
        date = obj.get("publication_date", [])

        result.append((date, obj))
    if not result:
        return
    result.sort(key=lambda x: x[0], reverse=not ascending)

    return [obj for date, obj in result]


def export_to_csv(data, output_file, columns):
    if not data:
        print("No data to export")
        return 0

    import os

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    data_copy = copy.deepcopy(data)
    for doc in data_copy:
        if "agencies" in columns:
            agencies = doc.get("agencies", [])
            if agencies:
                doc["agencies"] = ", ".join(agencies)

    try:
        with open(output_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(data_copy)

        return len(data_copy)
    except IOError as e:
        print(f"Error writing CSV: {e}")
        return 0


output_file = "data/my_results.csv"
cols = ["title", "type", "publication_date", "agencies"]

if __name__ == "__main__":
    # Test: Find all Notice documents
    notices = filter_by_type(file, "Notice")
    print(f"\nFound {len(notices)} Notice documents")

    # Test: Count documents by agency
    print("\nDocuments by agency:")
    count_by_agency(file)

    # Test: Count documents by type
    print("\nDocuments by type:")
    doc_counts = count_by_type(file)
    for dtype, count in doc_counts.items():
        print(f"  {dtype}: {count}")

    # Test: Export filtered results to CSV
    print("\nExporting Notice documents to CSV...")
    notices = filter_by_type(file, "Notice")
    if not notices:
        print("No results returned")
    else:
        export_to_csv(
            notices,
            "data/notices_export.csv",
            ["title", "type", "publication_date", "agencies"],
        )
        print("Export complete: data/notices_export.csv")
