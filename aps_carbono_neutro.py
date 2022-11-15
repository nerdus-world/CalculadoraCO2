typesList=[str("\n-Combustível \n-Gás de Cozinha \n-Eletricidade"), str("\n1-Gasolina; \n2-Diesel; \n3-Etanol; \n4-GNV")]
emissao=[]
print("Seja bem-vindo à Calculadora de CO2!", typesList[0])
tipo= str(input("Escolha primeiramente o tipo de cálculo:")).upper()
while tipo!='0':
  if tipo=='COMBUSTIVEL' or tipo=='COMBUSTÍVEL':
    print("Agora, o combustível utilizado!", typesList[1])
    combust=int(input("Digite o tipo:"))
    qtCombust=float(input("Digite a quantidade (em litros) gasta por mês:"))
    if combust==1:
      calcCombust= qtCombust*0.82*0.75*3.7
      #Cálculo baseado no site Lastrop, onde 1 litro de combustível equivale a qt_Litros*densidade_do_Combustivel*índice_transformação_CO2
      emissao.append(calcCombust)
      print("Foram emitidos cerca de", calcCombust,"kg de CO2 com gasolina.")
    elif combust==2:
      calcCombust= qtCombust*0.83*3.7
      emissao.append(calcCombust)
      print("Foram emitidos cerca de",calcCombust,"kg de CO2 com diesel.")
    elif combust==3:
      calcCombust= qtCombust*0.75*3.7
      emissao.append(calcCombust)
      print("Foram emitidos cerca de",calcCombust,"kg de CO2 com etanol.")
    else:
      calcCombust= qtCombust*0.76*3.7   
  elif tipo=='GAS DE COZINHA' or tipo=='GÁS DE COZINHA' or tipo=='GAS' or tipo=='GÁS':
    qtGas=float(input("Digite a quantidade de kg de gás usados por mês"))
    calcGas= qtGas*35.89
    emissao.append(calcGas)
    print("Foram emitidos cerca de", calcGas, "kg de CO2 com gás de cozinha. \nSão cerca de", round(calcGas*12/1000), "toneladas por ano.")
    #O cálculo foi baseado no site SOS Amazônia, onde 1kg de gás equivale a cerca de 35,89kg de CO2
  elif tipo=='ELETRICIDADE':
    convertKWh= str(input("Sabe a quantidade, em KWh, gasta por mês? (S para 'sim' e N para 'não')")).upper()
    if convertKWh=='S':
      qtKWh= float(input("Digite a quantidade de energia elétrica (em KW/h) gasta por mês:"))
      calcEletri= qtKWh*0.0125
      #Cálculo baseado no do site SOS Amazônia, onde 1KWh equivale a 0,0125kg de CO2
      emissao.append(calcEletri)
      print("Foram emitidos cerca de", round(calcEletri),"kg de CO2 com energia elétrica. \nSão cerca de",round(calcEletri*12/1000), "toneladas anuais")
    else:
      valorConta= float(input("Digite o valor, em R$, da conta de energia do mês:"))
      qtKWh= valorConta*1.79
      calcEletri= qtKWh*0.0125
      #Aqui, o cálculo foi baseado no valor do KWh em R$.
      emissao.append(calcEletri)
      print("Foram emitidos cerca de ",round(calcEletri),"kg de CO2 com energia elétrica. \nSão cerca de" ,calcEletri*12/1000, "toneladas anuais")
  else:
    print(typesList[0]) 
  tipo= str(input("Escolha um tipo de cálculo. Digite 0 para finalizar o cálculo:")).upper()
emissaoTotal= float(sum(emissao))
arvoreTotal= float(round(emissaoTotal*7.14)) #de acordo com estimativa, 7.14 árvores são capazes de sequestrar 1 tonelada de CO2 em seus primeiros 20 anos
solarTotal= int(qtKWh/40.8) #valor retirado de uma média de 1 painél de 340W, onde Energia= 340*5*(1-0.20)= 1,36kWh (multiplicado pelos 30 dias do mês, dão 40.8kWh) 
print("Sua emissão total foi cerca de", round(emissaoTotal)/1000,"ton de CO2. \nCaso continue neste ritmo, serão", round(emissaoTotal/1000*12),"tonelada(s) por ano")
print("Para compensar, pode-se plantar cerca de", arvoreTotal, "árvores. \nOutras alternativas são a implantação de", solarTotal, "painéis solares. \nOu, ainda, programas de incentivo, descarte correto de resíduos, uso moderado de água e energia, etc.")

#GLOSSÁRIO
#arvoreTotal: variável que armazena a quantidade de árvores que devem ser plantadas
#convertKWh: variável para armazenar se a pessoa sabe o valor de KWh gastos ou não
#combust: variável que armazena o tipo de combustível selecionado
#calcCombust;calcEletri;calcGas: variáveis que armazenam o cálculo de emissão de carbono em kg
#emissao[]: lista que armazena as quantidades de emissão em kg
#emissaoTotal: variável final que soma todas as emissões da lista emissao[]
#qtCombust; qtKWh; qtGas: armazenam as quantidades de cada aspecto (por exemplo, qtCombust salva a quantidade em litros de combustível usado)
#solarTotal: variável que armazena a quantidade de painéis solares que podem ser instalados.
#tipo: variável que armazena o tipo de cálculo selecionado e que controla o laço
#typesList: lista com as opções possíveis dentro da calculadora