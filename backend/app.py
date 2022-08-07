import requests
def home_handler(event, context):
    r = requests.get('https://reqres.in/api/users/2')
    message = 'Hello you'
    content = 'chau'
    return "Hello\n"

