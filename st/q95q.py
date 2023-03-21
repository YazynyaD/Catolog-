import array as arr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def goo(brow,z,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    br=brow
    brow.execute_script("window.open('');")
    brow.switch_to.window(brow.window_handles[z])
    ct1(br,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind)
def ct1(brow,ur,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,url,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind):
    wwww=notwww.split("\n")
    cit=city
    for q in wwww:
        if "mediapure.ru" in q or "82" in q:
            w="https://mediapure.ru/wp-content/uploads/2017/12/error-1021x580.jpg"
            return 0
        else:
            w=f"http://orgcatalog.ru/how-add-company"
    brow.get(url=w)
    try:
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/ul/li[1]/span/a").click()
        sleep(1)
        # brow.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div[2]/select/option[contains(text(),'{city}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div/div[2]/select/option[contains(text(),'{city}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/a").click()
        sleep(2)
    except Exception:
        print("Ошибка: namecl /orgcatalog.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /orgcatalog.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[3]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /orgcatalog.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[5]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /orgcatalog.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[6]/div/div/div[1]/table/tbody/tr/td[2]/div/input")
        zz.clear()
        zz.send_keys(numcodcity)
    except Exception:
        print("Ошибка: numcodcity /orgcatalog.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[6]/div/div/div[1]/table/tbody/tr/td[3]/div/input")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: numclshot /orgcatalog.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[7]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[7]/div/div/div[1]/div[2]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[7]/div/div/div[2]/div[2]/a[1]").click()
    except Exception:
        print("Ошибка: timework /orgcatalog.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[8]/a").click()
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[8]/div/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /orgcatalog.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[9]/a").click()
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[9]/div/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /orgcatalog.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[11]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/ul/li[6]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/ul[2]/li[24]/a").click()
    except Exception:
        print("Ошибка: категории /orgcatalog.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div/div[2]/form/div[12]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /orgcatalog.ru")
        pass
    
    