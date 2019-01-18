#coding: utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

 
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


LOGIN_ID = 'nktkm06@icloud.com'
LOGIN_PASSWORD = 'tkm070601'

 
LOGIN_URL = 'https://www.amazon.co.jp/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&openid.pape.max_auth_age=0'
ITEM_URL = 'https://www.amazon.co.jp/APAGARD-%E3%82%A2%E3%83%91%E3%82%AC%E3%83%BC%E3%83%89-%E3%83%97%E3%83%AC%E3%83%9F%E3%82%AA-%E3%80%90%E5%8C%BB%E8%96%AC%E9%83%A8%E5%A4%96%E5%93%81%E3%80%91-100g/dp/B00NE7JU34/ref=pd_rhf_se_s_rp_1_3?_encoding=UTF8&pd_rd_i=B00NE7JU34&pd_rd_r=b802044e-3af7-4d55-bfe0-b6a4dee52ddd&pd_rd_w=T6ZpQ&pd_rd_wg=vvSs2&pf_rd_p=7dd29278-17ac-4caf-a462-ad2d5bd94274&pf_rd_r=MVDRQBHVNDGAYHA46V1E&psc=1&refRID=MVDRQBHVNDGAYHA46V1E'
#ITEM_URL = 'https://www.amazon.co.jp/%E4%BB%BB%E5%A4%A9%E5%A0%82-amiibo-%E3%82%AB%E3%83%BC%E3%83%93%E3%82%A3-%E5%A4%A7%E4%B9%B1%E9%97%98%E3%82%B9%E3%83%9E%E3%83%83%E3%82%B7%E3%83%A5%E3%83%96%E3%83%A9%E3%82%B6%E3%83%BC%E3%82%BA%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA/dp/B00O9GPD26/ref=sr_1_18?ie=UTF8&qid=1545978972&sr=8-18&keywords=%E3%82%A2%E3%83%9F%E3%83%BC%E3%83%9C'

#ITEM_URL = 'https://www.amazon.co.jp/Nintendo-Switch-%E3%83%9D%E3%82%B1%E3%83%83%E3%83%88%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC-%E3%83%94%E3%82%AB%E3%83%81%E3%83%A5%E3%82%A6%E3%82%BB%E3%83%83%E3%83%88-%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%AB/dp/B07HBZBSN4/ref=sr_1_5?ie=UTF8&qid=1545979861&sr=8-5&keywords=%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%80%80%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81'


ACCEPT_SHOP = 'Amazon'
LIMIT_VALUE = 1000



#import requests
#line_notify_token = 'o4UIG4GtDBvfUTkimCsMjtUsy3RgZGCJq9EzRmYK2cq'
#line_notify_api = 'https://notify-api.line.me/api/notify'
#message = 'amazonで買ったよ(^o^)\n'+ITEM_URL+'\n設定した限度額:¥'+str(LIMIT_VALUE)
#payload = {'message': message}
#headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
#line_notify = requests.post(line_notify_api, data=payload, headers=headers)



#options = Options()
# Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
#options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
#options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。
#b = webdriver.Chrome(chrome_options=options)



def l(str):
    print("%s : %s"%(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),str))
 
if __name__ == '__main__':

    #options = Options()
    # Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
    #options.binary_location = '/Applications/GoogleChromeCanary.app/Contents/MacOS/GoogleChromeCanary'
    # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
    #options.add_argument('--headless')
    # ChromeのWebDriverオブジェクトを作成する。
    #b = webdriver.Chrome(chrome_options=options,executable_path="./chromedriver")
 
    # ブラウザの起動
    try:
        b = webdriver.Chrome('./chromedriver')
        b.get(LOGIN_URL)
        b.find_element_by_id('ap_email').send_keys(LOGIN_ID)
        b.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
        b.find_element_by_id('signInSubmit').click()
        b.get(ITEM_URL)
        #b.find_element_by_class_name('a-size-mini').click()
    except:
        l('Failed to open browser.')
        exit()
 
    time.sleep(1)
    b.find_element_by_class_name('a-size-mini').click()
    while True:
        # 値段の確認
        p = b.find_element_by_id('priceblock_ourprice').text
        p = int(p.replace('￥ ','').replace(',',''))
        print (OKGREEN,'価格：¥',str(p),ENDC)
        #if int(p.split(' ')[1].replace(',', '')) > LIMIT_VALUE:
        #    l('PRICE IS TOO LARGE')
        #    time.sleep(10)
        #continue
        # カートに追加
        if p > LIMIT_VALUE:
            time.sleep(10)
            print('価格を監視中\n価格が条件を満たしていません')
            b.refresh()
            continue
        else:
            shop = b.find_element_by_id('merchant-info').text
            print('出品者情報を確認しました')
            #print(shop)
            shop1 = shop.split('この商品は、')[1].split(' が販売、発送します。')[0]
            #print(shop1)
            if shop1 == 'Amazon.co.jp':
                #time.sleep(2)
                break
            else:
                print('価格は条件を満たしています。出品者がAmazonでないです。')
                time.sleep(10)
                b.refresh()
    #b.find_element_by_class_name('a-size-mini').click()
    time.sleep(2)
    #b.find_element_by_id('one-click-button').click()
    print('oneクリックで購入しました')
    #b.find_element_by_id('hlb-ptc-btn-native').click()
    #print('レジへ進みました')
    #b.find_element_by_class_name('a-declarative').click()
    #print('住所を選択しました')
    #hantei = b.find_element_by_class_name('a-spacing-base').text
    #hantei = hantei.split('\n')[0]
    #print(hantei)
    #if hantei == '発送オプションと配送オプションを選んでください':
        #print(b.current_url)
        #b.find_element_by_class_name('a-button-text').click()
        #print('配送オプションを選択しました')
        #print(b.current_url)
        #time.sleep(3)
        #print(b.current_url)
        #button= b.find_element_by_id('continue-bottom').click()
        #print('支払い方法を選択しました')
    #else:
        #b.find_element_by_class_name('vertical-center-grid').click()
        #b.find_elements_by_css_selector('input[type="radio"]')[1].click()
        #b.find_element_by_xpath("//input[@type='radio']")[0].click()
        #b.find_element_by_id('continue-bottom').click()
        #print('支払い方法を選択しました')
        #b.find_element_by_class_name('a-button-text').click()
        #print('配送オプションを選択しました')

