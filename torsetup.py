#! /bin/python3

import os
import time
import subprocess
logo = """                                                                              
                                                 #    .                         
 .******************************               #  ##                            
 ********************************           ######                              
 ********************************          #####                                
 ********************************         ####                                  
 ********************************        @@                                     
          **************                 @@@*                         **********
          *************                 @@@@ *                     *************
          *************              &@@@/@ @ ***                ***************
          *************           @@@@@@ @@@@@@******          *****************
          *************        @@@@@@ @@@@@@@@@@*******        *****************
          *************       @@@@ @@@@@@ @ @@ @ ********      ************     
          *************      @@@ @@@@@@@@@@@ @@@ ********      ************     
          *************      @@ @@@@ @@@@@@@@ @  *********     ************     
          *************      @@@@@@@@@@@@@@@@@@  ********      ************     
          *************       @@ @@@@@@@@@@@.@@/ ********      ************     
          *************        @@@@ @@@@@@@@(@   ******        ************     
          *************           @(@ @@@@@(@@  *****          ************     
           ************                 .     *                ************     

"""

while True:
    os.system("clear")
    print(logo)
    choose=int(input("""
choose an option :
1)set up proxychains and tor service
2)start tor service
3)set up proxychains.conf
4)open an app or module using proxychains
5)suffle proxy
6)about
7)exit
"""))
    if choose == 1 :
        os.system("sudo apt install tor")
        os.system("sudo apt install proxychains")
        print("tor and proxychains installed succsesfully \n")
    elif choose == 2:
        os.system("sudo service tor stop")
        os.system("sudo service tor start")
        os.system("sudo service tor reload")
        print("tor service started")
    elif choose == 3:
            os.system("sudo rm /etc/proxychains.conf")
            os.system("sudo cp proxychains.conf /etc")
    elif choose==4:
        Subprogram = subprocess.Popen(['qterminal', '-e', 'python ./start.py'], stdout=subprocess.PIPE)
    elif choose ==5 :
        Subprogram = subprocess.Popen(['qterminal', '-e', 'python ./suffel.py'], stdout=subprocess.PIPE)
    elif choose == 6:
        os.system("clear")
        print(f"""{logo}
        this script will work with proxychains on tor service at first make sure to update and upgrade your debian os
        after that setup (install) tor and proxychains using first option of script
        then set up proxychains config using second option 
        then start the tor service using third option
        in the forth option of script you could select the app or module you want to use with tor service for example firefox
        the fifth option is optional but if you want to stay anonymous you better to use it and set the number 0 for non limit shuffle proxy 
        this script is coded by Arsham 
        email : arshamcode@proton.me

        
        """)
    elif choose ==7:
        os.system("sudo service tor stop")
        input("tor srvice stoped press enter to exit")
        break
    else:
        print("wrong chooice\n")
    input("press enter for choose a new choice")