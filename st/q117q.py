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
            w=f"https://www.sitebase.ru/addfirm.html"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[1]/td[2]/select/option[9]").click()
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.sitebase.ru")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /www.sitebase.ru")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys("+7("+numcodcity+")")
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[3]/input")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: num /www.sitebase.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/table[2]/tbody/tr[2]/td/span/table/tbody/tr[2]/td/iframe").click()
        zz=brow.find_element(By.XPATH, "/html/body")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.sitebase.ru")
        pass
    try:
        # brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[3]/div[2]/div/div[1]/select[1]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/select/option[contains(text(),'{cityr}')]").click()
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/table/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[7]/td[2]/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[7]/td[2]/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[7]/td[2]/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /www.sitebase.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[9]/td[2]/table/tbody/tr/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail3 /www.sitebase.ru")
        pass
    