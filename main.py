
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
from PIL import Image
from twocaptcha import TwoCaptcha
from bs4 import BeautifulSoup
import re
import time, random, sys
from colorama import Fore, Style
opt = Options()


driver = webdriver.Chrome()

def crop():
    driver.get('https://zone-h.org/archive/published=0')
    driver.get_screenshot_as_file('f.png')
    Directory = os.getcwd()
    path = os.path.join(Directory, 'f.png')
    pathToSave = os.path.join(Directory, 'captch.png')
    im = Image.open(path)
    current_height, current_width = im.size
    xcenter = im.width/2
    ycenter = im.height/2
    x1 = xcenter - 500
    y1 = ycenter - 280
    x2 = xcenter + 80
    y2 = ycenter + 30
    
    im1 = im.crop((x1, y1, x2, 164))
    
    im1.save(fp="file.png")

def captcha():
    try:
        solver = TwoCaptcha('REPLACE YOUR 2CAPTCHA TOKEN')
        currentDi = os.getcwd()
        path = os.path.join(currentDi, 'file.png')
        result = solver.normal(path)
        print(result['code'])
        driver.find_element(By.XPATH, '//*[@id="propdeface"]/form/input[1]').send_keys(str(result['code']))
        driver.find_element(By.XPATH, '//*[@id="propdeface"]/form/input[2]').click()
    except:
        driver.find_element(By.XPATH, '//*[@id="propdeface"]/table/tbody/tr/td[2]/a/img').click()


def notiferFunction():
    for pg in range(1, 51):

        driver.get('https://zone-h.org/archive/published=0/page={}'.format(pg))
        SrcePage = driver.page_source
        if "If you often get this captcha when gathering data" in SrcePage:
                    message = "\nSolving Captcha ..."
    
                    for char in message:
                        sys.stdout.write(Fore.GREEN + char + Style.RESET_ALL)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    crop()
                    captcha()
                    continue
        else:
            soup = BeautifulSoup(SrcePage, 'html.parser')
                
            parenter = soup.find('table', {'id':'ldeface'})

            otherParent = parenter.findAll('a', href=True)
            with open('notiferz.txt','a') as notfier:

                for link in otherParent:
                    if "archive/notifier" in link['href']:
                        notiferName = link['href']
                        print(link.text)
                        notfier.write('https://zone-h.org{}'.format(str(notiferName)) + '\n')
                    else:
                        pass


def RemoveDuplicate():
    uniqlines = set(open('notiferz.txt').readlines())
    with open('Notifer_Result.txt', 'a') as notiferResult:
        for n in uniqlines:
            notiferResult.write(n.strip() + '\n')
    os.remove('notiferz.txt')



def BulkChecker():
    with open('Notifer_Result.txt','r') as nRez:
        for nA in nRez:
            for p in range(1, 50):

                driver.get(nA + '/page={}'.format(p))
                srcePage = driver.page_source
                if "If you often get this captcha when gathering data" in srcePage:
                    message = "\nSolving Captcha ..."
    
                    for char in message:
                        sys.stdout.write(Fore.GREEN + char + Style.RESET_ALL)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    crop()
                    captcha()
                    continue
                else:
                    try:

                        soup = BeautifulSoup(srcePage, 'html.parser')
                        #Getting Pages to range through
                        amir=soup.find("td", {"class": "defacepages"})
                        v = amir.text.strip()

                        if v == "0":
                            break

                        elif str(v[-2] + v[-1]).strip() == str(p):
                            break
                    
                        else:

                            parenter = soup.find('table', {'id':'ldeface'})
                            otherParent = parenter.findAll('td')

                            with open('TheResults.txt','a') as Rez:
                                #Scraping
                                for site in otherParent:
                                        if "DISCLAIMER"  in site.text:
                                                    pass
                                        elif "." in site.text:
                                                actualSite = site.text.strip().split('/', 1)
                                                print(actualSite[0])
                                                Rez.write(str(actualSite[0]) + '\n')
                                        else:
                                            pass
                    except IndexError:
                        break
                    except Exception as e:
                        break


def IPBulk():
    with open('Notifer_Result.txt','r') as nRez:
        for nA in nRez:
            for p in range(1, 50):

                driver.get(nA + '/page={}'.format(p))
                srcePage = driver.page_source
                if "If you often get this captcha when gathering data" in srcePage:
                    message = "\nSolving Captcha ..."
    
                    for char in message:
                        sys.stdout.write(Fore.GREEN + char + Style.RESET_ALL)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    crop()
                    captcha()
                    continue
                else:
                    try:

                        soup = BeautifulSoup(srcePage, 'html.parser')
                        #Getting Pages to range through
                        amir=soup.find("td", {"class": "defacepages"})
                        v = amir.text.strip()

                        if v == "0":
                            break

                        elif str(v[-2] + v[-1]).strip() == str(p):
                            break
                    
                        else:

                            parenter = soup.find('table', {'id':'ldeface'})
                            otherParent = parenter.findAll('a', href=True)
                            with open('TheResults.txt','a') as Rez:
                                #Scraping
                                for site in otherParent:
                                        if "/archive/ip" in site['href']:
                                            reAl = site['href'].replace('/archive/ip=', '')
                                            print(reAl)
                                            Rez.write(str(reAl) + '\n')
                                        else:
                                            pass
                    except IndexError:
                        break
                    except Exception as e:
                        break
def nameBulk():
            for p in range(1, 50):

                driver.get('https://zone-h.org/archive/published=0/' + '/page={}'.format(p))
                srcePage = driver.page_source
                if "If you often get this captcha when gathering data" in srcePage:
                    crop()
                    captcha()
                    continue
                else:
                    try:

                        

                        soup = BeautifulSoup(srcePage, 'html.parser')
                        #Getting Pages to range through
                        amir=soup.find("td", {"class": "defacepages"})
                        v = amir.text.strip()

                        if v == "0":
                            break

                        elif str(v[-2] + v[-1]).strip() == str(p):
                            break
                    
                        else:

                            parenter = soup.find('table', {'id':'ldeface'})
                            otherParent = parenter.findAll('td')

                            with open('TheResults.txt','a') as Rez:
                                #Scraping
                                for site in otherParent:
                                        if "DISCLAIMER"  in site.text:
                                                    pass
                                        elif "." in site.text:
                                                actualSite = site.text.strip().split('/', 1)
                                                print(actualSite[0])
                                                Rez.write(str(actualSite[0]) + '\n')
                                        else:
                                            pass
                    except IndexError:
                        break
                    except Exception as e:
                        break
if __name__ == "__main__":
    message = "\nStart Scraping ..."
    
    for char in message:
        sys.stdout.write(Fore.GREEN + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)

    notiferFunction()
    RemoveDuplicate()
    BulkChecker()