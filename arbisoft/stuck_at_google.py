# Assuming previous functions (read_trip_id and fetch_data_from_api) are defined above

import requests


def process_data(data):
    # Grouping timelines by masks
    grouped_data = {}
    for timeline, mask in zip(data['timelines'], data['masks']):
        if mask not in grouped_data:
            grouped_data[mask] = []
        grouped_data[mask].append(timeline)

    # Perform sub-operations
    sub_operations = data['action_plan']['sub_operations']
    results = {}
    for mask, values in grouped_data.items():
        operation = sub_operations.get(mask)
        if operation == "BAR":
            results[mask] = min(values)
        elif operation == "FOX":
            results[mask] = max(values)
        elif operation == "FOO":
            results[mask] = sum(values)
        else:
            results[mask] = 0

    # Perform final operation
    final_operation = data['action_plan']['operation']
    final_data = list(results.values())
    if final_operation == "FOO":
        return sum(final_data)
    # Add other final operations if needed

    return 0


def read_trip_id(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


def fetch_data_from_api(trip_id):
    api_url = f"https://jsonkeeper.com/b/{trip_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def main():
    file_path = 'input_file.txt'  # Replace with your input file path
    trip_id = read_trip_id(file_path)
    api_data = fetch_data_from_api(trip_id)

    if api_data:
        final_result = process_data(api_data)
        print("Final Result:", final_result)
    else:
        print("Failed to fetch data from API")


if __name__ == "__main__":
    main()
