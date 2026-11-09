

def pergunta_Numero():

    valido = False

    while valido == False:

        numero = int(input('Digite um número para verififcar se ele é primo \n'))

        if numero >= 1:
            
            valido = True

    return numero

def E_Par(x:int):

    if x % 2 == 0:

        return True
    
    else:

        return False
    
def Verifica_Primo_Par(X : int):
   
    if X == 2:

        return True 
    
    else:

        return False
    
def verifica_Primo_Impar(X:int):


      
    if X == 1:
            
        return False 

    else:

        Limite = X // 2 

        while Limite >= 3:


            if X % Limite == 0:
                return False

            Limite -= 1

        
    return True 
 


def Imprime_Mensagem(x:bool,Numero : int):
    if x:
        print(f'O número {Numero} é um número primo') 
    else:
        print(f'O número {Numero} Não é um número primo')      
        
                                  

def Fluxo():



    Numero_Usuario = pergunta_Numero()
    Numero_Par = E_Par(x = Numero_Usuario)
    


    if Numero_Par == True:
        Primo = Verifica_Primo_Par(X = Numero_Usuario)
    else:
        Primo = verifica_Primo_Impar(X = Numero_Usuario)   
        

    Imprime_Mensagem(x = Primo ,Numero = Numero_Usuario)    

    return Primo

def Main():

    Parar = False
    QuantPrimos = 0

    while Parar == False:

        Primo = Fluxo()
        print('Deseja Continuar a verificar primos?')
        Resposta = input('Digite sim para continuar a rodar o programa \n')
        if Resposta.strip().lower() == 'sim':
            Parar = False
        else:
            Parar = True    

        if Primo:
            QuantPrimos += 1


    print(f'Voce achou {QuantPrimos} Números Primos ')


if __name__ == '__main__':
    Main()


   






      


