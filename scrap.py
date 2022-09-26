import requests
from bs4 import BeautifulSoup
import pandas as pd

product_url_arr = []
product_name_arr = []
product_price_arr = []
rating_arr = []
number_of_reviews_arr = []

page_num = input("Number of page")

for i in range(1,int(page_num)+1):
    headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'personal@domain.com'  # This is another valid field
}
    url="https://www.amazon.in/s?k=bags&page="+str(i)+"&crid=2M096C61O4MLT&qid=1664118716&sprefix=ba%2Caps%2C283&ref=sr_pg_"+str(i)
    req = requests.get(url,headers=headers)
    content = BeautifulSoup(req.content,'html.parser')
    # print(content)
    product_url = content.find_all('a',{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
    product_name = content.find_all('span',{"class":"a-size-medium a-color-base a-text-normal"})
    product_price = content.find_all('span',{"class":"a-price-whole"})
    rating = content.find_all('span',{"class":"a-icon-alt"})
    number_of_reviews = content.find_all('span',{"class":"a-size-base s-underline-text"})
    # print(product_price)

    for i in product_url:
        product_url_arr.append("https://www.amazon.in"+i.get('href'))
    
    for i in product_name:
        product_name_arr.append(i.text)
    
    for i in product_price:
        product_price_arr.append(i.text)

    for i in rating:
        rating_arr.append(i.text)

    for i in number_of_reviews:
        number_of_reviews_arr.append(i.text)
    
    if(len(product_name_arr)>200):
        break
    
    data ={"Product Name":product_name_arr,"Product URL":product_url_arr,"Product Price":product_price_arr,"Product Raiting":rating_arr,"Product Reveiw":number_of_reviews_arr}
    df = pd.DataFrame.from_dict(data,orient='index')
    final_data = df.transpose()
    final_data.to_csv('abdullah_amazon.csv')
