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
            w=f"https://icomms.ru/add.html"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/section/form/div[2]/table/tbody/tr[1]/td/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /icomms.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div/div[2]/div[1]/section/form/div[2]/table/tbody/tr[2]/td/div[2]/select/option[contains(text(),'{city}')]").click()
        # brow.find_element(By.XPATH, f"/html/body/main/div[1]/div/form/div[2]/div[2]/div[1]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city /icomms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/section/form/div[2]/table/tbody/tr[3]/td/div[2]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /icomms.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/section/form/div[2]/table/tbody/tr[5]/td/div[1]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/select/option[11]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/select/option[9]").click()
        sleep(1)
    except Exception:
        print("Ошибка: категории /icomms.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/section/form/div[2]/table/tbody/tr[6]/td[1]/div[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /icomms.ru")
        pass
    