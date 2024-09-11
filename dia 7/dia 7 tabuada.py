def gerar_tabuada(número):
    print(f"Tabuada do {número}")
    for i in range(1, 11 ):
          resultado = número * i
          print(f"{número} x {i} = {resultado}") 

 # Solicita ao usuário que insira um número 

número = int(input("Digite um número para gerar a tabuada: ")) 

# Chamar a função para gerar a tabuada

gerar_tabuada(número) 
         
     
    