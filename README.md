# Blitz - Datablitz Price Monitoring System-

Monitor product prices and get instant Discord alerts when prices drop!

---

## Quick Start

Get up and running with Docker:

1. **[Set Up Discord Webhook](#discord-webhook-setup)** 
2. **[Build & Run with Docker](#docker-setup)**

---

## Key Features

- **Automated Price Tracking** - Continuously monitors product pages
- **Discord Alerts** - Instant notifications with product details
- **Smart Caching** - Avoids duplicate alerts
- **Multi-URL Support** - Monitor multiple products simultaneously

---

## Docker Setup

### Prerequisites

- Docker installed on your system
- A Discord server/channel
- Internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/yukirochi/Blitz.git
cd Blitz
```

### Step 2: Build the Docker Image

```bash
docker build -t blitz .
```

This Dockerfile:
- Uses Python 3.11 Slim as the base image
- Installs Chrome browser and all required dependencies
- Installs Python packages: `selenium`, `webdriver-manager`, `beautifulsoup4`, `python-dotenv`, `requests`
- Copies your code and sets up the container to run Blitz

### Step 3: Run the Docker Container

```bash
docker run --rm blitz
```

You'll be prompted to enter your Discord webhook URL when the container starts.


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

### 1. Set Up Your Discord Webhook

Follow the [Discord Webhook Setup](#discord-webhook-setup) section below to get your webhook URL.

### 2. Add Products to Monitor

Edit `Blitz.py` and add DataBlitz product URLs to your product list in the script.

### 3. Run the Application

**Using Docker (Recommended):**
```bash
docker run --rm blitz
```

**Using Python directly:**
```bash
python Blitz.py
```

When prompted, enter your Discord webhook URL and the application will start monitoring!

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