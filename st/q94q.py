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
            w=f"https://orgsprav.com/company/add.html"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[2]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /orgsprav.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[3]/div/span/span[1]/span/span[1]").click()
        zz=brow.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        zz.clear()
        zz.send_keys("Наркологические клиники")
        zz.send_keys(Keys.ENTER)
    except Exception:
        print("Ошибка: категории /orgsprav.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[5]/div/textarea")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /orgsprav.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[5]/div/textarea")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /orgsprav.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[7]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /orgsprav.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[8]/div/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /orgsprav.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[9]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /orgsprav.com")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[10]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /orgsprav.com")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div[2]/form/div[11]/div[2]/div/input[2]").click()
    except Exception:
        print("Ошибка: правило /orgsprav.com")
        pass