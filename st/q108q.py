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
            w=f"https://myfirms.su/neworg"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[1]/div[2]/div/input")
        zz.clear()
        zz.send_keys(login)
    except Exception:
        print("Ошибка: login /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[1]/div[3]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[2]/div[3]/div/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[2]/div[4]/div/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[2]/div[5]/div/input")
        zz.clear()
        zz.send_keys(unamecl)
    except Exception:
        print("Ошибка: unamecl /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[2]/div[6]/div/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc /myfirms.su")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[2]/div[7]/div/select[1]/option[13]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[2]/div[7]/div/select[2]/option[17]").click()
    except Exception:
        print("Ошибка: категории /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[2]/div[8]/div/textarea")
        zz.clear()
        zz.send_keys(keysl)
    except Exception:
        print("Ошибка: keysl /myfirms.su")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[3]/div[2]/div/div[1]/select[1]/option[contains(text(),'{cityr}')]").click()
        sleep(1)
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[3]/div[2]/div/div[1]/select[2]/option[contains(text(),'{city}')]").click()
    except Exception:
        print("Ошибка: city /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[3]/div[3]/div/input")
        zz.clear()
        zz.send_keys(ind)
    except Exception:
        print("Ошибка: ind /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[3]/div[4]/div/input")
        zz.clear()
        zz.send_keys(street)
    except Exception:
        print("Ошибка: street /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[3]/div[5]/div/input")
        zz.clear()
        zz.send_keys(home)
    except Exception:
        print("Ошибка: home /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[4]/div[3]/div/input")
        zz.clear()
        zz.send_keys(numclinic)
    except Exception:
        print("Ошибка: numclinic /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[4]/div[5]/div/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /myfirms.su")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[4]/div[6]/div/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /myfirms.su")
        pass
    try:
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[1]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[1]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[1]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[1]/div[2]/div[2]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[2]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[2]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[2]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[2]/div[2]/div[2]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[3]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[3]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[3]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[3]/div[2]/div[2]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[4]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[4]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[4]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[4]/div[2]/div[2]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[5]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[5]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[5]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[5]/div[2]/div[2]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[6]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[6]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[6]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[6]/div[2]/div[2]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[7]/div[2]/div[1]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[7]/div[2]/div[1]/select[2]/option[5]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[7]/div[2]/div[2]/select[1]/option[24]").click()
        brow.find_element(By.XPATH, f"/html/body/div[1]/main/div/form/fieldset[5]/div/div/div[7]/div[2]/div[2]/select[2]/option[5]").click()
    except Exception:
        print("Ошибка: timework /myfirms.su")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[1]/main/div/form/fieldset[6]/div[1]/input").click()
    except Exception:
        print("Ошибка: правила /myfirms.su")
        pass