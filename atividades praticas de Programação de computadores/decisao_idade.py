# Variavel criada para pegar o valor da idade do usuario via console
idade = int(input("Digite sua idade: "))
# Estrutura de decisão 
if idade > 18 :
    # Print caso sua idade seja 18 ou maior que 18
    print("você é maior de idade! ") 
elif idade == 18:
    #Print caso a pessoa tenha exatamente 18 anos de idade
    print("Parabens você agora é maior de idade")
else:
    #Print caso sua idade não é maior ou igual a 18
    print("você é menor de idade! ")
    