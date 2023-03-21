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
            w=f"https://adresa-nomera.ru/0/new"
    brow.get(url=w)
    try:
        # brow.find_element(By.XPATH, f"/html/body/div[2]/div[1]/form/div/div[1]/div/div[1]/div[2]/div/select/option[contains(text(),'{cityr}')]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/form/table/tbody/tr[1]/td[2]/select/option[contains(text(),'{cityr}')]").click()
    except Exception:
        print("Ошибка: namecl /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[5]/td[2]/textarea")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[6]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[7]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[9]/td[2]/input[1]")
        zz.clear()
        zz.send_keys(fio)
    except Exception:
        print("Ошибка: fio /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[9]/td[2]/input[2]")
        zz.clear()
        zz.send_keys("Менеджер")
    except Exception:
        print("Ошибка: Менеджер /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[11]/td[2]/textarea")
        zz.clear()
        zz.send_keys(timework)
    except Exception:
        print("Ошибка: timework /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[12]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /adresa-nomera.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr[13]/td[2]/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /adresa-nomera.ru")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/form/table/tbody/tr[14]/td[2]/div[1]/span[1]/select/option[7]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/form/table/tbody/tr[14]/td[2]/div[1]/span[2]/select/option[3]").click()
    except Exception:
        print("Ошибка: категории /adresa-nomera.ru")
        pass
    
    