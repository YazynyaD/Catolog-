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
            w=f"https://info-torg.ru/about/zayavka/order/?cid=3812"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[1]/td/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl1 /info-torg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[2]/td/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl2 /info-torg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[3]/td/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /info-torg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[4]/td/textarea")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: url /info-torg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[5]/td/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic1 /info-torg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[6]/td/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: url /info-torg.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/form/table/tbody/tr[7]/td/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic2 /info-torg.ru")
        pass
   