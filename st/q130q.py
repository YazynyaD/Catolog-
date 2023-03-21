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
            w=f"https://optom365.ru/add-firm.php"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[1]/a").click()
        sleep(2)
    except Exception:
        print("Ошибка: namecl /optom365.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[2]/div[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[2]/a[2]").click()
        sleep(2)
    except Exception:
        print("Ошибка: desc /optom365.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[3]/div[2]/textarea")
        zz.clear()
        zz.send_keys(keysl)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[3]/a[2]").click()
        sleep(2)
    except Exception:
        print("Ошибка: keysl /optom365.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[3]/div/div/div/form/div[4]/div[2]/select/option[contains(text(),'{cityr}')]").click()
        # brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/form/div[2]/div[3]/select/option[contains(text(),'{city}')]").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[1]/a").click()
        sleep(2)
    except Exception:
        print("Ошибка: cityr /optom365.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[1]/div[2]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /optom365.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /optom365.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[3]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /optom365.ru")
        pass
