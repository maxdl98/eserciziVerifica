# Crea un sistema ripetibile che si occupi
# di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata.
# Deve poter stampare una lista singola o tutte. 
# Si deve ripetere X volte definite all'inizio dall'utente

def collocare(dato):
    lista1 = []
    lista2 = []
    lista3 = []

    if (type(dato) == str) or (type(dato) == int):
        lista1.append(dato)  
        print("il dato è stato inserito nella lista 1 ", dato)
        return lista1  
    if (type(dato) == bool) or (type(dato) == float) or (type(dato) == dict):
        lista2.append(dato)
        print("il dato è stato inserito nella lista 2" , dato)
        return lista2
    else:
        lista3.append(dato)
        print("il dato è stato inserito nella lista 3: " , dato)
        return lista3

 
 
 lis = [4,56,6]
collocare(lis)



   
   
    
    
    
    
     
     
     
     
 
 
 
 
 
     
     
     
     
     
     
