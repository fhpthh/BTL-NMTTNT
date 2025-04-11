import time

def scroll_page(driver, max_scrolls=10, wait_time=2):
    """Cuộn trang để tải thêm dữ liệu, tối đa max_scrolls lần"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    scrolls = 0
    while scrolls < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scrolls += 1
