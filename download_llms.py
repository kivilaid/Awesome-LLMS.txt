import requests
import os
import time
from urllib.parse import urlparse

def sanitize_filename(name):
    # Remove any characters that aren't allowed in filenames
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '')
    return name.strip()

def download_llms_txt(url, title):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            filename = sanitize_filename(title) + '.txt'
            filepath = os.path.join('/Users/ai/Github/Awesome-LLMS.txt/', filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Successfully downloaded: {filename}")
            return True
        else:
            print(f"Failed to download {title}: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {title}: {str(e)}")
        return False

# List of URLs and titles - first page only for now
urls = [
    ("https://docs.1millionbot.com/llms.txt", "1MillionBot"),
    ("https://docs.1rpc.io/llms.txt", "1RPC"),
    ("https://docs.48.club/llms.txt", "48 Club"),
    ("https://docs.4everland.org/llms.txt", "4EVERLAND"),
    ("https://docs.a2rev.com/llms.txt", "A2Reviews"),
    ("https://docs.abcproxy.com/llms.txt", "ABCProxy"),
    ("https://docs.abs.xyz/llms.txt", "Abstract"),
    ("https://docs.abstractapi.com/llms.txt", "Abstract API"),
    ("https://docs.acrcloud.com/llms.txt", "ACRCloud"),
    ("https://docs.across.to/llms.txt", "Across"),
    ("https://www.activepieces.com/docs/llms.txt", "Activepieces"),
    ("https://docs.adgatemedia.com/llms.txt", "AdGate Media"),
    ("https://docs.adly.tech/llms.txt", "Adly"),
    ("https://docs.admira.com/llms.txt", "Admira"),
    ("https://docs.adnuntius.com/llms.txt", "ADNUNTIUS"),
    ("https://docs.adpies.com/llms.txt", "AdPie"),
    ("https://docs.advinservers.com/llms.txt", "Advin Servers"),
    ("https://docs.adxcorp.kr/llms.txt", "ADX"),
    ("https://docs.aethir.com/llms.txt", "Aethir"),
    ("https://docs.aevo.xyz/llms.txt", "Aevo"),
    # Add more URLs here...
]

# Create directory if it doesn't exist
os.makedirs('/Users/ai/Github/Awesome-LLMS.txt/', exist_ok=True)

# Download each llms.txt file
for url, title in urls:
    print(f"\nDownloading {title} from {url}")
    success = download_llms_txt(url, title)
    # Add a small delay between requests to be nice to servers
    time.sleep(1)

print("\nDownload process completed!")