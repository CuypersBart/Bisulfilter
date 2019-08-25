import os

coveragecut = 25
methylationperc = 0.8
mydir = "Path/To/CGmap"
filelist = []
#Choose between True or False
verbose=True

for myfile in os.listdir(mydir):
    if myfile.endswith("CGmap"):
        filelist.append(myfile)

os.chdir(mydir)

for selectfile in filelist:
    CG = 0.0
    CHG = 0.0
    CHH = 0.0
    CGall = 0.0
    CHGall = 0.0
    CHHall = 0.0
    CGmethylated = 0.0
    CHGmethylated = 0.0
    CHHmethylated = 0.0
    with open(selectfile) as myfile:
        for i in myfile:
            i = i.strip('\n').split('\t')
            if 'CG' in i[3]:
                CGall += 1
                if int(i[7]) > coveragecut:
                    CG += 1
                    if float(i[5]) > methylationperc:
                        CGmethylated += 1
                        if verbose == True:
                            print("\t".join([i[0],i[2],i[3]]))
            elif 'CHG' in i[3]:
                CHGall += 1
                if int(i[7]) > coveragecut:
                    CHG += 1
                    if float(i[5]) > methylationperc:
                        CHGmethylated += 1
                        if verbose == True:
                            print("\t".join([i[0],i[2],i[3]]))
            elif 'CHH' in i[3]:
                CHHall += 1
                if int(i[7]) > coveragecut:
                    CHH += 1
                    if float(i[5]) > methylationperc:
                        CHHmethylated += 1
                        if verbose == True:
                            print("\t".join([i[0],i[2],i[3]]))
    print("Summary:")
    print((CGmethylated / CG) * 50.0, end='\t')
    print(CGmethylated, end='\t')
    print(CG, end='\t')
    print(CGall, end='\t')
    print((CG/CGall)*100, end='\t')
    print((CHGmethylated/CHG)*50.0, end='\t')
    print(CHGmethylated, end='\t')
    print(CHG, end='\t')
    print(CHGall, end='\t')
    print((CHG/CHGall)*100, end='\t')
    print((CHHmethylated/CHH)*50.0, end='\t')
    print(CHHmethylated, end='\t')
    print(CHH, end='\t')
    print(CHHall, end='\t')
    print((CHH/CHHall)*100)