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
          
    comparisonChoice = input("What do you you want to configure? \n| + A loopback address (1) \n| + A routing protocol (2) \n| + A vlan (3) \n")
    
    if comparisonChoice == "1":
        print("\n+ Configuring loopback\n")
        loopbackChoice = input("Which loopback address do you want to configure? (e.g. 1)\n")
        loopbackCommands = ['int loopback '+loopbackChoice, 'ip address 10.10.10.10 255.255.255.0', 'no shut']
        session.send_config_set(loopbackCommands)
        print("\n+ Configured loopback\n")
    elif comparisonChoice == "2":
        protocolChoice = input("| Which routing protocol do you want to configure? \n| + Configure OSPF (1) \n| + Configure EIGRP (2) \n| + Configure RIP (3) \n")]
        if protocolChoice == "1":
            print("\n+ Configuring OSPF\n")
            idChoice = choice("Which OSPF process ID do you want to use? ")
            areaChoice = choice("Which OSPF area do you want to use? (0)")
            ospfCommands = ['router ospf '+idChoice, 'network 10.0.0.0 0.255.255.255 area '+areaChoice, 'exit']
            session.send_config_set(ospfCommands)
            print("\n+ Configured OSPF\n")
        elif protocolChoice == "2":
            print("\n+ Configuring EIGRP\n")
            eigrpCommands = ['router eigrp 20', 'network 10.0.0.0 0.0.0.255', 'exit']
            session.send_config_set(eigrpCommands)
            print("\n+ Configured EIGRP\n")
        elif protocolChoice == "3":
            print("\n+ Configuring RIP\n")
            ripCommands = ['router rip', 'network 10.0.0.0', 'exit']
            session.send_config_set(ripCommands)
            print("\n+ Configured RIP\n")
        else:
            exit()
    elif choice == "3":
        vlanChoice = input("Which vlan # do you want to configure? ")
        vlanCommands = ['vlan '+vlanChoice, 'name PRNE', 'ip address 192.168.10.10 255.255.255.0']
        deviceCheck = input("Are you connected to a switch? (y/n)")
        if deviceCheck.lower() == "y":
            print("\n+ Configuring VLAN\n")
            session.send_config_set(vlanCommands)
            print("\n+ Configured VLAN\n")
        elif deviceCheck.lower() == "n":
            print("| Closing existing SSH connection")
            session.quit()
            connectionInfo["host"] = input("Enter switch IP address: ")
            connectionInfo["password"] = getpass.getpass("Enter decive password: ")
            connectionInfo["secret"] = getpass.getpass("Enter device secret: ")

            session = netmiko.ConnectionHandler(**connectionInfo)
            session.enable()
            
            print("\n+ Configuring VLAN\n")
            session.send_config_set(vlanCommands)
            print("\n+ Configured VLAN\n")
        else:
            exit()
    else:
else:
    exit()
