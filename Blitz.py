from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import time
import requests
import os
#made by yukirochi

load_dotenv()

discord_Webhook = os.getenv('webhook')

if not discord_Webhook:
    raise ValueError("Discord webhook URL not found in environment variables.")

current_price = None

def discord(target,price, link=None):
    if not discord_Webhook:
        return
 
    data = {
        'content': f"**BLITZ**\n\nThe **{target}** is currently running **{price}**: {link}"
    }
    try:
        requests.post(discord_Webhook, json=data)
        print(f" -> Sent Discord alert for {target}")
    except Exception as e:
        print(f"Failed to send Discord alert: {e}")

def scrape(url, last_price):
   
    print(f"Checking...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = None   
    new_price = last_price
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fresh_price = soup.find('span', class_='price')
        price = soup.find('span', class_='price').text.strip().replace('₱', '').replace(',', '')
        name = soup.find('h1', class_='product-meta__title').text.strip()
        current_price = float(price)
        if float(price) != current_price:
            discord(name, current_price, url)
            print(f" -> Price changed to {new_price} for {name}")
            new_price = float(price)
        else:
            print(f"No change. Still {fresh_price.text.strip()}")
            new_price = last_price   

    except Exception as e:
        print(f"An exception occurred: {e}")

    finally:
        if driver:
            driver.quit()

    return new_price           
        

    
if __name__ == "__main__":
    url = os.getenv('target_product_url')
    if not url:
        raise ValueError("Target product URL not found in environment variables.")
    current_tracked_price = None 

    print("--- Monitoring Started (Press Ctrl+C to stop) ---")
    discord("Blitz", "✓ Monitoring started for the item.", url)
    try:
        while True:
            current_tracked_price = scrape(url, current_tracked_price)
            time.sleep(60)  # Wait for 1 minute
    except KeyboardInterrupt:
        print("\n--- Monitoring Stopped ---")
        discord("Blitz", "⏹️ Monitoring stopped.", url)
    except Exception as e:
        print(f"Error: {e}")
        discord("Blitz", f"❌ Error occurred: {e}", url)    