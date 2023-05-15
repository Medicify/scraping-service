import requests 
from bs4 import BeautifulSoup
import time
import json

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
                "deskripsi": detail_drug.get('deskripsi', None),
                "indikasi-umum": detail_drug.get('indikasi-umum', None),
                "komposisi": detail_drug.get('komposisi', None),
                "dosis":  detail_drug.get('dosis', None),
                "aturan-pakai": detail_drug.get('aturan-pakai', None),
                "perhatian":  detail_drug.get('perhatian', None),
                "kontra-indikasi": detail_drug.get('kontra-indikasi', None),
                "efek-samping": detail_drug.get('efek-samping', None),
                "golongan-produk": detail_drug.get('golongan-produk', None),
                "kemasan": detail_drug.get('kemasan', None),
                "manufaktur": detail_drug.get('manufaktur', None),
                "no-registrasi": detail_drug.get('no-registrasi', None)
            })




    json_data = json.dumps(drugs, indent=4,ensure_ascii=True)
    with open("drugs.json", 'w') as json_file:
        json_file.write(json_data)

    print(f"execution time: {(time.time() - start_time)}" )
    time.sleep(1)
   

    return "done"

if __name__ == "__main__":
    main()

    