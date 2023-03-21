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
            w=f"https://mapmax.ru/"
    brow.get(url=w)
    try:
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/span").click()
        sleep(2)
        # brow.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div[2]/select/option[contains(text(),'{city}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div/div[4]/div[2]/div[3]/table/tbody/tr/td/form/select/option[contains(text(),'{city}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[3]/table/tbody/tr/td/form/input").click()
        sleep(3)
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div[7]/span/a").click()
        sleep(1)
    except Exception:
        print("Ошибка: переход /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[1]/td/div[1]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[2]/td/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[3]/td/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[4]/td/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[5]/td/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[6]/td/input[2]")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[7]/td/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[8]/td/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /mapmax.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/form/table/tbody/tr[9]/td/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /mapmax.ru")
        pass
    