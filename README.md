# Blitz - Datablitz Price Monitoring System-

Monitor product prices and get instant Discord alerts when prices drop!

---

## Quick Start

Get up and running in 3 easy steps:

1. **[Install Dependencies](#installation)** 
2. **[Set Up Discord Webhook](#discord-webhook-setup)** 
3. **[Configure & Run](#configuration-and-usage)**

---

## Key Features

- **Automated Price Tracking** - Continuously monitors product pages
- **Discord Alerts** - Instant notifications with product details
- **Smart Caching** - Avoids duplicate alerts
- **Multi-URL Support** - Monitor multiple products simultaneously

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Internet connection
- A Discord server/channel

### Step 1: Clone the Repository

```bash
git clone https://github.com/yukirochi/Blitz.git
cd Blitz
```

### Step 2: Install Required Libraries

```bash
pip install requests beautifulsoup4
```

**What these do:**
- `requests` - Fetches web pages
- `beautifulsoup4` - Parses product data

---

## Discord Webhook Setup

Follow these steps to enable price alerts:

1. Open your Discord server
2. Go to the channel where you want alerts
3. Click the **Cog Icon** → **Integrations**
4. Select **Webhooks** → **New Webhook**
5. Copy the webhook URL

That's it! You now have your webhook URL.

---

## Configuration and Usage

### 1. Add Your Discord Webhook

Open `Blitz.py` and add your webhook URL to the configuration.

### 2. Add Products to Monitor

Add DataBlitz product URLs to your product list in the script.

### 3. Start Monitoring

```bash
python Blitz.py
```

Watch for alerts in your Discord channel!

---

## Coming Soon

We're building these features:

- **Multi-Store Support** - Monitor more retailers
- **Price History** - Track price trends over time
- **Dashboard** - Visual management interface
- **Telegram Support** - Get alerts on Telegram too

---

## Need Help?

Check the code comments or open an issue on GitHub!