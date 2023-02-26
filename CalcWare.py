import sys
import time
print("""\


 .d8888b.           888          888       888                          
d88P  Y88b          888          888   o   888                          
888    888          888          888  d8b  888                          
888         8888b.  888  .d8888b 888 d888b 888  8888b.  888d888 .d88b.  
888            "88b 888 d88P"    888d88888b888     "88b 888P"  d8P  Y8b 
888    888 .d888888 888 888      88888P Y88888 .d888888 888    88888888 
Y88b  d88P 888  888 888 Y88b.    8888P   Y8888 888  888 888    Y8b.     
 "Y8888P"  "Y888888 888  "Y8888P 888P     Y888 "Y888888 888     "Y8888  
                                                                  
                                          


             """)
print ("VERSION 2.5 beta")
time.sleep (1)
print ("I am NOT responsible for ANY DAMAGE caused to your calculator AT ALL.")
print ("This software is free and open-source,if you got it as a paid product,or as a part of a bundle - THIS IS A SCAM,GET YOUR MONEY BACK")
time.sleep (2)
print ("Waiting for device")
time.sleep (1)
print ("Found!")
time.sleep (1)
print ("Installing CalcWare")
loading= "LOADING THE FIRMWARE. DO NOT DICONNECT THE DEVICE\n"
bar = "[==========]"
print(loading)
for c in bar:
    time.sleep(0.3)
    sys.stdout.write(c)
    sys.stdout.flush()
    
print ("Succesfully installed CalcWare!")