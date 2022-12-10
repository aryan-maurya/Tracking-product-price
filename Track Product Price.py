from bs4 import BeautifulSoup
import requests
import smtplib
import time


budget = float(input("Please Enter your budget : "))
print("If the price lies within your budget, you'll receive a mail regarding the same.")
print("Looking prices for Iphone 13(128 gb) ====>")


URL_amazon = "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/?_encoding=UTF8&pd_rd_w=hBBq9&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_r=ERXKK8HGMTRA8DPG566S&pd_rd_wg=YYx45&pd_rd_r=5a25cff4-5a6a-43e1-adb0-cbd73e726e93&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

URL_flipkart = "https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=19ac8a9d-2ee2-480f-88f4-5a51b8608624.MOBG6VF5Q82T3XRS.SEARCH&ppt=None&ppn=None&ssid=drhn91hxtc0000001670696770434&qH=c68a3b83214bb235"

URL_reliance = "https://www.reliancedigital.in/apple-iphone-13-128-gb-red/p/491997701"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
# searching my user-agent on browser: A user agent, or UA, is a string of information that identifies a user's browser and operating system.


def check_price_amazon():
    page = requests.get(URL_amazon, headers=headers)   # retrieves data from that website
    # print(page.content)

    soup = BeautifulSoup(page.content, 'html.parser')
    '''
    A parser is a program that is part of the compiler, and parsing is part of the compiling process. 
    Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor,
    broken into smaller pieces and analyzed so other software can understand it.
    '''

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()     # finding product using the title stored in source code and just using the text
    price = soup.find("span", attrs="a-price-whole").get_text()     # finding the price of the product (jump in the class)

    curr_price = price.replace(',', '')  # removing the comma in price
    curr_price = float(curr_price)        # converting the price in float type

    print("The current price on Amazon is : ₹", curr_price)

    if curr_price < budget:
        send_mail_amazon()



def check_price_flipkart():
    page = requests.get(URL_flipkart, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(attrs="B_NuCI").get_text()
    # print(title)

    price = soup.find(attrs="_30jeq3 _16Jk6d").get_text()

    curr_price = price.replace(',', '')
    curr_price = float(curr_price[1:])

    print("The current price on Flipkart is : ₹", curr_price)

    if curr_price < budget:
        send_mail_flipkart()



def check_price_reliance():
    page = requests.get(URL_reliance, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("span", attrs="pdp__offerPrice").get_text()

    curr_price = price.replace(',', '')
    curr_price = float(curr_price[1:])

    print("The current price on Reliance Digital is : ₹", curr_price)

    if curr_price < budget:
        send_mail_reliance()




def send_mail_amazon():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # the SMTP class is being used to connect to the SMTP server at smtp.gmail.com using port 587

    server.ehlo()
    server.starttls()   # upgrading to TLS connection
    server.ehlo()

    server.login("howyoudoing4271@gmail.com", "kxkucrdpmaoooovc")
    # logging in using a password created by two step authentication

    subject = "In your budget now!"

    body = "Here's the link --> https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/?_encoding=UTF8&pd_rd_w=hBBq9&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_r=ERXKK8HGMTRA8DPG566S&pd_rd_wg=YYx45&pd_rd_r=5a25cff4-5a6a-43e1-adb0-cbd73e726e93&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

    msg = f"Subject: {subject} \n \n {body}"    # creating email content

    server.sendmail('howyoudoing4271@gmail.com', 'aryanmaurya38@gmail.com', msg)    # from, to, content

    print('Mail has been sent.')

    server.quit()



def send_mail_flipkart():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # the SMTP class is being used to connect to the SMTP server at smtp.gmail.com using port 587

    server.ehlo()
    server.starttls()   # upgrading to TLS connection
    server.ehlo()

    server.login("howyoudoing4271@gmail.com", "kxkucrdpmaoooovc")
    # logging in using a password created by two step authentication

    subject = "In your budget now!\n"

    body = "Here's the link --> https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=19ac8a9d-2ee2-480f-88f4-5a51b8608624.MOBG6VF5Q82T3XRS.SEARCH&ppt=None&ppn=None&ssid=drhn91hxtc0000001670696770434&qH=c68a3b83214bb235"

    msg = f"Subject: {subject} \n \n {body}"    # creating email content

    server.sendmail('howyoudoing4271@gmail.com', 'aryanmaurya38@gmail.com', msg)    # from, to, content

    print('Mail has been sent.')

    server.quit()



def send_mail_reliance():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # the SMTP class is being used to connect to the SMTP server at smtp.gmail.com using port 587

    server.ehlo()
    server.starttls()   # upgrading to TLS connection
    server.ehlo()

    server.login("howyoudoing4271@gmail.com", "kxkucrdpmaoooovc")
    # logging in using a password created by two step authentication

    subject = "In your budget now!"

    body = "Here's the link --> https://www.reliancedigital.in/apple-iphone-13-128-gb-red/p/491997701"

    msg = f"Subject: {subject} \n \n {body}"    # creating email content

    server.sendmail('howyoudoing4271@gmail.com', 'aryanmaurya38@gmail.com', msg)    # from, to, content

    print('Mail has been sent.')

    server.quit()




while True:
    check_price_amazon()
    check_price_flipkart()
    check_price_reliance()
    time.sleep(2)
    print("Prices will be checked after every 3 hours.")
    time.sleep(10800)       # runs the function after every 3 hours

