def hoststrings(cluster,servertype,min,max):
    serverlist = []   #it will create expty list
    for x in range(min,max):
        serverlist.append(cluster + servertype + str(x) + ".webex.com")
        print("retuned element : " ,serverlist)
    return serverlist  #return means it will kill the program and exit

hosts = hoststrings("abt1","wapi",1,10)
print(hosts)
