
import time
import random
from faker import Faker
from pathlib import Path
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

fake = Faker()

def human_type(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.15))

def generate_user():
    first = fake.first_name()
    last = fake.last_name()
    username = f"{first.lower()}{last.lower()}{random.randint(1000,9999)}"
    password = fake.password(length=12)
    return first, last, username, password

def load_proxies(filename="proxies.txt"):
    path = Path(filename)
    if path.exists():
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    return []

def create_gmail_account(proxy=None):
    first, last, username, password = generate_user()
    print(f"Creating: {first} {last} | {username} | {password}")

    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={fake.user_agent()}")

    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    driver = uc.Chrome(options=options)
    driver.get("https://accounts.google.com/signup")
    time.sleep(3)

    human_type(driver.find_element(By.ID, "firstName"), first)
    human_type(driver.find_element(By.ID, "lastName"), last)
    human_type(driver.find_element(By.ID, "username"), username)
    human_type(driver.find_element(By.NAME, "Passwd"), password)
    human_type(driver.find_element(By.NAME, "ConfirmPasswd"), password)

    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    time.sleep(10)

    # Save login
    with open("gmail_created.txt", "a") as f:
        f.write(f"{username}@gmail.com|{password}\n")

    print("🛑 Waiting at phone verification screen. Proceed manually if needed.")
    time.sleep(60)  # Pause for manual interaction
    driver.quit()

def main():
    num = int(input("How many Gmail accounts to create? "))
    proxies = load_proxies()
    for i in range(num):
        proxy = proxies[i % len(proxies)] if proxies else None
        create_gmail_account(proxy)

if __name__ == "__main__":
    main()
