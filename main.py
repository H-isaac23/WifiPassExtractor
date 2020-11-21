import subprocess

#read the file number
#filenumber = open('filenumber.txt', 'r')
#fileNum = filenumber.readline()[-1]

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
f = open('Passwords.txt', 'w+')
#print(fileNum)
#filenumber.close()

# add the number
#filenumber = open('filenumber.txt', 'a+')
#filenumber.write(str(int(fileNum) + 1))
#filenumber.close()

for wifi in wifis:
    password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    password = [line.split(':')[1][1:-1] for line in password if "Key Content" in line]
    f.write('Wifi = {0}, Password = {1}\n'.format(wifi, password))
    print('Wifi = {0}, Password = {1}'.format(wifi, password))

#f.close()