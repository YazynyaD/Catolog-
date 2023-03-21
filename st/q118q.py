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
            w=f"https://esbd.ru/add#"
    brow.get(url=w)
    try:
        # brow.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/form/select[1]/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/form/select[2]/option[contains(text(),'{city}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/form/select[3]/option[22]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: city /esbd.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/input[2]")
        zz.clear()
        zz.send_keys(namecl)
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: namecl /esbd.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/input[3]")
        zz.clear()
        zz.send_keys(adress)
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: adress /esbd.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/input[4]")
        zz.clear()
        zz.send_keys(numpl)
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: numpl /esbd.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/input[5]")
        zz.clear()
        zz.send_keys(url)
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: url /esbd.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/input[6]")
        zz.clear()
        zz.send_keys(timework)
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: timework /esbd.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/textarea")
        zz.clear()
        zz.send_keys(desc)
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[6]/div").click()
        sleep(1)
    except Exception:
        print("Ошибка: desc /esbd.ru")
        pass
    