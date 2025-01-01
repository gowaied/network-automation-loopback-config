from netmiko import ConnectHandler, NetMikoAuthenticationException,NetMikoTimeoutException
from getpass import getpass
import ipaddress

#Gather Credentials
username = input('Please, enter the username: ')
password = getpass('Please, enter the password: ')
secret = getpass('Please, enter the secret: ')

#Gather Target IPs
ip_list = []
print('Please, enter the target IPs one by one and write "done" when finish.')
while True:
    ip_add = input('Enter IP: ')
    if ip_add.strip().lower() == 'done':
        break
    try:
        ipaddress.IPv4Address(ip_add)
        ip_list.append(ip_add)
    except ipaddress.AddressValueError:
        print('Invalid IP address! Please, try again.')
    
#Gather Loopback IDs
loopback_id_list = []
print('Please, enter loopback ID one by one and write "done" when finish.')
while True:
    loopback_id = input('Enter ID: ')
    if loopback_id.strip().lower() == 'done':
        break
    if loopback_id.isdigit():
        loopback_id_list.append(loopback_id)
    else:
        print("Please, enter an integer numeric value.")

#Gather Loopback IPs
loopback_ip_list = []
while True:
    loopback_ip = input('Enter Loopback IP: ')
    if loopback_ip.strip().lower() == 'done':
        break
    try:
        ipaddress.IPv4Address(loopback_ip)
        loopback_ip_list.append(loopback_ip)
    except ipaddress.AddressValueError:
        print('Invalid IP address! Please, try again.')
if len(ip_list) != len(loopback_ip_list) or len(loopback_ip_list) != len(loopback_id_list):
    print('Error: The number of Target IPs , Loopback IPs , Loopback IDs must match.')
    exit()

#Define the Function
def config_loopback(username, password, secret, ip_list, loopback_id_list, loopback_ip_list ):
    for ip,loop_ip,loop_id in zip(ip_list,loopback_ip_list,loopback_id_list):
        device = {
             'device_type' : 'cisco_ios',
             'host' : ip,
             'username' : username,
             'password' : password,
             'secret' : secret
             }
        try:
            print(f'Connecting to {ip} host.....')
            net_connect = ConnectHandler(**device)
            net_connect.enable()
            net_connect.config_mode()
            commands = [f'int lo {loop_id}' , f'ip add {loop_ip} 255.255.255.255', f'no shutdown']
            output = net_connect.send_config_set(commands)
            print(output)
            verification = net_connect.send_command('sh ip int br')
            print(f'Loopback {loop_id} has been configured Successfully on host {ip}!')
            print(verification)
        except NetMikoAuthenticationException:
            print(f'Authentication failed for host {ip}. Please check the credentials.')
        except NetMikoTimeoutException:
            print(f'Timeout while connecting to hot {ip}. This host might be unreachable.')
        except Exception as e:
            print(f'Failed to configure {ip} device: {e}')

config_loopback(username, password, secret, ip_list, loopback_id_list, loopback_ip_list)
print("The Process is Done!")
input('Press Enter to close.....')