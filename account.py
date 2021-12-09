def all_sallaries(filename):
    file=open(filename,'r')
    totall=0
    for sal in file:
        sal = (sal.replace('\n', '')).split(',')
        totall=totall+int(sal[4])
    file.close()
    return totall
