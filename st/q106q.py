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
            w=f"https://catcompany.ru/dobavit-kompaniyu.html"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /catcompany.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[3]/td[2]/select/option[9]").click()
    except Exception:
        print("Ошибка: категории /catcompany.ru")
        pass
    try:
        # brow.find_element(By.XPATH, f"/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[6]/td/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[5]/td[2]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[7]/td[2]/textarea")
        zz.clear()
        zz.send_keys(ciadress)
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[8]/td[2]/textarea")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[9]/td[2]/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[10]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[11]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /catcompany.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[12]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /catcompany.ru")
        pass
    
    