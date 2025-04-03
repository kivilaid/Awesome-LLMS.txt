import json
from typing import List, Dict, Optional, Any

# Each website entry from the HTML has this structure:
"""
{
    "url": "https://docs.example.com/llms.txt",
    "urlFull": "https://docs.example.com/llms-full.txt",  # or null
    "title": "Example Product",
    "category": "AI",
    "description": "Product description",
    "mainDomain": "https://example.com",
    "down": false,
    "llms-txt-tokens": 1234,
    "llms-full-txt-tokens": 5678  # or 0
}
"""

# Extracted website data (copied from website HTML)
data = [{"url":"https://llmstxt.org/llms.txt","urlFull":None,"title":"llms.txt","category":"Websites","description":"A proposal to standardise on using an /llms.txt file to provide information to help LLMs use a website at inference time.","mainDomain":"https://llmstxt.org","down":False,"llms-txt-tokens":160,"llms-full-txt-tokens":0},{"url":"https://docs.anthropic.com/llms.txt","urlFull":"https://docs.anthropic.com/llms-full.txt","title":"Anthropic","category":"AI","description":"Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.","mainDomain":"https://anthropic.com","down":False,"llms-txt-tokens":6949,"llms-full-txt-tokens":388044},{"url":"https://docs.perplexity.ai/llms.txt","urlFull":"https://docs.perplexity.ai/llms-full.txt","title":"Perplexity","category":"AI","description":"Perplexity AI is an AI-powered search engine that provides direct answers to user queries by leveraging large language models.","mainDomain":"https://perplexity.ai","down":False,"llms-txt-tokens":453,"llms-full-txt-tokens":10093},{"url":"https://developers.cloudflare.com/llms.txt","urlFull":"https://developers.cloudflare.com/llms-full.txt","title":"Cloudflare","category":"Developer tools","description":"Make employees, applications and networks faster and more secure everywhere, while reducing complexity and cost.","mainDomain":"https://www.cloudflare.com/","down":False,"llms-txt-tokens":32628,"llms-full-txt-tokens":3688603},{"url":"https://sdk.vercel.ai/llms.txt","urlFull":None,"title":"Vercel AI SDK","category":"Developer tools","description":"The AI Toolkit for TypeScript, from the creators of Next.js.","mainDomain":"https://sdk.vercel.ai/","down":False,"llms-txt-tokens":111921,"llms-full-txt-tokens":0},{"url":"https://docs.cursor.com/llms.txt","urlFull":"https://docs.cursor.com/llms-full.txt","title":"Cursor","category":"AI","description":"The AI Code Editor","mainDomain":"https://cursor.com","down":False,"llms-txt-tokens":2029,"llms-full-txt-tokens":37741},{"url":"https://elevenlabs.io/docs/llms.txt","urlFull":"https://elevenlabs.io/docs/llms-full.txt","title":"ElevenLabs","category":"AI","description":"Create the most realistic speech with our AI audio in 1000s of voices and 32 languages. Pioneering research in Text to Speech and AI Voice Generation","mainDomain":"https://elevenlabs.io","down":False,"llms-txt-tokens":10041,"llms-full-txt-tokens":455706,"skipCheck":True},{"url":"https://docs.cdp.coinbase.com/llms.txt","urlFull":None,"title":"Coinbase","category":"Finance","description":"Buy & Sell Bitcoin, Ethereum, and more with trust.","mainDomain":"https://www.coinbase.com/","down":False,"llms-txt-tokens":11449,"llms-full-txt-tokens":0},{"url":"https://modelcontextprotocol.io/llms.txt","urlFull":"https://modelcontextprotocol.io/llms-full.txt","title":"Model Context Protocol","category":"AI","description":"Get started with the Model Context Protocol (MCP).","mainDomain":"https://modelcontextprotocol.io/","down":False,"llms-txt-tokens":738,"llms-full-txt-tokens":46753},{"url":"https://huggingface-projects-docs-llms-txt.hf.space/transformers/llms.txt","urlFull":None,"title":"Hugging Face Transformers","category":"AI","description":"State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX.","mainDomain":"https://huggingface.co/","down":False,"llms-txt-tokens":812605,"llms-full-txt-tokens":0},{"url":"https://huggingface-projects-docs-llms-txt.hf.space/diffusers/llms.txt","urlFull":None,"title":"Hugging Face Diffusers","category":"AI","description":"Diffusers is the go-to library for state-of-the-art pretrained diffusion models for generating images, audio, and even 3D structures of molecules.","mainDomain":"https://huggingface.co/","down":False,"llms-txt-tokens":383423,"llms-full-txt-tokens":0},{"url":"https://huggingface-projects-docs-llms-txt.hf.space/accelerate/llms.txt","urlFull":None,"title":"Hugging Face Accelerate","category":"AI","description":"Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration by adding just four lines of code! In short, training and inference at scale made simple, efficient and adaptable.","mainDomain":"https://huggingface.co/","down":False,"llms-txt-tokens":82137,"llms-full-txt-tokens":0},{"url":"https://huggingface-projects-docs-llms-txt.hf.space/hub/llms.txt","urlFull":None,"title":"Hugging Face Hub","category":"AI","description":"The Hugging Face Hub is a platform with over 900k models, 200k datasets, and 300k demo apps (Spaces), all open source and publicly available, in an online platform where people can easily collaborate and build ML together.","mainDomain":"https://huggingface.co/","down":False,"llms-txt-tokens":209827,"llms-full-txt-tokens":0},{"url":"https://mintlify.com/docs/llms.txt","urlFull":"https://mintlify.com/docs/llms-full.txt","title":"Mintlify","category":"Developer tools","description":"Meet the modern standard for public facing documentation. Beautiful out of the box, easy to maintain, and optimized for user engagement.","mainDomain":"https://mintlify.com","down":False,"llms-txt-tokens":2732,"llms-full-txt-tokens":89613},{"url":"https://svelte.dev/llms.txt","urlFull":"https://svelte.dev/llms-full.txt","title":"Svelte","category":"Developer tools","description":"Web development for the rest of us.","mainDomain":"https://svelte.dev/","down":False,"llms-txt-tokens":279,"llms-full-txt-tokens":223426},{"url":"https://docs.play.ai/llms.txt","urlFull":"https://docs.play.ai/llms-full.txt","title":"PlayAI","category":"Developer tools","description":"Tavus is the leading AI video research company that enables product development teams to build white-labeled digital twin experiences with easy-to-use APIs.","mainDomain":"https://www.tavus.io/","down":False,"llms-txt-tokens":3959,"llms-full-txt-tokens":37697},{"url":"https://docs.zapier.com/llms.txt","urlFull":"https://docs.zapier.com/llms-full.txt","title":"Zapier","category":"Products","description":"Workflow automation software for everyone. Automate your work across 7,000+ app integrations—no developers, no IT tickets, no delays.","mainDomain":"https://zapier.com","down":False,"llms-txt-tokens":13876,"llms-full-txt-tokens":265377}]

def convert_to_products_format(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert website entries to products_data.json format."""
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
    # Convert data to products format
    products = convert_to_products_format(data)
    
    # Save to new JSON file
    output_file = '/Users/ai/Github/Awesome-LLMS.txt/all_products_data.json'
    save_products_json(products, output_file)
    print(f"Saved {len(products)} products to {output_file}")

if __name__ == "__main__":
    main()