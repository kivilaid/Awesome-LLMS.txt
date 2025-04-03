import json

# The raw data extracted from the website HTML is a stringified array
raw_data = '[{"url":"https://llmstxt.org/llms.txt","urlFull":null,"title":"llms.txt","category":"Websites","description":"A proposal to standardise on using an /llms.txt file to provide information to help LLMs use a website at inference time.","mainDomain":"https://llmstxt.org","down":false,"llms-txt-tokens":160,"llms-full-txt-tokens":0},{"url":"https://docs.anthropic.com/llms.txt","urlFull":"https://docs.anthropic.com/llms-full.txt","title":"Anthropic","category":"AI","description":"Anthropic is an AI safety and research company that\'s working to build reliable, interpretable, and steerable AI systems.","mainDomain":"https://anthropic.com","down":false,"llms-txt-tokens":6949,"llms-full-txt-tokens":388044}]'

# Parse and format
data = json.loads(raw_data)
formatted = json.dumps(data, indent=4)

# Print Python-style formatted data
print("data = " + formatted.replace("null", "None").replace("false", "False").replace("true", "True"))