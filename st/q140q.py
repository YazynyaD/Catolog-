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
            w=f"http://msk24.net/companies/add.html"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: v /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /msk24.net")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/select/option[9]").click()
    except Exception:
        print("Ошибка: categor /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[5]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[6]/td[2]/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[9]/td[2]/textarea")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[10]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[12]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[13]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /msk24.net")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr[14]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /msk24.net")
        pass