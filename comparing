import netmiko
import getpass

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
    file = open("config-output- " + connectionInfo["host"] + ".txt", "w")
    file.write(output)
    file.close()
    print("*** Configuration Saved ***)
elif connectionType == "2":
    connectionInfo["device_type"] = "cisco_ios_telnet"
    session = netmiko.ConnectionHandler(**connectionInfo)
    print("*** Connection Successful ***)
    session.enable()
    print(session.send_command('sh ip int br'))
else:
    exit()
