def lasit_datni():
    try:
        with open('maize.txt','r',encoding='utf8')as f:
            read=f.read()
            print(read)
            
            

    except FileNotFoundError:
        print("Datne nav atrasta")
    
    except SystemError:
        print("Ievadi tikai burtus")

if __name__=="__main__":
    lasit_datni()