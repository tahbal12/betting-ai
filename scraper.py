import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-data-dir=/tmp/temp-profile')

# Launch browser
driver = webdriver.Chrome(options=options)
driver.get('https://www.888sport.com/betting')

# Accept cookie banner if it appears
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    ).click()
    print("Cookies accepted.")
except:
    print("No cookie banner found.")

print("Waiting for page to load...")
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'event-title'))
    )
    time.sleep(3)
except:
    print("Timeout waiting for games to load.")

# Screenshot for debugging
driver.save_screenshot('page.png')
print("Screenshot saved as page.png")

# Scrape data
games = driver.find_elements(By.CLASS_NAME, 'event-title')[:5]
odds = driver.find_elements(By.CLASS_NAME, 'outcome-price')[:5]
print(f'Found {len(games)} games and {len(odds)} odds')

# Save to CSV
with open('betting_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Game', 'Odds'])  # Header
    for i in range(min(len(games), len(odds))):
        game = games[i].text
        odd = odds[i].text
        writer.writerow([game, odd])
        print(f'{game} @ {odd}')

print("Data saved to betting_data.csv")

# Close browser
driver.quit()from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-data-dir=/tmp/temp-profile')

driver = webdriver.Chrome(options=options)
driver.get('https://www.888sport.com/betting')

# Accept cookie banner if it appears
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    ).click()
    print("Cookies accepted.")
except:
    print("No cookie banner found.")

print('Waiting for page to load...')
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'event-title'))
    )
    time.sleep(3)
except:
    print('Timeout waiting for games to load.')

# Screenshot for debugging
driver.save_screenshot('page.png')
print("Screenshot saved as page.png")

games = driver.find_elements(By.CLASS_NAME, 'event-title')[:5]
odds = driver.find_elements(By.CLASS_NAME, 'outcome-price')[:5]

print(f'Found {len(games)} games and {len(odds)} odds')

for i in range(min(len(games), len(odds))):
    print(f'{games[i].text} @ {odds[i].text}')

driver.quit()
