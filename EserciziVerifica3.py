# Es 3:  Andare a creare una funzioni che si occupi di salvare 
# i dati dell'utente, andare a creare una funzione che si occupi di fare il login dell'utente,
# Andare a creare un funzioni che modifichi i dati dell'utente solo se questi sono già 
# stati creati  / salvati e solo dopo il login.  Andare a creare un menu che concateni le
# tre funzioni precedenti e permetta di ripetere il ciclo a più utenti diversi.

    
    
def login(username, password):
    username1 = "maxdl"
    password1 = "password"
    list = {
        username1 : "",
        password1 : ""
    }
    
    if username == username1 and password == password1:
        print("Benvenuto nel sistema")
        list[username1] = username
        list[password1] = password1
     
    return list


def modifica_dati():
    if login():
        inp = input("Vuoi cambiare la password")
        inp1 = input("Vuoi cambiare l'username")
    
    if(inp == "si"):
        
        
        
 
 
 
 
     
     
     
     
     
     
