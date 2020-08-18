from selenium import webdriver
import time
proxylist="0.0.0.0"
portlist=8080
proxyline=1
def Readproxies():
        global proxylist
        global portlist
        global proxyline
        #If you want u can change "proxies.txt" for different location of your proxy list.
        txt=open("proxies.txt", "r")
        proxies=txt.readlines()[proxyline]
        for i in range(0,len(proxies)+1):
            a=proxies[i]
            if a==":":
                proxylist=proxies[0:i]
                portlist=proxies[i+1:len(proxies)]
                proxyline+=1
                break

def Proxyprofile_Chrome():
    global browser
    full_proxy=proxylist+":"+portlist

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % full_proxy)
    browser = webdriver.Chrome(executable_path=r"chromedriver.exe", options=chrome_options)
    print(proxylist)
    print(portlist)



def Startprocess_Chrome():
        try:
            #Change this for your website.
            browser.get("https://google.com/")
            time.sleep(60)
            browser.quit()
        except:
            print("One error is happened.Please reboot this session.")
            browser.quit()
            
        

def Proxyprofile():
        global profile
        profile=webdriver.FirefoxProfile()
        profile.set_preference("privacy.trackingprotection.enabled ", 0)
        profile.set_preference("dom.push.connection.enabled",0)
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http",str(proxylist))
        profile.set_preference("network.proxy.http_port",int(portlist))
        profile.set_preference("network.proxy.ssl",str(proxylist))
        profile.set_preference("network.proxy.ssl_port", int(portlist))
        profile.set_preference("dom.disable_open_during_load", False)
        print(proxylist)
        print(portlist)


def Startprocess():
        global driver,profile
        driver=webdriver.Firefox(executable_path=r"geckodriver.exe",firefox_profile=profile)
        #driver.set_page_load_timeout(40)
        try:
            #Change this for your website.
            driver.get("https://google.com/")
            time.sleep(60)
            driver.quit()
        except:
            print("One error is happened.Please reboot this session.")
            driver.quit()
            




while True:
        Readproxies()
        Proxyprofile()
        Startprocess()



"""while True:
        Readproxies()
        Proxyprofile_Chrome()
        Startprocess_Chrome()"""
