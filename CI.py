#AingGabud
#Recode Gih :v

#import

import os
import time

#variabel

gy="\033[0;30m"  #abu-abu
lgy="\033[1;30m" #abu² cerah
rd="\033[0;31m"  #merah
lrd="\033[1;31m" #merah cerah
gr="\033[0;32m"  #hijau
lgr="\033[1;32m" #hijau cerah
yl="\033[0;33m"  #kuning
lyl="\033[1;33m" #kuning cerah
bl="\033[0;34m"  #biru
lbl="\033[1;34m" #biru cerah
pp="\033[0;35m"  #ungu
lpp="\033[1;35m" #ungu cerah
cy="\033[0;36m"  #cyan
lcy="\033[1;36m" #cyan cerah

#Mari Kita Mulai >:)

opening='''

   -----------------------------------------------------------
   |                                                         |
   |   ToolsName : ComInstaller		                     |
   |   Code : Python                      @ Mr.S             |
   |   Coder : Mr.S				             |
   |                                                         |
   |          + ~#  Menu List                     +          |
   |          +                                   +          |
   |          + ~[1]~ Show All Tools              +          |
   |          + ~[2]~ Install all Tools           +          |
   |          + ~[3]~ About Me                    +          |
   |          + ~[4]~ Exit                        +          |
   |                                                         |
   |__________________________     __________________________|
              ________________|___|________________
             (_____________________________________)
'''
os.system ("clear")
print (lgr,opening)
time.sleep(1)
print (lrd)
mn=input ("root@Mr.Squidy ~#: ")
if mn=="1" or mn=="01":
   m1='''

   -----------------------------------------------------------
   |                                                         |
   |   Menu :                                                |
   |                                                         |
   |   + ~[1]~ Metasploit                         +          |
   |   						             |
   |   						             |
   |   						             |
   |   						             |
   |   						             |
   |  						             |
   |   + ~[x]~ Exit                               +          |
   |                                                         |
   |__________________________     __________________________|
              ________________|___|________________
             (_____________________________________)
   '''
   m2='''
   -----------------------------------------------------------
   |                                                         |
   |   Menu :                                                |
   |                                                         |
   |   + ~[1]~ Metasploit                         +          |
   |   + ~[2]~ A-Rat                              +          |
   |   						             |
   |  						             |
   |   						             |
   |   						             |
   |   						             |
   |   + ~[x]~ Exit                               +          |
   |                                                         |
   |__________________________     __________________________|
              ________________|___|________________
             (_____________________________________)
   '''
   m3='''
   -----------------------------------------------------------
   |                                                         |
   |   Menu :                                                |
   |                                                         |
   |   + ~[1]~ Metasploit                         +          |
   |   + ~[2]~ A-Rat                              +          |
   |   + ~[3]~ DDOS                               +          |
   |                                                         |
   |                                                         |
   |                                                         |
   |                                                         |
   |   + ~[x]~ Exit                               +          |
   |                                                         |
   |__________________________     __________________________|
              ________________|___|________________
             (_____________________________________)
   '''
   m4='''
   -----------------------------------------------------------
   |                                                         |
   |   Menu :                                                |
   |                                                         |
   |   + ~[1]~ Metasploit                         +          |
   |   + ~[2]~ A-Rat                              +          |
   |   + ~[3]~ DDOS                               +          |
   |   + ~[4]~ Webdav                             +          |
   |                                                         |
   |                                                         |
   |                                                         |
   |   + ~[x]~ Exit                               +          |
   |                                                         |
   |__________________________     __________________________|
              ________________|___|________________
             (_____________________________________)
   '''
   m5='''
   -----------------------------------------------------------
   |                                                         |
   |   Menu :                                                |
   |                                                         |
   |   + ~[1]~ Metasploit                         +          |
   |   + ~[2]~ A-Rat                              +          |
   |   + ~[3]~ DDOS                               +          |
   |   + ~[4]~ Webdav                             +          |
   |   + ~[5]~ Trace IP                           +          |
   |                                                         |
   |                                                         |
   |   + ~[x]~ Exit                               +          |
   |                                                         |
   |__________________________     __________________________|
              ________________|___|________________
             (_____________________________________)
   '''
   os.system ("clear")
   print (lcy)
   os.system ("clear")
   print (m1)
   time.sleep(1)
   os.system ("clear")
   print (m2)
   time.sleep(1)
   os.system ("clear")
   print (m3)
   time.sleep(1)
   os.system ("clear")
   print (m4)
   time.sleep(1)
   os.system ("clear")
   print (m5)
   time.sleep(1)
   print (lpp)
   slc=input ("root@Mr.Squidy ~#: ")
   if slc=="1" or slc=="01":
      os.system ("pkg update && pkg upgrade;apkg install unstable-repo;pkg install metasploit")
   elif slc=="2" or slc=="02":
        os.system ("apt update && apt upgrade;apt install python;apt install python2;apt install git;git clone https://github.com/Xi4u7/A-Rat")
   elif slc=="3" or slc=="03":
        os.system ("apt update;apt upgrade;apt install python;apt install git;git clone https://github.com/cyweb/hammer")
        print (lyl,"To Use >> Open folder hammer >> python hammer.py [IP TARGET] -p 80 -t 135")
   elif slc=="4" or slc=="04":
        os.system ("apt update && apt upgrade;apt install python2;pip2 install urllib3 chardet certifi idna requests;apt install openssl curl;pkg install libcurl;mkdir webdav;cd webdav;apt install wget;wget https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR webdav.py;chmod 777 webdav.py")
   elif slc=="5" or slc=="05":
        os.system ("apt update;apt upgrade;apt install git;apt install python;git clone https://ITermSec/ITU")
   elif slc=="x" or slc=="X":
        os.system ("exit")
   else:
        time.sleep(1)
        print (lrd,"ERROR : Wrong Input...!!!")

elif mn=="2" or mn=="02":
     os.system ("pkg update && pkg upgrade;apkg install unstable-repo;pkg install metasploit")
     os.system ("apt update && apt upgrade;apt install python;apt install python2;apt install git;git clone https://github.com/Xi4u7/A-Rat")
     os.system ("apt update;apt upgrade;apt install python;apt install git;git clone https://github.com/cyweb/hammer")
     os.system ("apt update && apt upgrade;apt install python2;pip2 install urllib3 chardet certifi idna requests;apt install openssl curl;pkg install libcurl;mkdir webdav;cd webdav;apt install wget;wget https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR webdav.py;chmod 777 webdav.py")
     os.system ("apt update;apt upgrade;apt install git;apt install python;git clone https://ITermSec/ITU")

elif mn=="3" or mn=="03":
     print (lyl,"Nick Name : mr.squidy")
     print (lcy,"Team : Garuda Team Commando")
     print (lgr,"Github : https://github.com/5qu1dy")
     print (lrd,"Contact : +6281393175636")
     time.sleep(1)

elif mn=="4" or mn=="04":
     os.system ("exit")

else:
     print (lrd,"Error : Wrong Input...!!!")
