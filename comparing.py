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
connectionType = input("Do you want to connect? (y/n)") 

if connectionType.lower() == "y":
    connectionInfo["device_type"] = "cisco_ios"
    session = netmiko.ConnectionHandler(**connectionInfo)
    print("*** Connection Successful ***)
    session.enable()
          
    comparisonChoice = input("Do you want to compare running config and startup config (1) or running config with an existing backup (2)?")
    
    if comparisonChoice == "1":
          output = session.send_command('sh run')
          runFile = open("runfile.txt", "w")
          runfile.write(output)
          runfile.close()
          
          outputTwo = session.send_command('sh start')
          startFile = open("startfile.txt", "w")
          startFile.write(outputTwo)
          startFile.close()
          
          runFileForComparison = open("runfile.txt", "r")
          startFileForComparison = open("startfile.txt", "r")
          
          diffs = difflib.unified_diff(runFileForComparison.readlines(), startFileForComparison.readlines(), n=0)
          for diff in diffs:
                print(diff)
          print("Comparison Successsul")
          
    elif comparisonChoice == "2":
          output = session.send_command('sh run')
          runFile = open("runfile.txt", "w")
          runfile.write(output)
          runfile.close()
          
          runFileForComparison = open("runfile.txt", "r")
          localBackup = open("config-output.txt", "r")
          
          diffs = difflib.unified_diff(runFileForComparison.readlines(), localBackup.readlines(), n=0)
          for diff in diffs:
                print(diff)
    else:
          print("Option not found!")
          print("Please enter either option 1 or 2")
else:
    exit()
