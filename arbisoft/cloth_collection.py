import requests
import json


def get_discount_percentage(price, previous_price):
    """Calculate the discount percentage."""
    return ((previous_price - price) / previous_price) * 100


def count_products_on_sale(data, collection_name, discount_limit):
    """Count the number of products on sale above the discount limit in a collection."""
    count = 0
    for product in data:
        if product['collection'] == collection_name:
            discount_percentage = get_discount_percentage(
                product['price'], product['previous_price'])
            if discount_percentage >= discount_limit:
                count += 1
    return count


def main(input_file_path):
    # Load the JSON data from the API
    api_url = "https://jsonkeeper.com/b/ZVOV"
    response = requests.get(api_url)
    data = response.json()

    # Read the input file for test cases
    with open(input_file_path, 'r') as file:
        test_cases = int(file.readline().strip())
        for _ in range(test_cases):
            collection_name, discount_limit = file.readline().strip().split(',')
            discount_limit = float(discount_limit)
            result = count_products_on_sale(
                data, collection_name, discount_limit)
            print(result)


# The input file path should be the path to your input file
input_file_path = 'path_to_your_input_file.txt'
main(input_file_path)
