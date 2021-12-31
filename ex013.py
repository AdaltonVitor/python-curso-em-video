   #recebendo a largur da parede em m2
L = float(input('digite a largura da sua parede : '))
   #recebendo altura da pparede em m2
A = float(input('digite a altura da sua parede :'))
   #rebendo o rendimemto da tinta em L por m2
R = float(input('digite o rendimento da tinta :'))
   #calculando o comprimento da parede
At =(L * A)
   #calculando o total gasto de tinta
Tt = (At / R)
print(' a sua parede mede{} m2'.format(At))
print(' voce precisa de {}L de tinta'.format(Tt))
