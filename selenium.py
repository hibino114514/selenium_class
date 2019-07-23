 #! /usr/bin/ python
# -*- coding: utf-8 -*-
# PythonでSeleniumのwebdriverモジュールをインポート
# mainはgoogleでクローリングするテストプログラム
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from time import sleep
import random
import math

class SeleniumClass:
    
    def __init__(self,driver_dir,filename=None):
        self.driver_dir = driver_dir
        self.driver  = webdriver.Chrome(driver_dir)
        self.options = webdriver.ChromeOptions()
        #Cookieを削除
        self.driver.delete_all_cookies()
        #UAを設定
        #chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1')
        #初期設定
        self.time_s = 1
        self.time_e = 5



    def Help(self):
        print "***********[Help]**********"
        print " "
        print "driver ReturnDriver()"
        print "　ドライバをreturnする"
        print " "
        print "str AccessUrl(url)"
        print "　指定されたURLにアクセスし、アクセス先のURLをreturnする"
        print " "
        print "str Back_Forword_Page(str) ... 1.\"back\"or\"forword\""
        print "　一つ前か先のページに遷移し、アクセス先のURLをreturnする"
        print " "
        print "element SearchSet(str,str) ... 1.\"id\"or\"xpath\"or\"name\"or\"class_name\", 2.[search_word]"
        print "　HTMLの中から、指定された要素と一致する項目を検索し、そのelementをreturnする"
        print " "
        print " str AlartPass(str,str) ... 1.\"dialog\"or\"basic\", 2.imput_word"
        print "　アラートダイアログへの対応(YESNOの押下)、BASIC認証の突破を行う"
        print " "
        print "str RefreshPage()"
        print "　ページを再読み込みし、アクセス先のURLをreturnする"
        print " "
        print "str GetSource()"
        print "　ページのソースを取得して、その値をreturnする"
        print " "
        print "None MaximumWindow()"
        print "　ウィンドウを最大化する"
        print " "
        print "None Quit(int) ... 1.0 or else_num"
        print "　全セッションを終了する。0以外の引数を入れるとそのページだけを閉じる。"
        print " "
        print "None TimeSetting(int,int) ... 1.rand_min_time, 2.rand_max_time"
        print "　ランダムに決定するアクセス時間を調整する。"
        print " "
        print "***************************"



    def HelpElement(self):
        print "***********[Help]**********"
        print " "
        print "・制御"
        print "element.send_keys([word])　テキストを入力する"
        print "element.text             　テキストを取得する"
        print "element.get_attribute    　属性値を取得する"
        print "element.cloar()          　テキストをクリアする"
        print "element.click()          　クリックする"
        print " "
        print "・選択"
        print "Select(element).select_by_value([value])         value属性を選択"
        print "Select(element).select_by_index([index])         indexを選択"
        print "Select(element).select_by_visible_text([str])    テキストを選択"
        print "選択解除は select → deselect　あるは　.deselect_all()"
        print " "
        print "***************************"



    def ReturnDriver(self):
        return self.driver
    

    def MaximumWindow(self):
        self.options.add_argument('--kiosk')
        self.driver = webdriver.Chrome(self.driver_dir,chrome_options=options)
    
    
    

    #JAVAScriptを使ってゆっくりスクロールを実行
    def ScreenScroll(self,height_target):
        height = self.driver.execute_script("return document.body.scrollHeight")
        height_t = height * height_target
        #ループ処理で少しづつ移動
        for x in range(1,int(height_t)):
            y = -2.0 ** 1.0*(float(height_t-x)/height_t*3-3)+random.uniform(-0.05,0.05)#ランダム性を付与
            self.driver.execute_script("window.scrollTo(0, "+str(x)+");")
            #print y/2000.0
            sleep(math.fabs(y/2000.0))
            
            
            
    def AlartPass(self,type,word):
        if type=="dialog":
            if word=="y" or word=="yes":
                Alart(self.driver).accept()
            else:
                Alart(self.driver).dismiss()
        elif type=="basic":
            #print "URL例:http://username:password@hogehoge.com"
            #print "input:",word
            driver.get(word)


    def AccessUrl(self,url):
        self.driver.get(url)
        self.TimeSleep()
        return self.driver.current_url


    def Back_Forword_Page(self,b_or_f=None):
        if b_or_f is None:
            print "Please input back or forword"
            return
        if b_or_f=="b" or b_or_f=="back":
            self.driver.back()
        if b_or_f=="f" or b_or_f=="forword":
            self.driver.forward()
        self.TimeSleep()
        return self.driver.current_url

    def SearchSet(self,Find=None,Type=None):
        if Find is None or Type is None:
            print "Can't Find."
            return
        if Find=="id":
            text = self.driver.find_element_by_id(Type)
        elif Find=="xpath":
            text = self.driver.find_element_by_xpath(Type)
        elif Find=="name":
            text = self.driver.find_element_by_name(Type)
        elif Find=="class_name" or "classname":
            text = self.driver.find_element_by_class_name(Type)
        elif Find=="css_selector":
            text = self.driver.find_element_by_css_selector(Type)
        elif Find=="partial_link_text":#部分一致
            text = self.driver.find_element_by_partial_link_text(Type)
        elif Find=="link_text":#完全一致
            text = self.driver.find_element_by_link_text(Type)
        else:
            print "Can't find Element."
        self.TimeSleep()
        return text

    def RefreshPage(self):
        self.driver.refresh()
        self.TimeSleep()
        return self.driver.current_url

    def GetSource(self):
        return self.driver.page_source


    def Quit(self,num=0):
        if num==0:
            self.driver.quit()
        else:
            self.driver.close()

    #BAN回避用
    def TimeSleep(self):
        if self.time_e==self.time_s:
            num = self.time_s
        else:
            num = random.randint(self.time_s,self.time_e)
        sleep(num)


    def TimeSetting(self,s,e):
        self.time_s = s
        self.time_e = e




if __name__ == '__main__':
    driver_dir = './chromedriver'
    sel = SeleniumClass(driver_dir)
    
    sel.Help()
    
    sel.TimeSetting(2,2)
    
    chrome_options = Options()
    #JSを無効にする→無効にすると検索画面で、チェックボックス入れても0件になる
    #chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})

    #アクセス開始
    sel.AccessUrl("https://www.google.com/?hl=ja")

    #検索ボックスに文字を入力
    txtbox = sel.SearchSet("name","q")
    txtbox.send_keys("google")
    #検索ボタンを押す
    btn = sel.SearchSet("name","btnK")
    btn.click()
    
    #スクロール
    sel.ScreenScroll(0.5)
    #移動する
    sel.Back_Forword_Page("b")
    sel.Back_Forword_Page("f")
    


    
    sel.Quit(0)
