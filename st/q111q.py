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
            w=f"http://nnit.ru/"
    brow.get(url=w)
    try:
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div[3]/a").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[2]/div/input[9]").click()
    except Exception:
        print("Ошибка: переход/категории /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[4]/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[5]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[8]/textarea")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[10]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[11]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[13]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[17]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[18]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /nnit.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[19]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /nnit.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[1]/noindex[1]/div/div/form/div[22]/input").click()
    except Exception:
        print("Ошибка: правила /nnit.ru")
        pass