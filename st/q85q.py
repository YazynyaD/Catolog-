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
            w=f"http://www.binfo.ru/main/company.asp?mod=i"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[4]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[6]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[7]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[20]/td[2]/input")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[21]/td[2]/input")
        zz.clear()
        zz.send_keys(f)
    except Exception:
        print("Ошибка: f /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[22]/td[2]/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[23]/td[2]/input")
        zz.clear()
        zz.send_keys(o)
    except Exception:
        print("Ошибка: o /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[24]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[25]/td[2]/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[30]/td[2]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /www.binfo.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[31]/td[2]/input")
        zz.clear()
        zz.send_keys(passw)
    except Exception:
        print("Ошибка: passw /www.binfo.ru")
        pass
    