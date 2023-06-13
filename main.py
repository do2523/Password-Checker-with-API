import requests  # like having a browser without a browster


def request_api_data(query_characters):
    # API below
    url = "https://api.pwnedpasswords.com/range/" + query_characters # uses Hashing
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')

def pwned_api_check(password):
    # Check Password if it exists in API response
    pass

request_api_data("321")