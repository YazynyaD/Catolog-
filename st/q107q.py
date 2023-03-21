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
            w=f"http://xn--80aale8ch.xn--p1ai/%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%84%D0%B8%D1%80%D0%BC%D1%83"
    brow.get(url=w)
    try:
        brow.find_element(By.XPATH, f"/html/body/form/table/tbody/tr/td/table[1]/tbody/tr/td[2]/select/option[10]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/form/table/tbody/tr/td/div[1]/table/tbody/tr/td[2]/select/option[41]").click()
    except Exception:
        print("Ошибка: категории /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /адреса.рф")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[4]/td[2]/select/option[contains(text(),'{city}')]").click()
        # brow.find_element(By.XPATH, f"/html/body/div/div/div/div/div[7]/div/div[2]/div/form/table/tbody/tr[5]/td[2]/select/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/div[3]/table/tbody/tr/td[2]/input[2]")
        zz.clear()
        zz.send_keys(numcodcity)
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/div[3]/table/tbody/tr/td[2]/input[3]")
        zz.clear()
        zz.send_keys(numclshot)
    except Exception:
        print("Ошибка: num /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[6]/tbody/tr[1]/td[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[6]/tbody/tr[2]/td[2]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[6]/tbody/tr[4]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[6]/tbody/tr[5]/td[2]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /адреса.рф")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[6]/tbody/tr[6]/td[2]/input[2]")
        zz.clear()
        zz.send_keys("48")
    except Exception:
        print("Ошибка: 48 /адреса.рф")
        pass
    