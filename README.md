# Blitz — Datablitz Product Price Monitor (step-by-step)

This project watches a DataBlitz product page and sends a Discord message only when the price changes. Follow the numbered steps below — no deep technical knowledge required.

What you need:
- A computer (Windows, macOS, or Linux).
- Either Docker installed (recommended) or Python 3.11 installed locally.
- A Discord server where you can create a webhook (instructions below).
- The DataBlitz product page URL you want to monitor.

Step-by-step guide
1. Create a Discord webhook (copy the URL)
	- Open Discord (app or browser).
	- Go to the server where you want alerts to appear.
	- Click the server name → Server Settings → Integrations → Webhooks.
	- Click "New Webhook", pick a channel and name, then click "Copy Webhook URL".

2. Put the webhook and product URL into a `.env` file
	- In the project folder, create a file named `.env` (plain text).
	- Add these two lines, replacing the placeholders:

```dotenv
webhook=PASTE_YOUR_WEBHOOK_URL_HERE
target_product_url=PASTE_DATA_BLITZ_PRODUCT_URL_HERE
```

3. Run the monitor (choose one option)

Option A — Recommended: Run with Docker (one command to start)

```bash
docker build -t blitz .
docker run --env-file .env --rm blitz
```

Option B — Run locally with Python (if you prefer not to use Docker)

```bash
pip install selenium webdriver-manager beautifulsoup4 python-dotenv requests
python Blitz.py
```

4. Stop the monitor
- If you ran with Docker: press Ctrl+C in the terminal or stop the container.
- If you ran `python Blitz.py`: press Ctrl+C in the terminal.

5. Quick notes and small edits
- The script checks the product regularly (default every 60 seconds). To change this, open [Blitz.py](Blitz.py) and edit the `time.sleep(60)` value to the number of seconds you prefer.
- The Docker option already includes Chrome and the browser driver, which avoids local browser setup.

Troubleshooting
- If you see errors about Chrome or the web driver when running locally, try the Docker option.
- If Discord messages do not arrive, double-check the webhook URL in your `.env` file and make sure the webhook's channel is visible and has permission to post.

Need help or a shorter checklist?
- Tell me which part you want shortened or if you want a printable one-page checklist.

