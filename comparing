import netmiko
import getpass
import difflib

connectionInfo = {
    'device_type' : '',
    'host':'192.168.1.1',
    'username':'cisco',
    'password':'',
    'secret':''
}

print("*** Device connection script ***")
connectionInfo["password"] = getpass.getpass("Enter decive password: ")
connectionInfo["secret"] = getpass.getpass("Enter device secret: ")
connectionType = input("Do you want to connect via SSH (1) or Telnet(2)?")

if connectionType == "1":
    connectionInfo["device_type"] = "cisco_ios"
    session = netmiko.ConnectionHandler(**connectionInfo)
    print("*** Connection Successful ***)
    session.enable()
    output = session.send_command('sh run')
    outputTwo = session.send_command('sh start')
    
    runFile = open("runfile.txt", "w")
    runfile.write(output)
    runfile.close()
    
    startFile = open("startfile.txt", "w")
    startFile.write(outputTwo)
    startFile.close()
    
    runFileForComparison = open("runfile.txt", "r")
    startFileForComparison = open("startfile.txt", "r")
    
    diffs = difflib.unified_diff(runFileForComparison.readlines(), startFileForComparison.readlines(), n=0)
    
    #file = open("config-output- " + connectionInfo["host"] + ".txt", "w")
    #file.write(output)
    #file.close()
    print("*** Configuration Saved ***)
elif connectionType == "2":
    connectionInfo["device_type"] = "cisco_ios_telnet"
    session = netmiko.ConnectionHandler(**connectionInfo)
    print("*** Connection Successful ***)
    session.enable()
    print(session.send_command('sh ip int br'))
else:
    exit()
