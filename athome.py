 #! /usr/bin/ python
# -*- coding: utf-8 -*-
# PythonでSeleniumのwebdriverモジュールをインポート
# mainはgoogleでクローリングするテストプログラム
import selenium as selc


if __name__ == '__main__':
    driver_dir = './chromedriver'
    sel = selc.SeleniumClass(driver_dir)
    
    sel.Help()
    
    sel.TimeSetting(3,7)

    #アクセス開始
    sel.AccessUrl("https://www.athome.co.jp/chintai/")

    #スクロール
    sel.ScreenScroll(0.05)
    
    btn = sel.SearchSet("id","area-hokkaido")
    btn.click()
    btn = sel.SearchSet("id","search-type-area-btn")
    btn.click()
    
    #スクロール
    sel.ScreenScroll(0.05)

    cbox = sel.SearchSet("id","sapporo_chuo")
    cbox.click()
    sel.ScreenScroll(0.4)
    btn = sel.SearchSet("class_name","viewResult ir-bt_view_result")
    btn.click()

    sleep(4)


    sel.Quit(0)
