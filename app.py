from flask import Flask
import requests

app = Flask(__name__)

def request_api_data(query_characters):
    url = "https://api.pwnedpasswords.com/range/" + query_characters
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res



if __name__ == '__main__':
    app.run()
