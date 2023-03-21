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
            w=f"https://nashaspravka.ru/add_firm"
    brow.get(url=w)
    try:
        # brow.find_element(By.XPATH, f"/html/body/main/div/noindex/div/div[3]/form/div[3]/div[2]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[2]/div/select/option[contains(text(),'{city} ({cityr})')]").click()
    except Exception:
        print("Ошибка: city /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[3]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[4]/div/textarea")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[5]/div/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[6]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[7]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /nashaspravka.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[8]/div/select/option[69]").click()
    except Exception:
        print("Ошибка: categ /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[9]/div/textarea")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /nashaspravka.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[10]/div/label/input").click()
        brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[11]/div/label/input").click()
    except Exception:
        print("Ошибка: re /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[13]/div/input")
        zz.clear()
        zz.send_keys(i+" "+f)
    except Exception:
        print("Ошибка: i+f /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[14]/div/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /nashaspravka.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/main/div[1]/section/form/div[15]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /nashaspravka.ru")
        pass