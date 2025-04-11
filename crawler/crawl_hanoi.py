from crawl_quan import crawl_quan

# Danh sách các quận cần crawl và URL tương ứng
quan_urls = {
    "ha_dong": "https://batdongsan.com.vn/ban-nha-rieng-ha-dong",
    "thanh_xuan": "https://batdongsan.com.vn/ban-nha-rieng-thanh-xuan",
    "cau_giay": "https://batdongsan.com.vn/ban-nha-rieng-cau-giay",
    "tay_ho": "https://batdongsan.com.vn/ban-nha-rieng-tay-ho",
    "bac_tu_liem": "https://batdongsan.com.vn/ban-nha-rieng-bac-tu-liem",
    "ba_dinh": "https://batdongsan.com.vn/ban-nha-rieng-ba-dinh",
    "hai_ba_trung": "https://batdongsan.com.vn/ban-nha-rieng-hai-ba-trung",
    "nam_tu_liem":"https://batdongsan.com.vn/ban-nha-rieng-nam-tu-liem",
    "dong_da": "https://batdongsan.com.vn/ban-nha-rieng-dong-da",
    "hoan_kiem": "https://batdongsan.com.vn/ban-nha-rieng-hoan-kiem",
    "hoang_mai":"https://batdongsan.com.vn/ban-nha-rieng-hoang-mai",
    "long_bien":"https://batdongsan.com.vn/ban-nha-rieng-long-bien",
    "ba_vi":"https://batdongsan.com.vn/ban-nha-rieng-ba-vi",
    "chuong_my":"https://batdongsan.com.vn/ban-nha-rieng-chuong-my",
    "dong_anh":"https://batdongsan.com.vn/ban-nha-rieng-dong-anh",
    "hoai_duc":"https://batdongsan.com.vn/ban-nha-rieng-hoai-duc",
    "quoc-oai":"https://batdongsan.com.vn/ban-nha-rieng-quoc-oai",
    "thuong-tin":"https://batdongsan.com.vn/ban-nha-rieng-thuong-tin",
    "me_linh":"https://batdongsan.com.vn/ban-nha-rieng-me-linh",
    "dan_phuong":"https://batdongsan.com.vn/ban-nha-rieng-dan-phuong",
    "gia_lam":"https://batdongsan.com.vn/ban-nha-rieng-gia-lam",
    "phuc_tho": "https://batdongsan.com.vn/ban-nha-rieng-phuc-tho",
    "ung_hoa": "https://batdongsan.com.vn/ban-nha-rieng-ung-hoa",
    "son_tay": "https://batdongsan.com.vn/ban-nha-rieng-son-tay",
    "phu_xuyen": "https://batdongsan.com.vn/ban-nha-rieng-phu-xuyen",
    "thanh_tri": "https://batdongsan.com.vn/ban-nha-rieng-thanh-tri",
    "thanh_oai": "https://batdongsan.com.vn/ban-nha-rieng-thanh-oai",
    "my_duc": "https://batdongsan.com.vn/ban-nha-rieng-my-duc",
    "thach_that": "https://batdongsan.com.vn/ban-nha-rieng-thach-that",

}

if __name__ == "__main__":
    for quan, url in quan_urls.items():
        crawl_quan(quan, url)
