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
            w=f"https://wk3.ru/add-found"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /wk3.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[3]/select/option[2]").click()
        sleep(1)
        # brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/div[2]/form/div[2]/div[1]/div/div/div/div/select[1]/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[4]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[5]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city|cityr /wk3.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[6]/select/option[10]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[7]/select/option[31]").click()
    except Exception:
        print("Ошибка: категории /wk3.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[8]/input")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /wk3.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[10]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /wk3.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[11]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /wk3.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[12]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /wk3.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/article/div/form/div[13]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /wk3.ru")
        pass
    