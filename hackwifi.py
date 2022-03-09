import subprocess
data=subprocess.check_output(['netsh','wlan','show','profiles'])
data= data.decode('utf-8').split('\n')
wifi_names=[]
for profile in data :
    if "ALL USER PROFILE" in profile:
        profile=profile.split(":")

        profile=profile[1]
        profile=profile[1:-1]

        wifi_names.append(profile)
print("{:<20}|       {:}\n".format('WI_FI Names','Passwords'))
for name in wifi_names:
    data=subprocess.check_output(['netsh','wlan','show','profiles',name,'key=clear'])
    data=data.decode('utf-8').split('\n')
    passwords=[]
    for passw in data:
        if "Key Content" in passw:
            password=passw.split(":")
            password=password[1]
            password=password[1:-1]
            password.append(password)

    try:
        print("{:<20}|     {:}".format(name, passwords[0]))

    except IndexError:
        print("{:<20}|      {:}".format(name,""))