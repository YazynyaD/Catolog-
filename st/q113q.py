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
            w=f"http://www.catalogvn.ru/regfirm/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[1]/td[3]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[3]/td[3]/input")
        zz.clear()
        zz.send_keys(cityr)
    except Exception:
        print("Ошибка: cityr /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[5]/td[3]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[7]/td[3]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[9]/td[3]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[11]/td[3]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[15]/td[3]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[17]/td[3]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[19]/td[3]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc1 /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[21]/td[3]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc2 /www.catalogvn.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[23]/td[3]/input[1]")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /www.catalogvn.ru")
        pass
    