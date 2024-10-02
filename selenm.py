from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Set Chrome options (optional)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-extensions")  # Disable extensions

    # Initialize the WebDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("Navigating to Google...")
        driver.get('https://www.google.com')

        # Keep the browser open indefinitely until you manually close it
        print("Browser is now open. Close it manually to stop the script.")
        while True:
            time.sleep(1)  # Sleep for a while to keep the loop from using too much CPU

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()  # This will only run when you manually terminate the script

if __name__ == "__main__":
    main()
