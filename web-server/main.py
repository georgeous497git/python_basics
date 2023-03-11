import store_request.store_request as sr
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_data():
    return 'Welcome!'


@app.get('/data')
def get_data():
    return dict(language = 'Python', version = 3.11, level = 'Basics')


@app.get('/info')
def get_data():
    return dict(name = 'Jorge', last_name = 'Correa', country = 'MX')


def run():
    sr.get_employees()

if __name__ == '__main__':
    run()
