
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = '/usr/bin/chromium-browser'

driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)
driver.get('https://search.shopping.naver.com/search/all?query=다이소')
time.sleep(3)

items = driver.find_elements(By.CSS_SELECTOR, 'div.product_info_area__xxCTi > a')[:10]

results = []
for item in items:
    try:
        driver.execute_script("arguments[0].click();", item)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        real_url = driver.current_url
        name = driver.title
        results.append({'상품명': name, 'URL': real_url})
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        continue

driver.quit()
df = pd.DataFrame(results)
df.to_excel('daiso_real_urls.xlsx', index=False)
