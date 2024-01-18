ievade=input("ievadi savu vārdu: ")

def lasit_datni():

    try:
        with open ('desa.txt','w',encoding='utf8')as ff:
            ff.write (ievade)


    except FileNotFoundError:
        print("Datne nav atrasta")
    
    except SystemError:
        print("Ievadi tikai burtus")

if __name__=="__main__":
    lasit_datni()
        