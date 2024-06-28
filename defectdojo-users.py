import logging
import requests, argparse, os

def main():
    
    if not os.environ['DEFECTDOJO_API_KEY']:
        logging.error("DEFECTDOJO_API_KEY environmnent variable not populated. Exiting.")
        exit()
    api_key = os.environ['DEFECTDOJO_API_KEY']
    
    headers = {
        'content-type': 'application/json',
        'Authorization': f"Token {api_key}"
    }

    proxies = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"}

    users_url = "https://defectdojo.batcave.internal.cms.gov/api/v2/users/?limit=100"

    r = requests.get(users_url, headers=headers)

    # Figure out using python requests documentation at https://pypi.org/project/requests/ how to get the JSON of the response

    # Get the JSON response
    response_json = r.json()
    print(response_json) #<---- answer goes into the parentheses

privateKey = """ -----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
"""
    

# r = requests.get('https://httpbin.org/basic-auth/user/pass'


if __name__ == "__main__":
    main()
