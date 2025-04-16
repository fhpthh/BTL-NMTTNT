import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from crawl_utils import scroll_page

def crawl_quan(quan, url):
    """Crawl dữ liệu nhà đất của một quận và lưu vào file CSV (không có tiêu đề)"""

    # Cấu hình trình duyệt
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    print(f"🔍 Đang crawl dữ liệu từ {quan}...")
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    data = []

    # Lấy số trang
    try:
        last_page = int(driver.find_element(By.XPATH, "//a[last()]").text.strip())
    except:
        last_page = 1

    for page in range(1, last_page + 1):
        print(f"📌 Trang {page}/{last_page}...")

        scroll_page(driver)

        listings = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 're__card-info')]")))

        for listing in listings:
            try:
                price = listing.find_element(By.XPATH, ".//span[contains(@class, 're__card-config-price')]").text.strip()
                area = listing.find_element(By.XPATH, ".//span[contains(@class, 're__card-config-area')]").text.strip()
                location = listing.find_element(By.XPATH, ".//div[@class='re__card-location']/span").text.strip()
                try:
                    room = listing.find_element(By.XPATH, ".//span[contains(@class, 're__card-config-bedroom')]/span").text.strip()
                except:
                    room = "N/A"

                data.append([price, area, location, room])
            except Exception as e:
                print("⚠️ Lỗi khi lấy dữ liệu:", e)
                continue

        if page < last_page:
            try:
                next_page = driver.find_element(By.XPATH, f"//a[text()='{page + 1}']")
                driver.execute_script("arguments[0].click();", next_page)
                time.sleep(3)
            except:
                print("⚠️ Không tìm thấy trang tiếp theo, dừng crawl.")
                break

    driver.quit()

    unique_data = list(set(tuple(row) for row in data))

    # Xóa file cũ nếu có
    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/{quan}.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"🗑️ Đã xóa file cũ: {file_path}")

    # Lưu CSV (không có cột Tiêu đề)
    df = pd.DataFrame(unique_data, columns=["Giá", "Diện tích", "Vị trí", "Phòng"])
    df.to_csv(file_path, index=False, encoding="utf-8")

    print(f"✅ Đã lưu dữ liệu từ {quan} vào {file_path}. Tổng số bài: {len(df)}")
