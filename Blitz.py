from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        'content': f"**BLITZ**\n\nThe **{target}** **{price}**: {link}"
    }
    try:
        requests.post(discord_Webhook, json=data)
        print(f" -> Sent Discord alert for {target}")
    except Exception as e:
        print(f"Failed to send Discord alert: {e}")
        
def price_update_notification(name, price, url):
    if not discord_Webhook:
        return
    
    content = f"**PRICE CHANGE ALERT**\n\nThe price of **{name}** has changed to **{price}**: {url}"
    
    try:
        requests.post(discord_Webhook, json={'content': content})
        print(f" -> Sent price update notification for {name}")
    except Exception as e:
        print(f"Failed to send price update notification: {e}")

def scrape(url, last_price,name_element=None, price_element=None, price_class='price', name_class='product-meta__title'):
   
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

        wait = WebDriverWait(driver, 10)
        price_element_present = EC.presence_of_element_located((By.CLASS_NAME, price_class))
        wait.until(price_element_present)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fresh_price = soup.find(price_element, class_=price_class)
        price = soup.find(price_element, class_=price_class).text.strip().replace('₱', '').replace(',', '')
        name = soup.find(name_element, class_=name_class).text.strip()
        current_price = float(price)

        if float(price) != current_price :
            price_update_notification(name, price, url)
            print(f" -> Price changed to {new_price} for {name}")
            new_price = float(price)
        else:
            print(f"No change. Still {current_price} for {name}")
            new_price = last_price   

    except Exception as e:
        print(f"An exception occurred: {e}")

    finally:
        if driver:
            driver.quit()

    return new_price           


        

    
if __name__ == "__main__":
    site_list =  {
        'datablitz': {
            'name_element': 'h1',
            'price_element': 'span',
            'price_class': 'price',
            'name_class': 'product-meta__title'
        },
        'gamextreme': {
            'name_element': 'h1',
            'price_element': 'span',
            'price_class': 'price-item',
            'name_class': 'product-title'
        },
        'easypc': {
            'name_element': 'h1',
            'price_element': 'span',
            'price_class': 'price',
            'name_class': 'page-heading'
        },
        'amazon': {
            'name_element': 'span',
            'price_element': 'span',
            'price_class': 'a-price-whole',
            'name_class': 'a-size-large product-title-word-break'
        }
        
    }
    url = os.getenv('target_product_url')
    site = None
    extractsite = url.split('/')[2].lower()
    if 'datablitz' in extractsite:
        site = site_list['datablitz']
    elif 'gamextreme' in extractsite:
        site = site_list['gamextreme']
    elif 'easypc' in extractsite:
        site = site_list['easypc']
    elif 'amazon' in extractsite:
        site = site_list['amazon']
    else:
        raise ValueError("Unsupported site. Please use a supported e-commerce site.")
    

    if not url:
        raise ValueError("Target product URL not found in environment variables.")
    current_tracked_price = None 

    print("--- Monitoring Started (Press Ctrl+C to stop) ---")
    discord("Blitz", "✓ Monitoring started for the item.", url)
    try:
        while True:
            current_tracked_price = scrape(
                url,
                current_tracked_price,
                name_element=site['name_element'],
                price_element=site['price_element'],
                price_class=site['price_class'],
                name_class=site['name_class']
            )

            time.sleep(60)  # Wait for 1 minute
    except KeyboardInterrupt:
        print("\n--- Monitoring Stopped ---")
        discord("Blitz", "⏹️ Monitoring stopped.", url)
    except Exception as e:
        print(f"Error: {e}")
        discord("Blitz", f"❌ Error occurred: {e}", url)    