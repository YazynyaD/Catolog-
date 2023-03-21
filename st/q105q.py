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
            w=f"http://katpo.ru/reg.php"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[1]/td/select/optgroup[13]/option[3]").click()
    except Exception:
        print("Ошибка: категории /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[2]/td/input[1]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[3]/td/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[4]/td/input")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /katpo.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[5]/td/select/option[21]").click()
        brow.find_element(By.XPATH, f"/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[6]/td/select/option[contains(text(),'{cityr}')]").click()
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[7]/td/input")
        zz.clear()
        zz.send_keys(city)
        # brow.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/form/table/tbody/tr[1]/td[2]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: city /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[8]/td/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[9]/td/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[10]/td/input")
        zz.clear()
        zz.send_keys(numclinic)
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[12]/td/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[14]/td/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[15]/td/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[21]/td/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[21]/td/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login1 /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[23]/td/input[1]")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login2 /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[24]/td/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /katpo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[25]/td/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /katpo.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[26]/td/input[1]").click()
    except Exception:
        print("Ошибка: правила /katpo.ru")
        pass