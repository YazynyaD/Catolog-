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
            w=f"https://www.sdki.ru/firms/add/uslugi/uslugi-rek.html"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.sdki.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys("Россия, "+city)
    except Exception:
        print("Ошибка: city /www.sdki.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.sdki.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.sdki.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.sdki.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.sdki.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.sdki.ru")
        pass
    
    