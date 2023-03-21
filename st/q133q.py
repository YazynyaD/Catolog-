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
            w=f"https://odintsovo.biz/anketa.asp?div_id=1"
    brow.get(url=w)
    # brow.find_element(By.XPATH, "/html/").click()
    try:
        brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/select/option[56]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[1]/div/input").click()
        brow.find_element(By.XPATH, "/html/body/div[3]/div/div/form/div[2]/button").click()
        brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[1]/div/button").click()
    except Exception:
        print("Ошибка: категории+ /odintsovo.biz")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/select/option[1]").click()
    except Exception:
        print("Ошибка: ooo /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc1 /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[2]/table/tbody/tr[8]/td[1]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc2 /odintsovo.biz")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[2]/div/button[2]").click()
    except Exception:
        print("Ошибка: next /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[3]/table/tbody/tr[8]/td[1]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[3]/table/tbody/tr[10]/td[1]/textarea")
        zz.clear()
        zz.send_keys(adress)
    except Exception:
        print("Ошибка: adress /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[3]/table/tbody/tr[16]/td[1]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /odintsovo.biz")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/section/form/div[2]/div/div[3]/table/tbody/tr[20]/td[1]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /odintsovo.biz")
        pass
    