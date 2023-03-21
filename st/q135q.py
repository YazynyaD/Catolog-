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
            w=f"https://spravka.city/add/company"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[1]/div[3]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[1]/div[4]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /spravka.city")
        pass
    try:
        
        brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[2]/select/optgroup[8]/option[8]").click()
    except Exception:
        print("Ошибка: category /spravka.city")
        pass
    try:
        # brow.find_element(By.XPATH, f"/html/body/div[3]/div/div/div/form/div[4]/div[2]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/main/div/noindex/div/div[3]/form/div[3]/div[2]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/main/div/noindex/div/div[3]/form/div[3]/div[2]/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[3]/div[3]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[3]/div[4]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[4]/div[2]/div[1]/div/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[4]/div[3]/div[1]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[4]/div[4]/div[1]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[5]/div[2]/div[1]/div[1]/input[1]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[5]/div[2]/div[1]/div[1]/input[2]")
        zz.clear()
        zz.send_keys("00:00")
    except Exception:
        print("Ошибка: timework /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[5]/div[3]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /spravka.city")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/main/div/noindex/div/div[3]/form/div[6]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /spravka.city")
        pass
    