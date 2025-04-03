import requests
import json
import time
from bs4 import BeautifulSoup
from typing import List, Dict, Any

def get_page_html(page_number: int) -> str:
    """Get HTML from a specific page number."""
    url = f"https://directory.llmstxt.cloud/?page={page_number}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page {page_number}: {response.status_code}")
    return response.text

def extract_entries_from_html(html: str) -> List[Dict[str, Any]]:
    """Extract directory entries from page HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    entries = []
    
    # Find all entry divs
    for entry_div in soup.find_all('li', class_="p-4 rounded-lg"):
        try:
            # Extract title and link
            title_link = entry_div.find('h3', class_="font-semibold").text.strip()
            
            # Extract category
            category_span = entry_div.find('span', class_="text-xs")
            category = category_span.text.strip() if category_span else ""
            
            # Extract URLs
            links = entry_div.find_all('a', class_="inline-flex")
            llms_txt_link = None
            llms_full_txt_link = None
            
            for link in links:
                link_text = link.text.strip()
                if '/llms.txt' in link_text:
                    llms_txt_link = link.get('href')
                elif '/llms-full.txt' in link_text:
                    llms_full_txt_link = link.get('href')
            
            # Extract token counts
            token_spans = entry_div.find_all('span', class_="tokens-count")
            llms_txt_tokens = 0
            llms_full_txt_tokens = None
            
            for span in token_spans:
                text = span.text.strip()
                tokens = int(text.split()[0])
                if 'llms.txt' in str(span.previous_sibling):
                    llms_txt_tokens = tokens
                elif 'llms-full.txt' in str(span.previous_sibling):
                    llms_full_txt_tokens = tokens
            
            # Create entry dictionary
            entry = {
                "product": title_link,
                "website": "",  # Main website URL is not directly available
                "llms-txt": llms_txt_link,
                "llms-txt-tokens": llms_txt_tokens,
                "llms-full-txt": llms_full_txt_link if llms_full_txt_link else "",
                "llms-full-txt-tokens": llms_full_txt_tokens,
                "category": category
            }
            entries.append(entry)
            
        except Exception as e:
            print(f"Error processing entry: {str(e)}")
            continue
    
    return entries

def load_existing_json(filename: str) -> List[Dict[str, Any]]:
    """Load existing JSON file or return empty list if file doesn't exist."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(data: List[Dict[str, Any]], filename: str):
    """Save data to JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    output_file = '/Users/ai/Github/Awesome-LLMS.txt/all_products_data.json'
    all_entries = []
    
    # Process each page (8 pages total)
    for page in range(1, 9):
        print(f"\nProcessing page {page}...")
        try:
            # Get and parse page
            html = get_page_html(page)
            entries = extract_entries_from_html(html)
            
            print(f"Found {len(entries)} entries on page {page}")
            all_entries.extend(entries)
            
            # Add delay between pages
            if page < 8:
                print("Waiting before next page...")
                time.sleep(2)
                
        except Exception as e:
            print(f"Error processing page {page}: {str(e)}")
            continue
    
    # Save all entries
    print(f"\nSaving {len(all_entries)} total entries to {output_file}")
    save_json(all_entries, output_file)
    
    # Print sample of first entry
    if all_entries:
        print("\nSample entry:")
        print(json.dumps(all_entries[0], indent=2))

if __name__ == "__main__":
    main()