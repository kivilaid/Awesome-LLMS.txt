import requests
import os
import time
from urllib.parse import urlparse

def sanitize_filename(name):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '')
    return name.strip()

def download_llms_txt(url, title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
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

# List of failed URLs to retry
failed_urls = [
    ("https://docs.anthropic.com/llms.txt", "Anthropic"),
    ("https://docs.analog.one/documentation/llms.txt", "Analog"),
    ("https://cloudfix.com/llms.txt", "CloudFix"),
    ("https://blogv2.voiceflow.com/llms.txt", "Voiceflow"),
    ("https://www.wized.com/docs/llms.txt", "Wized"),
    ("https://docs.attest.com/llms.txt", "Attest"),
    ("https://docs.remult.dev/llms.txt", "Remult"),
    # Alternative URLs to try
    ("https://docs.anthropic.com/claude/llms.txt", "Anthropic-Alt"),
    ("https://analog.one/llms.txt", "Analog-Alt"),
    ("https://www.cloudfix.com/llms.txt", "CloudFix-Alt"),
    ("https://voiceflow.com/llms.txt", "Voiceflow-Alt"),
    ("https://wized.com/llms.txt", "Wized-Alt"),
    ("https://attest.com/llms.txt", "Attest-Alt"),
    ("https://remult.dev/llms.txt", "Remult-Alt")
]

# Create directory if it doesn't exist
os.makedirs('/Users/ai/Github/Awesome-LLMS.txt/', exist_ok=True)

# Download each llms.txt file
total = len(failed_urls)
for i, (url, title) in enumerate(failed_urls, 1):
    print(f"\nRetry {i}/{total}: Downloading {title} from {url}")
    success = download_llms_txt(url, title)
    # Add a delay between requests
    time.sleep(2)

print("\nRetry process completed!")