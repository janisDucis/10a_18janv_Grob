def lasit_datni():

    try:
        ziema=['Vasara','Ziema','rudens','pavasaris']
        with open ('sakta.txt','w',encoding='utf8')as f:
            f.write("\n".join(ziema))
        with open ('sakta.txt','r',encoding='utf8')as dd:
            line=dd.readline(3)
            print(line)




    except FileNotFoundError:
        print("Datne nav atrasta")
    
    except SystemError:
        print("Ievadi tikai burtus")

if __name__=="__main__":
    lasit_datni()