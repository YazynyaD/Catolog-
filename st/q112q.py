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
            w=f"https://btk-online.ru/search/add_search.html"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[6]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/textarea[1]")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[7]")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[8]")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[9]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[11]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[12]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[13]")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[14]")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /btk-online.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/center/div/center/div[4]/div/div[1]/div/div[2]/form/input[15]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /btk-online.ru")
        pass
    
    