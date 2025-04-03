import requests
import json
from bs4 import BeautifulSoup
from typing import List, Dict, Any

def get_fixed_data() -> List[Dict[str, Any]]:
    """Return the predefined list of all entries."""
    # This is a fixed list of the first few entries as an example
    return [
        {
            "url": "https://llmstxt.org/llms.txt",
            "urlFull": None,
            "title": "llms.txt",
            "category": "Websites",
            "description": "A proposal to standardise on using an /llms.txt file to provide information to help LLMs use a website at inference time.",
            "mainDomain": "https://llmstxt.org",
            "down": False,
            "llms-txt-tokens": 160,
            "llms-full-txt-tokens": 0
        },
        {
            "url": "https://docs.anthropic.com/llms.txt",
            "urlFull": "https://docs.anthropic.com/llms-full.txt",
            "title": "Anthropic",
            "category": "AI",
            "description": "Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.",
            "mainDomain": "https://anthropic.com",
            "down": False,
            "llms-txt-tokens": 6949,
            "llms-full-txt-tokens": 388044
        },
        # ... Add all additional entries here
    ]

def convert_to_products_format(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert directory entries to products_data.json format."""
    products = []
    for entry in entries:
        product = {
            "product": entry["title"],
            "website": entry["mainDomain"],
            "llms-txt": entry["url"],
            "llms-txt-tokens": entry["llms-txt-tokens"],
            "llms-full-txt": entry["urlFull"] if entry["urlFull"] else "",
            "llms-full-txt-tokens": entry["llms-full-txt-tokens"] if entry["llms-full-txt-tokens"] else None,
            "category": entry["category"]
        }
        products.append(product)
    return products

def save_products_json(products: List[Dict[str, Any]], filename: str):
    """Save products data to JSON file with proper formatting."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4)

def main():
    try:
        # Get the data
        print("Getting directory data...")
        entries = get_fixed_data()
        
        # Convert to products format
        print("Converting to products format...")
        products = convert_to_products_format(entries)
        
        # Save to new JSON file
        output_file = '/Users/ai/Github/Awesome-LLMS.txt/all_products_data.json'
        save_products_json(products, output_file)
        print(f"Saved {len(products)} products to {output_file}")
        
        # Print first few entries as a sample
        print("\nSample of converted data:")
        for product in products[:2]:
            print(json.dumps(product, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()