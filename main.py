import requests 
from bs4 import BeautifulSoup
import time
import json
import mysql.connector

urls = open("urls.txt", "r").read().split("\n")

BASE_URL = "https://www.halodoc.com/obat-dan-vitamin"

detail_products = []
drugs = []


def main():
    print("scraping....")
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
           

        
        drugs.append({
            "product_url" : BASE_URL + detail,
            "image" : "-" if images is None else images["src"] , 
            "title" : "-" if titles is None else titles.text,
            "detail" : detail_drug
        })
       

    # Todo SQL
    ctx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='drug_capstone')

    insert_query = "INSERT IGNORE INTO drugs (title,image,product_url,description, indication, compotition, dose, how_to_use, attention, indication_contra, side_effect, product_class, package, manufactur, bpom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = ctx.cursor()


    # cursor.execute("truncate drugs")


    batch_size=5
    for i in range(0, len(drugs), batch_size):
        batch = drugs[i:i+batch_size]
        values = [(row.get("title", None),row.get("image", None), row.get("product_url", None),row["detail"].get('deskripsi', None), row["detail"].get('indikasi-umum', None), row["detail"].get('komposisi', None), row["detail"].get('dosis', None), row["detail"].get('aturan-pakai', None), row["detail"].get('perhatian', None), row["detail"].get('kontra-indikasi', None), row["detail"].get('efek-samping', None), row["detail"].get('golongan-produk', None), row["detail"].get('kemasan', None), row["detail"].get('manufaktur', None), row["detail"].get('no-registrasi', None)) for row in batch]

        cursor.executemany(insert_query, values)


    ctx.commit()

    # Close the cursor and connection
    cursor.close()
    ctx.close()    


    print(f"execution time: {(time.time() - start_time)}" )
    time.sleep(1)

    # ToDo SQL
    json_data = json.dumps({"total_data" : len(drugs), "drugs" : drugs}, indent=4,ensure_ascii=True)
    

    with open("drugs.json", 'w') as json_file:
        json_file.write(json_data)



    print(f'total data scrape: {len(drugs)}')

if __name__ == "__main__":
    main()

    