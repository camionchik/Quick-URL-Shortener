import requests
import pyperclip
import sys
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from config.json."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("config.json file not found!")
        sys.exit(1)

def shorten_url(long_url, config):
    """Shorten the URL using the selected service."""
    service = config.get("service", "tinyurl")
    if service == "tinyurl":
        api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
        response = requests.get(api_url)
    elif service == "bitly" and "bitly_token" in config:
        headers = {"Authorization": f"Bearer {config['bitly_token']}"}
        payload = {"long_url": long_url}
        response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["link"]
    else:
        logger.error("Invalid service or missing Bitly token!")
        return None

    if response.status_code == 200:
        return response.text if service == "tinyurl" else None
    logger.error(f"API error: {response.status_code}")
    return None

def main():
    if len(sys.argv) != 2:
        logger.error("Usage: python shortener.py <long_url>")
        sys.exit(1)

    long_url = sys.argv[1]
    config = load_config()
    short_url = shorten_url(long_url, config)

    if short_url:
        pyperclip.copy(short_url)
        logger.info(f"Shortened URL: {short_url} (Copied to clipboard!)")
    else:
        logger.error("Failed to shorten URL. Please check the URL and try again.")

if __name__ == "__main__":
    main()
