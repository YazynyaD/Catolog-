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
            w=f"http://www.nofollow.ru/?page=add"
    brow.get(url=w)
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[2]/input")
        zz.clear()
        zz.send_keys(url)
    except Exception:
        print("Ошибка: url /www.nofollow.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[4]/input")
        zz.clear()
        zz.send_keys(namecl)
    except Exception:
        print("Ошибка: namecl /www.nofollow.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[6]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc1 /www.nofollow.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[8]/textarea")
        zz.clear()
        zz.send_keys(desc)
    except Exception:
        print("Ошибка: desc2 /www.nofollow.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[10]/input")
        zz.clear()
        zz.send_keys(city)
    except Exception:
        print("Ошибка: city /www.nofollow.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[12]/input")
        zz.clear()
        zz.send_keys(mail)
    except Exception:
        print("Ошибка: mail /www.nofollow.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[14]/select/option[85]").click()
    except Exception:
        print("Ошибка: категории /www.nofollow.ru")
        pass
    try:
        brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/p[16]/select/option[4]").click()
    except Exception:
        print("Ошибка: правила /www.nofollow.ru")
        pass
    try:
        zz=brow.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/div[6]/p[2]/input")
        zz.clear()
        zz.send_keys(tupecl)
    except Exception:
        print("Ошибка: tupecl /www.nofollow.ru")
        pass
   