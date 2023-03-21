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
            w=f"https://www.plan1.ru/city/"
    brow.get(url=w)
    try:
        sleep(2)
        brow.find_element(By.XPATH, "//*[@id=\"FormAddCompanyHeader_small\"]").click()
        sleep(2)
    except Exception:
        print("Ошибка: переход /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[1]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[2]")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[3]")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[4]")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[5]")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[6]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[7]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.plan1.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/input[8]")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.plan1.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/a").click()
        brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/div[1]/div[1]/div[1]/input").click()
        brow.find_element(By.XPATH, "/html/body/noindex/div/div/div[2]/form/fieldset/div[1]/div[1]/div[2]/div/input").click()
        
    except Exception:
        print("Ошибка: timework /www.plan1.ru")
        pass