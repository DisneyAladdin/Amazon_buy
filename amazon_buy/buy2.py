#coding: utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
UNDERLINE = '\033[4m'
import time
import sys
import random
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOGIN_ID = 'nktkm06@icloud.com'
LOGIN_PASSWORD = 'tkm070601'
LOGIN_URL = 'https://www.amazon.co.jp/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&openid.pape.max_auth_age=0'
ITEM_URL = input('自動購入したい商品のURLを貼ってください\n--->')
lim      = int(input('希望額を入力してください\n--->'))
confirm  = input('希望額は'+PURPLE+'¥'+str(lim)+ENDC+'でよろしいですね？(yes or no)\n--->')
if confirm == 'no':
	print ('プログラムをキャンセルしました')
	sys.exit()



def LINE_notify(ITEM_URL):
    line_notify_token = 'o4UIG4GtDBvfUTkimCsMjtUsy3RgZGCJq9EzRmYK2cq'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = 'amazonで自動購入しました\n商品URL↓\n'+ITEM_URL
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)










b = webdriver.Chrome('./chromedriver')
b.get(LOGIN_URL)
b.find_element_by_id('ap_email').send_keys(LOGIN_ID)
b.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
b.find_element_by_id('signInSubmit').click()
b.get(ITEM_URL)
time.sleep(1)
#one-click注文オン
#b.find_element_by_class_name('a-size-mini').click()
while True:
	#one-click注文オン
	#b.find_element_by_class_name('a-size-mini').click()
	# 値段
	p = b.find_element_by_id('priceblock_ourprice').text
	p = int(p.replace('￥ ','').replace(',',''))
	#ショップ
	shop = b.find_element_by_id('merchant-info').text
	shop = shop.split('この商品は、')[1].split(' が販売、発送します。')[0]
	shop = shop.replace('が販売し、Amazon.co.jp が発送します。','').replace('この出品商品にはコンビニ・ATM・ネットバンキング・電子マネー払いが利用できます。','').replace(' ギフトラッピングを利用できます。','')
	#商品名
	title = b.find_element_by_id('title').text
	print('========================================')
	print(PURPLE+'¥'+str(p)+ ENDC+' '+shop+ ' ' +UNDERLINE+OKBLUE+title+ENDC)
	print('========================================')
	#time.sleep(0.3)
	#print('*****')
	#time.sleep(0.3)
	#print('****')
	#time.sleep(0.3)
	#print('***')
	#time.sleep(0.3)
	#print('**')
	#time.sleep(0.3)
	#print('*')
	#print('***情報取得中***')
	#値段が希望額以下であり，かつ，ショップがAmazonである時のみ購入
	if p <=lim and shop == 'Amazon.co.jp':
		break
	else:
		b.refresh()
	time.sleep(random.uniform(3, 7))
	time.sleep(0.3)
	print('*****')
	time.sleep(0.3)
	print('****')
	time.sleep(0.3)
	print('***')
	time.sleep(0.3)
	print('**')
	time.sleep(0.3)
	print('*')
	#print('***情報取得中***')
		

#b.find_element_by_id('one-click-button').click()
print('商品を購入しました')
LINE_notify(ITEM_URL)
print('LINEにお知らせしました')
