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
            w=f"http://bdpoi.ru/addnewfirm/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/input[1]")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /bdpoi.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/input[3]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /bdpoi.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/input[4]")
        zz.clear()
        zz.send_keys(numn)
    except Exception:
        print("Ошибка: numn /bdpoi.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/input[7]")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /bdpoi.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/select[2]/option[7]").click()
        brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/select[3]/option[17]").click()
        brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/select[5]/option[17]").click()
    except Exception:
        print("Ошибка: timework /bdpoi.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/input[8]")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /bdpoi.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /bdpoi.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/form/input[9]")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /bdpoi.ru")
        pass
    
    