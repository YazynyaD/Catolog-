import array as arr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import importlib.util
import sys
import os
import pandas as pd
from openpyxl import *
import xlsxwriter 
import xlrd
# then import foo
# from ...main import *
# import curl from .../main.py
# from .. import 
def goo(brow,z,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    br=brow
    brow.execute_script("window.open('');")
    brow.switch_to.window(brow.window_handles[z])
    с=ct1(br,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
def ct1(brow,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    wwww=notwww.split("\n")
    cit=city
    for q in wwww:
        if "компаниирф.рф" in q or "2" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"https://xn--80aqafkhejn4b.xn--p1ai/%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[3]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /компаниирф.рф")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[1]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[2]/option[contains(text(),'{city}')]").click()
        
    
    
    except Exception:
        print("Ошибка: xp /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[4]/div/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[5]/div/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[6]/div[2]/div[1]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /компаниирф.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[7]/div/div[1]/div[1]/div/select[1]/option[6]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[7]/div/div[1]/div[1]/div/select[2]/option[36]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[1]/div[7]/div/div[1]/div[1]/input").click()
    
    except Exception:
        print("Ошибка: категории /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[1]/div[8]/div/div[1]/div")
        zz.clear()
        zz.send_keys(keysl)
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: keysl /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[2]/div/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[4]/div/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[2]/div[5]/div/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[1]/div/input")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[3]/div[2]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[4]/div/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys("00:00")
    except Exception:
        print("Ошибка: timework /компаниирф.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /компаниирф.рф")
        pass
    # try:
    #     zz=brow.find_element(By.XPATH,"//*[@id="select_logo"]")
    #     zz.send_keys(os.getcwd()+"/001.jpg")

    # except Exception:
    #     print("Ошибка: img /компаниирф.рф")
    #     pass
    
    sleep(2)
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/fieldset/div/div[2]/div[2]/input").click()
    except Exception:
        print("Ошибка: правила /компаниирф.рф")
        pass
    sleep(1)
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/form/div[6]/input").click()
    except Exception:
        print("Ошибка: Готово1 /компаниирф.рф")
        pass
    sleep(5)
    # try:
    #     brow.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/a").click()
    # except Exception:
    #     print("Ошибка: Готово2 /компаниирф.рф")
    #     pass
    try:
        brow.get(url="https://компаниирф.рф/%D0%BA%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82/%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8")
    except Exception:
        print("Ошибка: Готово2 /компаниирф.рф")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/table/tbody/tr/td[1]/span/a").click()
    except Exception:
        print("Ошибка: Готово1 /компаниирф.рф")
        pass
    try:
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/table/tbody/tr/td[1]/span/a").click()
        
    except Exception:
        print("Ошибка: Готово1 /компаниирф.рф")
        pass
    try:
        sleep(5)
        
        curl=brow.current_url
        print(curl)
        df = pd.DataFrame({'Карточка': [curl, 188500000]})
        df.to_excel('./st/autost/ex/ur.xlsx')
    except Exception:
        print("Ошибка: Готово3 /компаниирф.рф")
        curl="non1"
        df = pd.DataFrame({'Карточка': [curl, 188500000]})
        df.to_excel('./st/autost/ex/ur.xlsx') 
        pass
    # print(driver.current_url)
    
    # /html/body/div[1]/header/div/div[3]/a
    # /html/body/div[1]/main/div/table/tbody/tr/td[1]/span/a