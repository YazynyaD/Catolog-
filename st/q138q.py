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
            w=f"https://kaz.all-gorod.ru/add"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[1]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl1 /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[2]/td[2]/input[1]")
        zz.clear()
        zz.send_keys("ООО")
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[2]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl2 /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[3]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[4]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[5]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[6]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/input[2]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[7]/td[2]/table/tbody/tr/td[2]/input[3]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: num1 /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[11]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[12]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail1 /kaz.all-gorod.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[3]/div/table/tbody/tr[13]/td[2]/table/tbody/tr[1]/td/input").click()
    except Exception:
        print("Ошибка: time /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[5]/div/table/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[5]/div/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[5]/div/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail2 /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[5]/div/table/tbody/tr[4]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[5]/div/table/tbody/tr[4]/td[2]/input[2]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: num2 /kaz.all-gorod.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[9]/div/table/tbody/tr[1]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /kaz.all-gorod.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[8]/div[6]/div").click()
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[8]/div[7]/table/tbody/tr/td[1]/input[1]")
        zz.clear()
        zz.send_keys("Наркологическая")
        brow.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/div/div/form/div[8]/div[7]/fieldset[1]/div/div/table/tbody/tr[2]/td[2]/a").click()
    except Exception:
        print("Ошибка: categor /kaz.all-gorod.ru")
        pass