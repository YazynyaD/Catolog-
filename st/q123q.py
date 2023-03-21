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
            w=f"https://moskva.nashigoroda.ru/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /moskva.nashigoroda.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[4]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /moskva.nashigoroda.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[10]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /moskva.nashigoroda.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[14]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /moskva.nashigoroda.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[16]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /moskva.nashigoroda.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[18]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /moskva.nashigoroda.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/form/div[20]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /moskva.nashigoroda.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/form/div[7]/select/optgroup[9]/option[10]").click()
    except Exception:
        print("Ошибка: timework /moskva.nashigoroda.ru")
        pass