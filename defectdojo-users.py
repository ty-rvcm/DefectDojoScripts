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


    

# r = requests.get('https://httpbin.org/basic-auth/user/pass'


if __name__ == "__main__":
    main()