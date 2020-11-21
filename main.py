import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
filename = subprocess.check_output(['whoami']).decode('utf-8').split('\\')
f = open('{0}- {1}.txt'.format(filename[0], filename[1][0:-2]), 'w+')

for wifi in wifis:
    password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    password = [line.split(':')[1][1:-1] for line in password if "Key Content" in line]
    f.write('Wifi = {0}, Password = {1}\n'.format(wifi, password))
    print('Wifi = {0}, Password = {1}'.format(wifi, password))
f.close()