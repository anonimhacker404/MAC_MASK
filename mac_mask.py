import subprocess
def mac_mask(interfeys,new_mac):
    print(interfeys+" ning Mac adresi o'zgaryapti "+new_mac+" ga ")
    subprocess.call(["ifconfig",interfeys,"down"])
    subprocess.call(["ifconfig",interfeys,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interfeys,"up"])
interfeys=input(" {●} INTERFEYS nomini kiriting > ")   
new_mac=input(" {●} Yangi Mac Adres kiriting > ")
mac_mask(interfeys,new_mac)