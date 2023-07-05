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

if __name__ == "__main__":
    main()
