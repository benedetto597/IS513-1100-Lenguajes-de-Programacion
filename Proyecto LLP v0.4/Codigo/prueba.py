def aaa():

    diccionary= {
        "python":{"tipos de datos":"no","si":"no", "sino":"nosi", "no":"si"}, 
        "java":{"this":"", "si":""}
    }
    key = diccionary.keys()
    #print(key)
    values = diccionary.values
    #print(values)
    
    for i in diccionary:
        print("\n"+i+"\n"+"*"*80)
        #print (diccionary[i])
        for j in diccionary[i]:
            print(j)
            print("\t"+diccionary[i][j])
            
   
aaa()