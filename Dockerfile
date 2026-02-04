# Use Python 3.11 Slim (Debian 12 based)
FROM python:3.11-slim

WORKDIR /app

# STEP 1: Install dependencies
# We install wget to download Chrome, and the common missing libraries
RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    curl \
    gnupg \
    unzip \
    libnss3 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    fonts-liberation \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# STEP 2: Install Chrome Directly (Bypasses 'apt-key' error)
# We download the official .deb file and let apt install it locally
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# STEP 3: Install Python libraries
RUN pip install --no-cache-dir selenium webdriver-manager beautifulsoup4 python-dotenv requests

# STEP 4: Copy your code and run
COPY Blitz.py .
COPY .env .
CMD ["python3", "-u", "Blitz.py"]