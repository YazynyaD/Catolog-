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
            w=f"https://tilbagevise.ru/add/"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[2]/div[2]/input")
        zz.clear()
        zz.send_keys(i)
    except Exception:
        print("Ошибка: i /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[3]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[5]/div[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[6]/div[2]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[7]/div[2]/input")
        zz.clear()
        zz.send_keys(ciadress)
    except Exception:
        print("Ошибка: ciadress /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[8]/div[2]/input")
        zz.clear()
        zz.send_keys(numpl)
    except Exception:
        print("Ошибка: numpl /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[9]/div[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[10]/div[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[11]/div[2]/input")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[12]/div[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /tilbagevise.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div/div[13]/div[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /tilbagevise.ru")
        pass
    