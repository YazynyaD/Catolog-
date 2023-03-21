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
            w=f"http://b2b-russia.ru/add"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(namecl)
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[4]/td[2]/button").click()
        sleep(2)
    except Exception:
        print("Ошибка: переход /b2b-russia.ru")
        pass
    
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(ciadress)
        # zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[3]/td[2]/input")
        # zz.clear()
        # zz.send_keys(numclinic)
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[4]/td[2]/button").click()
        sleep(2)
    except Exception:
        print("Ошибка: переход /b2b-russia.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/div[1]/div[3]/div/strong[2]/a").click()
        sleep(2)
        
    except Exception:
        print("Ошибка: переход /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[1]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl1 /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[2]/td[2]/input[1]")
        zz.clear()
        zz.send_keys("ООО")
    except Exception:
        print("Ошибка: ООО /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[2]/td[2]/input[2]")
        zz.clear()
        zz.send_keys("\""+namecl+"\"")
    except Exception:
        print("Ошибка: namecl2 /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[3]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /b2b-russia.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[4]/td[2]/select/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[6]/td[2]/div[1]/a/a").click()
        sleep(1)
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[6]/td[2]/div[2]/div[1]/table/tbody/tr/td[1]/div/input")
        zz.clear()
        zz.send_keys(city)
        # brow.find_element(By.XPATH, f"/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[8]/select/option[contains(text(),'{cityr}')]").click()
        # brow.find_element(By.XPATH, f"/html/body/div[1]/div/div/main/article/div[1]/form/ul/li[8]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[7]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[1]/tbody/tr[8]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/input[1]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/input[3]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: num /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[2]/tbody/tr[5]/td[2]/input")
        zz.clear()
        zz.send_keys(url[8:])
    except Exception:
        print("Ошибка: url /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[2]/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[1]/div/table[2]/tbody/tr[7]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[2]/div/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[2]/div/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[2]/div/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[2]/div/table/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /b2b-russia.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[8]/div[2]/table/tbody/tr/td[1]/input[1]")
        zz.clear()
        zz.send_keys(tupecl)
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[8]/div[2]/table/tbody/tr/td[2]/div").click()
        sleep(2)
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/div[8]/div[2]/fieldset/div/div/table/tbody/tr[1]/td[2]/a").click()
    except Exception:
        print("Ошибка: категории /b2b-russia.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr/td[1]/table[4]/tbody/tr/td[1]/input").click()
    except Exception:
        print("Ошибка: правила /b2b-russia.ru")
        pass