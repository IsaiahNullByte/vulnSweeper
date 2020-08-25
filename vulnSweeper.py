#pip install python-nmap
import nmap
import datetime

i = 0
portNum = input("[+] Please enter service port: ")
serviceVer = raw_input("\n\n[+] Please enter service version: ")
logPath = raw_input("\n\n[+] Please enter file path for logs of identified host: ")

nm = nmap.PortScannerAsync() 

timeStamp = print datetime.datetime.today()
filePath = "%s_%s-sweepLogs.txt" % (logPath,timeStamp)
f=open("%s" % filePath,mode="w+")
print "\n\n[+] Created log file -> %s" % filePath


def callback_result(host, scanResult): 
    for serviceVer in scanResult: 
        print "%s : Potential Vulnerability" % host 
        f=open("%s" % filePath,"a+")
        f.write("%s\r\n" % scanResult)
        print "[%s] Detected Total" % (i+1)
 

nm.scan(hosts='0.0.0.0/0',arguments='--exclude 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16 -sV -p "%s"' % portNum,callback=callback_result) 
while nm.still_scanning():
    verboseStamp = datetime.datetime.now()
    print "[+] Sweeping..       [%s]" % verboseStamp
    nm.wait(600)
