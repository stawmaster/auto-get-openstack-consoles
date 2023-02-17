import subprocess
import json

# subprocess.run('source ./kolla/virtualenv/bin/activate', shell=True)


# subprocess.run('source /etc/kolla/admin-openrc.sh', shell=True)


result = subprocess.run("openstack server list -c Name -c Image -c Networks".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)


text= result.stdout.decode('utf-8').split('\n')
del text[:3]
del text[-1]
del text[-1]

servers=[]
for i in text :
    servers.append(i.split('|'))

for i in servers:
    del i[0]
    del i[-1]
    print(i)
    print('++++++++++++++++++++')

serverdicts=[]

for serv in servers:
    serverdicts.append({'name':serv[0],'IPs':serv[1],'Image':serv[2]})

for i in serverdicts:
    print(i)
    print('++++++++++++++++++++')



protocols=['--novnc','--rdp','--serial','--spice']

outs=[]

for server in serverdicts:
        consolesout = subprocess.run(("openstack console url show"+server['name']).split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outs.append(consolesout.stdout.decode('utf-8').split('\n'))

for con in outs:
    for i in con:
        print(i)
        print('++++++++++++++++++++++++')





with open("data.json", "w") as file:
    json.dump(data, file)