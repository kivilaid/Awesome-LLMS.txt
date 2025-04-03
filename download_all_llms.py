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

# Complete list of URLs and titles from all 8 pages
urls = [
    ("https://llmstxt.org/llms.txt", "llms.txt"),
    ("https://docs.anthropic.com/llms.txt", "Anthropic"),
    ("https://docs.perplexity.ai/llms.txt", "Perplexity"),
    ("https://developers.cloudflare.com/llms.txt", "Cloudflare"),
    ("https://sdk.vercel.ai/llms.txt", "Vercel AI SDK"),
    ("https://docs.cursor.com/llms.txt", "Cursor"),
    ("https://elevenlabs.io/docs/llms.txt", "ElevenLabs"),
    ("https://docs.cdp.coinbase.com/llms.txt", "Coinbase"),
    ("https://modelcontextprotocol.io/llms.txt", "Model Context Protocol"),
    ("https://huggingface-projects-docs-llms-txt.hf.space/transformers/llms.txt", "Hugging Face Transformers"),
    ("https://huggingface-projects-docs-llms-txt.hf.space/diffusers/llms.txt", "Hugging Face Diffusers"),
    ("https://huggingface-projects-docs-llms-txt.hf.space/accelerate/llms.txt", "Hugging Face Accelerate"),
    ("https://huggingface-projects-docs-llms-txt.hf.space/hub/llms.txt", "Hugging Face Hub"),
    ("https://mintlify.com/docs/llms.txt", "Mintlify"),
    ("https://svelte.dev/llms.txt", "Svelte"),
    ("https://docs.play.ai/llms.txt", "PlayAI"),
    ("https://docs.zapier.com/llms.txt", "Zapier"),
    ("https://www.answer.ai/llms.txt", "Answer.AI"),
    ("https://docs.venice.ai/llms.txt", "Venice.ai"),
    ("https://docs.ventrata.com/llms.txt", "Ventrata"),
    ("https://docs.verdn.com/llms.txt", "Verdn"),
    ("https://docs.vertexprotocol.com/llms.txt", "Vertex"),
    ("https://docs.videowise.com/llms.txt", "Videowise"),
    ("https://docs.vooi.io/llms.txt", "VOOI"),
    ("https://docs.vvs.finance/llms.txt", "VVS Finance"),
    ("https://docs.warp.dev/llms.txt", "Warp"),
    ("https://docs.waveonsui.com/llms.txt", "Wave"),
    ("https://docs.weka.io/llms.txt", "WEKA"),
    ("https://docs.whereby.com/llms.txt", "Whereby"),
    ("https://docs.whisk.com/llms.txt", "Samsung Food"),
    ("https://docs.whitechain.io/llms.txt", "Whitechain"),
    ("https://docs.wingbits.com/llms.txt", "Wingbits"),
    ("https://docs.x.com/llms.txt", "X"),
    ("https://docs.x.ink/xos/llms.txt", "XOS"),
    ("https://docs.xdcscan.com/llms.txt", "XDCScan"),
    ("https://docs.xrpscan.com/llms.txt", "XRPSCAN"),
    ("https://docs.yala.org/llms.txt", "Yala"),
    ("https://docs.z1labs.ai/llms.txt", "Zero1 Labs"),
    ("https://docs.zipchat.ai/llms.txt", "Zipchat"),
    ("https://docs.zoko.io/llms.txt", "Zoko"),
    ("https://docs.social.plus/llms.txt", "Social+"),
    ("https://docs.unstructured.io/llms.txt", "Unstructured"),
    ("https://docs.frigade.com/llms.txt", "Frigade"),
    ("https://docs.48.club/llms.txt", "48 Club"),
    ("https://docs.4everland.org/llms.txt", "4EVERLAND"),
    ("https://docs.a2rev.com/llms.txt", "A2Reviews"),
    ("https://docs.abcproxy.com/llms.txt", "ABCProxy"),
    ("https://docs.abs.xyz/llms.txt", "Abstract"),
    ("https://docs.acrcloud.com/llms.txt", "ACRCloud"),
    ("https://docs.across.to/llms.txt", "Across"),
    ("https://docs.adly.tech/llms.txt", "Adly"),
    ("https://docs.admira.com/llms.txt", "Admira"),
    ("https://docs.adnuntius.com/llms.txt", "ADNUNTIUS"),
    ("https://docs.aethir.com/llms.txt", "Aethir"),
    ("https://docs.aevo.xyz/llms.txt", "Aevo"),
    ("https://docs.aftermath.finance/llms.txt", "Aftermath"),
    ("https://docs.agentlayer.xyz/llms.txt", "AgentLayer"),
    ("https://docs.akool.com/llms.txt", "AKOOL"),
    ("https://docs.alphagate.io/llms.txt", "Alphagate"),
    ("https://docs.alphaos.net/whitepaper/llms.txt", "Alpha Network"),
    ("https://docs.alva.xyz/llms.txt", "Alva"),
    ("https://docs.analog.one/documentation/llms.txt", "Analog"),
    ("https://docs.annoto.net/home/llms.txt", "Annoto"),
    ("https://docs.anytype.io/anytype-docs/llms.txt", "Anytype"),
    ("https://docs.apex.exchange/llms.txt", "ApeX Protocol"),
    ("https://docs.apify.com/llms.txt", "Apify"),
    ("https://gr-docs.aporia.com/llms.txt", "Aporia"),
    ("https://www.aptible.com/docs/llms.txt", "Aptible"),
    ("https://docs.arbiscan.io/llms.txt", "Arbiscan"),
    ("https://docs.arcade.software/kb/llms.txt", "Arcade"),
    ("https://docs.argil.ai/llms.txt", "Argil AI"),
    ("https://arpeggi.gitbook.io/faq/llms.txt", "Arpeggi"),
    ("https://docs.artzero.io/llms.txt", "ArtZero"),
    ("https://docs.asapp.com/llms.txt", "ASAPP"),
    ("https://docs.autentique.com.br/api/llms.txt", "Autentique"),
    ("https://docs.avaamo.com/user-guide/llms.txt", "Avaamo"),
    ("https://developers.avacloud.io/llms.txt", "AvaCloud"),
    ("https://docs.avada.io/seo-suite-help-center/llms.txt", "Avada SEO Suite"),
    ("https://docs.availspace.app/avail-space/llms.txt", "Avail Space"),
    ("https://docs.avalonfinance.xyz/llms.txt", "Avalon Labs"),
    ("https://docs.ave.ai/llms.txt", "Ave.ai"),
    ("https://docs.awesomeapi.com.br/llms.txt", "AwesomeAPI"),
    ("https://axiom.co/docs/llms.txt", "Axiom"),
    ("https://docs.axiom.trade/llms.txt", "Axiom Trade"),
    ("https://www.better-auth.com/llms.txt", "Better Auth"),
    ("https://bits-ui.com/llms.txt", "Bits UI"),
    ("https://blogv2.voiceflow.com/llms.txt", "Voiceflow"),
    ("https://booqable.com/llms.txt", "Booqable"),
    ("https://bun.sh/llms.txt", "Bun"),
    ("https://cal.com/docs/llms.txt", "Cal.com"),
    ("https://clerk.com/docs/llms.txt", "Clerk"),
    ("https://cloudfix.com/llms.txt", "CloudFix"),
    ("https://docs.replit.com/llms.txt", "Replit"),
    ("https://docs.replit.com/llms-full.txt", "Replit Full"),
    ("https://duckdb.org/duckdb-docs.md", "DuckDB"),
    ("https://himalayas.app/llms.txt", "Himalayas"),
    ("https://novilabs.com/llms.txt", "Novi Labs"),
    ("https://docs.stripe.com/llms.txt", "Stripe"),
    ("https://www.thenile.dev/docs/llms.txt", "Nile Postgres"),
    ("https://webrecorder.net/llms.txt", "Webrecorder"),
    ("https://www.wized.com/docs/llms.txt", "Wized"),
    ("https://docs.attest.com/llms.txt", "Attest"),
    ("https://blog.teraren.com/llms.txt", "Matsubo Tech Blog"),
    ("https://docs.remult.dev/llms.txt", "Remult"),
    ("https://www.prisma.io/docs/llms.txt", "Prisma"),
    ("https://www.meilisearch.com/llms.txt", "Meilisearch"),
    ("https://liveblocks.io/llms.txt", "Liveblocks"),
    ("https://docs.promptlayer.com/llms.txt", "PromptLayer"),
    ("https://docs.platform.sh/llms.txt", "Platform.sh"),
    ("https://docs.upsun.com/llms.txt", "Upsun"),
    ("https://superwall.com/docs/llms.txt", "Superwall"),
    ("https://transloadit.com/llms.txt", "Transloadit"),
    ("https://docs.moondream.ai/llms.txt", "Moondream"),
    ("https://docs.expo.dev/llms.txt", "Expo")
]

# Create directory if it doesn't exist
os.makedirs('/Users/ai/Github/Awesome-LLMS.txt/', exist_ok=True)

# Download each llms.txt file
total = len(urls)
for i, (url, title) in enumerate(urls, 1):
    print(f"\nProcessing {i}/{total}: Downloading {title} from {url}")
    success = download_llms_txt(url, title)
    # Add a small delay between requests to be nice to servers
    time.sleep(1)

print("\nDownload process completed!")