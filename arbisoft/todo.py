import requests
import json


def fetch_and_process_data(api_url):
    # Fetching the data from the API
    response = requests.get(api_url)
    todos_data = response.json()

    # Analyzing the data to find users who completed the most tasks
    completed_tasks_by_user = {}
    for todo in todos_data:
        if todo['completed']:
            user_id = todo['userId']
            completed_tasks_by_user[user_id] = completed_tasks_by_user.get(
                user_id, 0) + 1

    return completed_tasks_by_user, todos_data


def find_users_with_max_tasks(completed_tasks_by_user):
    # Finding the maximum number of completed tasks
    max_completed_tasks = max(completed_tasks_by_user.values())

    # Filtering users who have completed the maximum number of tasks
    return [user for user, count in completed_tasks_by_user.items() if count == max_completed_tasks]


def create_json_for_max_users(users_with_max_tasks, todos_data):
    # Preparing the final JSON with todos for these users
    final_json = {}
    for user in users_with_max_tasks:
        final_json[user] = [
            todo for todo in todos_data if todo['userId'] == user and todo['completed']]
    return final_json


def main():
    api_url = 'https://jsonplaceholder.typicode.com/todos'

    completed_tasks_by_user, todos_data = fetch_and_process_data(api_url)
    users_with_max_tasks = find_users_with_max_tasks(completed_tasks_by_user)
    final_json = create_json_for_max_users(users_with_max_tasks, todos_data)

    # Writing the result to a JSON file
    with open('completed_tasks_max_users.json', 'w') as file:
        json.dump(final_json, file, indent=4)

    print("JSON file created for users with the maximum completed tasks.")
    print(f"users_with_max_task{users_with_max_tasks}")
    print(f"completed_tasks_by_user {completed_tasks_by_user}")


if __name__ == "__main__":
    main()


def read_and_process_data(file_path):
    # Reading data from a JSON file
    with open(file_path, 'r') as file:
        todos_data = json.load(file)

    # Analyzing the data to find users who completed the most tasks
    completed_tasks_by_user = {}
    for todo in todos_data:
        if todo['completed']:
            user_id = todo['userId']
            completed_tasks_by_user[user_id] = completed_tasks_by_user.get(
                user_id, 0) + 1

    return completed_tasks_by_user, todos_data


def find_users_with_max_tasks(completed_tasks_by_user):
    # Finding the maximum number of completed tasks
    max_completed_tasks = max(completed_tasks_by_user.values())

    # Filtering users who have completed the maximum number of tasks
    return [user for user, count in completed_tasks_by_user.items() if count == max_completed_tasks]


def post_users_data(api_url, users_with_max_tasks):
    # Posting data for users with max tasks to the API
    for user_id in users_with_max_tasks:
        response = requests.post(api_url, json={"userId": user_id})
        print(
            f"Posted data for user {user_id}: Response {response.status_code}")


def main():
    # Replace with the actual JSON file path
    json_file_path = 'path_to_json_file.json'
    # Replace with the actual API endpoint
    api_url = 'https://jsonplaceholder.typicode.com/users'
    completed_tasks_by_user, _ = read_and_process_data(json_file_path)
    users_with_max_tasks = find_users_with_max_tasks(completed_tasks_by_user)
    post_users_data(api_url, users_with_max_tasks)


if __name__ == "__main__":
    main()
