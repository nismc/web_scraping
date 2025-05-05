from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# this makes it possible for Selenium to access and interact with keys like enter and backspace
import time

user_input = input("Enter movie title:")
movies = user_input
driver = webdriver.Chrome()

driver.get("https://www.imdb.com")
try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(movies)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    first_result = driver.find_element(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")
    title = first_result.find_element(By.TAG_NAME, "a").text
    year = first_result.find_element(
        By.CSS_SELECTOR,
        ".ipc-metadata-list-summary-item__li"
    ).text

    print(f"{title} ({year})")

except Exception as e:
    print(f"Error retrieving info for '{movie}': {e}")

driver.quit()