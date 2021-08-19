from bs4 import BeautifulSoup
import requests
import smtplib
from product_data import my_products


MY_EMAIL = ''
MY_PASSWORD = ''
amazon_request_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.amazon.in',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Connection': 'keep-alive',
}

for product in my_products:
    amazon_response = requests.get(url=product['amazon_url'], headers=amazon_request_headers)
    print(amazon_response)

    soup = BeautifulSoup(amazon_response.text, 'html.parser')
    amazon_price = float(soup.find(name='span', id='priceblock_ourprice').getText().strip('₹').replace(',', ''))
    amazon_product_title = soup.find(name='span', id='productTitle').getText().strip('\n\t ')
    print(amazon_product_title, amazon_price)

    if amazon_price <= product['target_price']:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f'Subject:Amazon Low Price Alert: {product["product_name"]}\n\n'
                                    f'{amazon_product_title} is now available at a price of INR {amazon_price} only. Buy now!\n'
                                    f'{product["amazon_url"]}')
            print(f'Email sent for {product["product_name"]}')
