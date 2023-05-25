import requests 
from bs4 import BeautifulSoup
import time
import json
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
urls = open("urls.txt", "r").read().split("\n")

BASE_URL = os.environ.get("BASE_URL")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")

detail_products = []


def main():
    print("scraping....")
    insert_query = "INSERT IGNORE INTO drugs (title,image,product_url,description, indication, compotition, dose, how_to_use, attention, indication_contra, side_effect, product_class, package, manufactur, bpom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    ctx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD,
                              host=DB_HOST,
                              database=DB_DATABASE)

    cursor = ctx.cursor()

    start_time = time.time()

    for url in urls:
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        li_elements =soup.find_all("li", class_="custom-container__list__container__item")
        for li_element in li_elements:
            detail_product = li_element.find("a", class_="custom-container__list__container__item--link")
            detail_products.append(detail_product['href'])



    for detail in detail_products:
        get_detail_products = requests.get(BASE_URL + detail)
        bs = BeautifulSoup(get_detail_products.text, "html.parser")
        
        images = bs.find("img",class_="hd-base-image-mapper__img product-image")
        titles = bs.find("h1",class_="product-label")
        drug_details = bs.find_all("div", class_="drug-detail")
        detail_titles = bs.find_all("div", class_="ttl-list")

        detail_drug = {}
        for index in range(len(detail_titles)):
            detail_drug[detail_titles[index].text.lower().replace(".", "").replace(" ", "-")] = "-" if drug_details[index].find('div').text == "" else drug_details[index].find('div').text.replace("\n", "")
           
    
        values = ["-" if titles is None else titles.text, "-" if images is None else images["src"], BASE_URL + detail ,detail_drug.get('deskripsi', None), detail_drug.get('indikasi-umum', None), detail_drug.get('komposisi', None), detail_drug.get('dosis', None), detail_drug.get('aturan-pakai', None), detail_drug.get('perhatian', None), detail_drug.get('kontra-indikasi', None), detail_drug.get('efek-samping', None), detail_drug.get('golongan-produk', None), detail_drug.get('kemasan', None), detail_drug.get('manufaktur', None), detail_drug.get('no-registrasi', None)]

        cursor.execute(insert_query, values)


    ctx.commit()
    cursor.close()
    ctx.close()    


    print(f"execution time: {(time.time() - start_time)}" )
    time.sleep(1)
   

    return "done"

if __name__ == "__main__":
    main()

    