def algoritmo(x):
     grau_de_convergencia = float(input("Digite o grau de convergência:"))
     limite =int(input("Digite o número máximo de interações:"))
     funcao = x**3-5*(x**2)+x+3
     derivada = 3*(x**2)-10*x + 1
     i=1
     print(i, x, funcao)
     while funcao >= grau_de_convergencia or funcao <= -grau_de_convergencia or i==limite+1:
        x = x - funcao/derivada
        funcao = x**3-5*(x**2)+x+3
        derivada = 3*(x**2)-10*x + 1
        i = i+1
        print(i, x, funcao)
        
        
     
    
    
    
