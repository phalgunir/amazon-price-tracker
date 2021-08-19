Track the price of Amazon products and get an alert if it falls below your target price.

This project helps to keep track of the prices of products you want to buy on Amazon.   
Update the product_data.py file with the name for your product, the amazon URL for that product and your target price below which you are willing to buy it.

For each entry in the list, the program fetches the current price on Amazon for it by scraping the website using BeautifulSoup module.      
If the current amazon price is lesser than the user set target price, then the user is sent an email alert, using SMTPLib module, with the product Name, price and link to purchase it.

One can schedule to run this program every morning using PythonAnywhere to find the best deal price on Amazon.