import json
import re
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup

def get_page_html() -> str:
    """Get the initial HTML that contains the data."""
    url = "https://directory.llmstxt.cloud/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")
    return response.text

def extract_data_from_props(html: str) -> List[Dict[str, Any]]:
    """Extract the data array from astro-island props."""
    # Find the astro-island element with the data
    soup = BeautifulSoup(html, 'html.parser')
    island = soup.find('astro-island', attrs={'uid': 'Z1fTkxW'})
    if not island:
        raise Exception("Could not find data element")
    
    # Get the props attribute
    props = island.get('props', '')
    
    # Find the array in the props
    match = re.search(r'directoryItems":\[1,(\[\[.*?\]\])\]', props, re.DOTALL)
    if not match:
        raise Exception("Could not find data array in props")
    
    # Extract and clean the array string
    array_str = match.group(1)
    array_str = array_str.replace('true', 'True').replace('false', 'False').replace('null', 'None')
    
    # Safely evaluate the string to get Python objects
    data = eval(array_str)
    
    # Convert the data to our format
    entries = []
    for item in data:
        if not isinstance(item, list) or len(item) < 2:
            continue
            
        entry_data = item[1]
        # Extract the actual values from the [0, value] format
        entry = {
            "product": entry_data.get("title", ["", ""])[1],
            "website": entry_data.get("mainDomain", ["", ""])[1],
            "llms-txt": entry_data.get("url", ["", ""])[1],
            "llms-txt-tokens": entry_data.get("llms-txt-tokens", [0, 0])[1],
            "llms-full-txt": entry_data.get("urlFull", ["", None])[1] or "",
            "llms-full-txt-tokens": entry_data.get("llms-full-txt-tokens", [0, None])[1],
            "category": entry_data.get("category", ["", ""])[1]
        }
        entries.append(entry)
    
    return entries

def save_json(data: List[Dict[str, Any]], filename: str):
    """Save data to JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    output_file = '/Users/ai/Github/Awesome-LLMS.txt/all_products_data.json'
    
    try:
        # Get the HTML and extract data
        print("Fetching website data...")
        html = get_page_html()
        
        print("Extracting entries...")
        entries = extract_data_from_props(html)
        
        # Save all entries
        print(f"\nSaving {len(entries)} entries to {output_file}")
        save_json(entries, output_file)
        
        # Print sample entries
        print("\nSample entries:")
        for entry in entries[:2]:
            print(json.dumps(entry, indent=2))
            print()
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()