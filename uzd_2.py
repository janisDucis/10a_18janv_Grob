import csv
def lasit_datni():
    
    try:
        
        labs=['cilveks','masina,''planeta']
        with open ('labs.csv','r',encoding='utf8')as dd:
            dd.readline('\n'.join(labs))
            line=dd.readline(2)
            print(line)

    except FileNotFoundError:
        print("Datne nav atrasta")
    
    except SystemError:
        print("Ievadi tikai burtus")

if __name__=="__main__":
    lasit_datni()