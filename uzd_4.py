ievade=input("Ievadi faila nosaukumu un formātu: ")

def lasit_datni():

    try:
        atzime=['10','5','1']
        with open (ievade,'w',encoding='utf8')as ff:
            ff.write('\n'.join(atzime))
            


    except FileNotFoundError:
        print("Datne nav atrasta")
    
    except SystemError:
        print("Ievadi tikai burtus")

if __name__=="__main__":
    lasit_datni()