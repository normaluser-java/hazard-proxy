import threading, requests, random, time, re, ctypes, os
proxylistlog = []
proxycount = 0
startTime = time.time()
os.system("mode 125, 20")
print(f"Hazard's scraper")
print("RDIMO PLEASE DONT SUE ME I DIDN'T WANTED TO SKID YOUR FUCKING CODE")
print("it prints and it's slowed down to make you see how it works")
time.sleep(3)
print("Starting")

def settitle(text):
    ctypes.windll.kernel32.SetConsoleTitleW(text)

def fetchProxies(url, custom_regex):
    time.sleep(3)
    global proxycount, proxylist
    try:
        proxylist = requests.get(url, timeout=5).text
    except Exception:
        pass
    finally:
        proxylist = proxylist.replace('null', '')
    #get the proxies from all the sites with the custom regex
    custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
    custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
    for proxy in re.findall(re.compile(custom_regex), proxylist):
        proxylistlog.append(f"{proxy[0]}:{proxy[1]}")
        time.sleep(0.02)
        proxycount += 1
        settitle(f"{proxycount} proxies | {url}")
        print(f"Scraped proxy: {proxy[0]}:{proxy[1]}")

#all urls
proxysources = [
    ["http://spys.me/proxy.txt","%ip%:%port% "],
    ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
    ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
    ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
    ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
    ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
    ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
    ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
    ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
    ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
    ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
    ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
    ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
    ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
    ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
    ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
    ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
]
threads = [] 
settitle("Sending requests")
for url in proxysources:
    print(f"Scraping proxies from {url[0]} (scrap starts in 3 on this url)")
    #send them out in threads
    t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

proxies = list(set(proxylistlog))
with open(f"proxies.txt", "w") as f:
    for proxy in proxies:
        for i in range(random.randint(7, 10)):
            f.write(f"{proxy}\n")
        print(f"Writed {i} times {proxy} into txt file")
    f.close()

execution_time = (time.time() - startTime)
print(f"scraped and saved proxies")
print("this (proxy scraper) wasn't made by rdimo guy (don't get a lawyer pls), i just made it so fre proxies!!!1")
print("also if you dont see files then add extensions to anti-virus (idk why this happens but it happens)")
print(f"thanks for wasting {execution_time} seconds of ur life")
input()