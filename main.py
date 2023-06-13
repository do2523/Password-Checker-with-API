import requests  # like having a browser without a browster
import hashlib # contains many of the SHA Hashings


def request_api_data(query_characters):
    # API below
    url = "https://api.pwnedpasswords.com/range/" + query_characters  # uses Hashing
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':'))  # splitting password an num times it's been hacked


def pwned_api_check(password):
    # Check Password if it exists in API response
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()  # In documentation for more info
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_password_leaks_count(response)

pwned_api_check("password")