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
            w=f"http://tradeis.ru/add-company"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[3]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[4]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /tradeis.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[5]/select/option[8]").click()
    except Exception:
        print("Ошибка: категории /tradeis.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[8]/select/option[contains(text(),'{city}')]").click()
        # brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/form/select[1]/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: city /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[9]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[12]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[14]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[16]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /tradeis.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[25]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /tradeis.ru")
        pass
    