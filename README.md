# Blitz — Price Monitor

Monitor product prices across multiple e-commerce stores and get instant Discord notifications when prices change.

## Supported Stores

Blitz works with the following e-commerce sites:
- **DataBlitz** (datablitz.com)
- **GameXtreme** (gamextreme.com.ph)
- **EasyPC** (easypc.com.ph)
- **Amazon** (amazon.com)

Simply use a product URL from any of these stores, and Blitz will automatically detect which site you're using.

## What You Need

Before starting, make sure you have:
- A computer (Windows, macOS, or Linux)
- Either **Docker** (recommended) or **Python 3.11** installed locally
- A Discord server where you can create a webhook
- The product URL from one of the supported stores

## Setup Instructions
### Step 1: Create a Discord Webhook

1. Open Discord (app or browser)
2. Go to the server where you want price alerts to appear
3. Click the server name → **Server Settings** → **Integrations** → **Webhooks**
4. Click **"New Webhook"**, choose a channel, name it, then click **"Copy Webhook URL"**

### Step 2: Create a `.env` File

1. In the project folder, create a new file named `.env` (plain text)
2. Add these two lines, replacing the placeholders with your actual values:

```dotenv
webhook=PASTE_YOUR_WEBHOOK_URL_HERE
target_product_url=PASTE_PRODUCT_URL_HERE
```

The product URL can be from DataBlitz, GameXtreme, EasyPC, or Amazon.

### Step 3: Run the Monitor

#### Option A: Using Docker (Recommended)

```bash
docker build -t blitz .
docker run --env-file .env --rm blitz
```

This is the easiest option. Docker handles all dependencies and browser setup automatically.

#### Option B: Using Python Locally

If you prefer not to use Docker, install the required packages first:

```bash
pip install selenium webdriver-manager beautifulsoup4 python-dotenv requests
python Blitz.py
```

### Step 4: Monitor the Prices

The script will now check the product price every 60 seconds and send a Discord message whenever it changes. You'll see output in your terminal showing each check.

### Step 5: Stop the Monitor

Press **Ctrl+C** in your terminal to stop monitoring.

## Customization

**Change the check interval:** The script checks the price every 60 seconds by default. To change this, open [Blitz.py](Blitz.py) and find the line `time.sleep(60)` near the end of the file. Replace `60` with the number of seconds you prefer.

## Troubleshooting

**Chrome or WebDriver errors when running locally?**
- Try using Docker instead (Option A) — it includes everything needed.

**Discord messages not arriving?**
- Double-check your webhook URL in the `.env` file
- Make sure the webhook's Discord channel is visible and has permission to receive messages
- Verify the `.env` file is in the project folder (same location as `Blitz.py`)

**Can't get it working?**
- Try the Docker option first
- Make sure your product URL is from one of the supported stores (DataBlitz, GameXtreme, EasyPC, Amazon)

