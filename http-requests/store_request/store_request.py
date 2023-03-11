import requests

def get_employees():
    # r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # r = requests.get('https://dummy.restapiexample.com/api/v1/employees')
    r = requests.get('https://api.github.com')
    print(f' {r.status_code = } ')
    # printing row data
    print(f' {r.text = } ')

    print(f' {r = } ')
    response = r.json()
    user_url = response['current_user_url']

    print(f' {user_url = } ')
