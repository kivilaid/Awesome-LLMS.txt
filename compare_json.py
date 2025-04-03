import json
from typing import Dict, List, Any, Set, Tuple

def load_json(filepath: str) -> List[Dict[str, Any]]:
    """Load JSON file and return data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_product_set(data: List[Dict[str, Any]]) -> Set[str]:
    """Get set of product names from data."""
    return {item['product'] for item in data}

def get_product_dict(data: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Convert list to dictionary with product names as keys."""
    return {item['product']: item for item in data}

def compare_products(old_data: List[Dict[str, Any]], new_data: List[Dict[str, Any]]) -> Tuple[List[str], List[str], List[Dict[str, Any]]]:
    """Compare old and new data, return added, removed, and changed products."""
    old_products = get_product_set(old_data)
    new_products = get_product_set(new_data)
    
    added = list(new_products - old_products)
    removed = list(old_products - new_products)
    
    # For products that exist in both, check for changes
    old_dict = get_product_dict(old_data)
    new_dict = get_product_dict(new_data)
    
    changed = []
    for product in old_products & new_products:
        old_item = old_dict[product]
        new_item = new_dict[product]
        
        # Compare all fields except product name
        differences = {}
        for key in ['website', 'llms-txt', 'llms-txt-tokens', 'llms-full-txt', 'llms-full-txt-tokens', 'category']:
            if old_item.get(key) != new_item.get(key):
                differences[key] = {
                    'old': old_item.get(key),
                    'new': new_item.get(key)
                }
        
        if differences:
            changed.append({
                'product': product,
                'changes': differences
            })
    
    return added, removed, changed

def main():
    # Load both JSON files
    old_file = '/Users/ai/Github/Awesome-LLMS.txt/products_data.json'
    new_file = '/Users/ai/Github/Awesome-LLMS.txt/all_products_data.json'
    
    try:
        old_data = load_json(old_file)
        new_data = load_json(new_file)
        
        # Get statistics
        print(f"\nFile Statistics:")
        print(f"Old file entries: {len(old_data)}")
        print(f"New file entries: {len(new_data)}")
        
        # Compare products
        added, removed, changed = compare_products(old_data, new_data)
        
        # Print results
        print(f"\nComparison Results:")
        print(f"Added products: {len(added)}")
        print(f"Removed products: {len(removed)}")
        print(f"Changed products: {len(changed)}")
        
        # Print details
        if added:
            print("\nAdded Products:")
            for product in sorted(added)[:10]:  # Show first 10
                print(f"- {product}")
            if len(added) > 10:
                print(f"... and {len(added) - 10} more")
        
        if removed:
            print("\nRemoved Products:")
            for product in sorted(removed):
                print(f"- {product}")
        
        if changed:
            print("\nChanged Products (sample):")
            for item in changed[:5]:  # Show first 5 changes
                print(f"\n{item['product']}:")
                for field, values in item['changes'].items():
                    print(f"  {field}:")
                    print(f"    Old: {values['old']}")
                    print(f"    New: {values['new']}")
            if len(changed) > 5:
                print(f"... and {len(changed) - 5} more changes")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()