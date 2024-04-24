import requests
import sys

def get_todo_list_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Employee not found.")
        return

    user = response.json()
    todos = requests.get(url + "/todos").json()

    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
