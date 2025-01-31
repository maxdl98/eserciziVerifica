# Es 2:  Andare a creare un sistema ripetibile che si occupa
# di gestire la lunghezza delle stringhe e salvarle, 
# l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga 
# della precedente, alla fine stamperà l'insieme delle stringhe date in input divise 
# da virgole e quante stringhe ha inserito.
# (1 punto)


def inserireStringa():
    precedente = ""  
    stringhe = []  
    
    while True:
        testo = input("Inserisci una stringa: ")
        
        if len(testo) > len(precedente):
            stringhe.append(testo)  
            precedente = testo  
        else:
            print("Inserire una stringa di lunghezza superiore.")
            break  

    print("Numero di stringhe inserite:", len(stringhe))
    
    print("Le stringhe inserite sono:", ", ".join(stringhe))

inserireStringa()

    
    
    
     
     
     
     
 
 
 
 
 
     
     
     
     
     
     
