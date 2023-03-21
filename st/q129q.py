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
            w=f"https://xn--80apmglwl.xn--p1ai/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D1%84%D0%B8%D1%80%D0%BC%D1%83"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[1]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl1 /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[2]/input[1]")
        zz.clear()
        zz.send_keys("\""+namecl+"\"")
    except Exception:
        print("Ошибка: namecl2 /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[2]/input[2]")
        zz.clear()
        zz.send_keys("ООО")
    except Exception:
        print("Ошибка: ООО /офирмах.рф")
        pass
    try:
        # brow.find_element(By.XPATH, f"/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[4]/td[2]/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[2]/form/div[2]/div[3]/select/option[contains(text(),'{city}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[4]/select/option[10]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[5]/select/option[12]").click()
    except Exception:
        print("Ошибка: city+категории /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[1]/input[1]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[1]/input[2]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[2]/input[2]")
        zz.clear()
        zz.send_keys(numcodcity)
    except Exception:
        print("Ошибка: numcodcity /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[2]/input[3]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: numclshot /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[5]/input")
        zz.clear()
        zz.send_keys(mail)
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[9]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[8]/input")
        zz.clear()
        zz.send_keys(url[8:])
    except Exception:
        print("Ошибка: url /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[10]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[11]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /офирмах.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/div[2]/div[12]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /офирмах.рф")
        pass