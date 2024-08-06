import os
import requests
import time
import logging

URL = os.getenv("URL")

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def make_https_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        logging.info("Request successful!")
    except requests.exceptions.HTTPError as http_err:
        logging.error(http_err)
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(conn_err)
    except requests.exceptions.Timeout as timeout_err:
        logging.error(timeout_err)
    except requests.exceptions.RequestException as req_err:
        logging.error(req_err)

# Example usage
url = f"https://{URL}"

while True:
    make_https_request(url)
    time.sleep(5)
