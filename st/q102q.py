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
            w=f"https://blizko.pro/add"
    brow.get(url=w)
    try:
        # brow.find_element(By.XPATH, f"/html/body/main/div[1]/div/form/div[2]/div[1]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[1]/div[1]/div/select/option[4]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[1]/div[2]/div/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[1]/div[3]/div/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: xp /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[2]/div[1]/div/input[2]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[2]/div[2]/div/input[1]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[4]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[4]/div[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[4]/div[3]/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /blizko.pro")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[5]/div[2]/div[1]/div/select/option[5]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[5]/div[2]/div[2]/div/div/select/option[4]").click()
    except Exception:
        print("Ошибка: категория /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[6]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[7]/div/span[2]/span[1]/span/span/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[9]/div[1]/div[1]/div/div/div[1]/input[1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[9]/div[1]/div[1]/div/div/div[1]/input[2]")
        zz.clear()
        zz.send_keys("00:00")
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[9]/div[1]/div[2]/div/div/div[1]/input[1]")
        zz.clear()
        zz.send_keys("23:59")
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[9]/div[1]/div[2]/div/div/div[1]/input[2]")
        zz.clear()
        zz.send_keys("00:00")
    except Exception:
        print("Ошибка: timework /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[12]/div[1]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[12]/div[2]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[12]/div[3]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[17]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[18]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw1 /blizko.pro")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div/div[1]/div/div[19]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw2 /blizko.pro")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[20]/div/label/input[2]").click()
    except Exception:
        print("Ошибка: правила /blizko.pro")
        pass
    
    