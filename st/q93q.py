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
            w=f"https://placesrf.ru/new"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[2]/div[2]/div/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[2]/div[3]/div[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[3]/div[1]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[3]/div[2]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[3]/div[3]/table/tbody/tr[1]/td[3]/input")
        zz.send_keys("23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[3]/div[3]/table/tbody/tr[1]/td[5]/input")
        zz.send_keys("00:00")
    except Exception:
        print("Ошибка: timework /placesrf.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[4]/div[1]/div[1]/select[1]/option[71]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[4]/div[1]/div[1]/select[2]/option").click()
    except Exception:
        print("Ошибка: категории /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[4]/div[2]/div[1]/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /placesrf.ru")
        pass
    try:
        # brow.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div[2]/select/option[contains(text(),'{city}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[2]/main/div/form/div[5]/div[1]/div/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[2]/main/div/form/div[5]/div[2]/div/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[5]/div[3]/div/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[5]/div[4]/div/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[7]/div[1]/div/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[7]/div[2]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /placesrf.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[7]/div[3]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /placesrf.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[8]/input[1]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[2]/main/div/form/div[8]/div/input").click()
    except Exception:
        print("Ошибка: правила /placesrf.ru")
        pass
    
    