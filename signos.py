# Signos
print('Informar o signo conforme a data de nascimento.')

dia = input('Digite o dia do nascimento: ')
mes = input('Escreva o mês: ')

if not dia.isdigit():
    print("Por favor, digite uma data válida.")
else:
    dia = int(dia)
    mes = mes.lower()


    janeiro = dia >=1 and dia <= 20 and mes == 'janeiro'
    janeiro_2 = dia >=21 and dia <= 31 and mes == 'janeiro'
    fevereiro = dia >=1 and dia <= 18 and mes == 'fevereiro'
    fevereiro_2 = dia >=19 and dia <= 28 and mes == 'fevereiro'
    marco = dia >=1 and dia <= 20 and mes == 'março' 
    marco_2 = dia >=21 and dia <= 31 and mes == 'março'
    abril = dia >=1 and dia <= 20 and mes == 'abril'
    abril_2 = dia >=21 and dia <= 30 and mes == 'abril'
    maio = dia >=1 and dia <= 20 and mes == 'maio'
    maio_2 = dia >=21 and dia <= 31 and mes == 'maio'
    junho = dia >=1 and dia <= 20 and mes == 'junho'
    junho_2 = dia >=21 and dia <= 30 and mes == 'junho'
    julho = dia >=1 and dia <= 22 and mes == 'julho'
    julho_2 = dia >=23 and dia <= 31 and mes == 'julho'
    agosto = dia >=1 and dia <= 22 and mes == 'agosto'
    agosto_2 = dia >=23 and dia <= 31 and mes == 'agosto'
    setembro = dia >=1 and dia <= 22 and mes == 'setembro'
    setembro_2 = dia >=23 and dia <= 30 and mes == 'setembro'
    outubro = dia >=1 and dia <= 22 and mes  == 'outubro'
    outubro_2 = dia >=23 and dia <= 31 and mes == 'outubro'  
    novembro = dia >=1 and dia <= 21 and mes == 'novembro'
    novembro_2 = dia >=22 and dia <= 30 and mes == 'novembro'
    dezembro = dia >=1 and dia <= 21 and mes == 'dezembro'
    dezembro_2 = dia >=22 and dia <= 31 and mes == 'dezembro'
    

        # Áries
    if marco_2 or abril:
      print(f'{dia} de {mes}, Áries.')
      print('Lado Bom: Energetico, determinado, corajoso, líder natural.')
      print('Lado Ruim: Impulsivo, impaciente, competitivo em excesso.')

    # Touro
    elif abril_2 or maio:
      print(f'{dia} de {mes}, Touro.')
      print('Lado Bom: Leal, paciente, prático, confiável.')
      print('Lado Ruim: Teimoso, indulgente, resistente a mudanças.')

    # Gêmeos
    elif maio_2 or junho:
      print(f'{dia} de {mes}, Gêmeos.')
      print('Lado Bom: Versátil, comunicativo, intelectual, adaptável.')
      print('Lado Ruim: Superficial, inconstante, disperso.')

    # Câncer
    elif junho_2 or julho:
      print(f'{dia} de {mes}, Câncer.')
      print('Lado Bom: Sensível, carinhoso, protetor, intuitivo.')
      print('Lado Ruim: Hiper sensível, manipulador emocional, reservado.')

    # Leão
    elif julho_2 or agosto:
      print(f'{dia} de {mes}, Leão.')
      print('Lado Bom: Carismático, generoso, criativo, líder.')
      print('Lado Ruim: Egocêntrico, autoritário, arrogante.')

    # Virgem
    elif agosto_2 or setembro:
      print(f'{dia} de {mes}, Virgem.')
      print('Lado Bom: Analítico, prático, organizado, atencioso.')
      print('Lado Ruim: Crítico em excesso, preocupado demais, perfeccionista.')

    # Libra
    elif setembro_2 or outubro:
      print(f'{dia} de {mes}, Libra.')
      print('Lado Bom: Diplomático, justo, charmoso, sociável.')
      print('Lado Ruim: Indeciso, evita conflitos, busca aprovação.')

    # Escorpião
    elif outubro_2 or novembro:
      print(f'{dia} de {mes}, Escorpião.')
      print('Lado Bom: Determinado, apaixonado, corajoso, leal.')
      print('Lado Ruim: Ciumento, desconfiado, intenso demais.')

    # Sagitário
    elif novembro_2 or dezembro:
      print(f'{dia} de {mes}, Sagitário.')
      print('Lado Bom: Aventureiro, otimista, honesto, entusiasta.')
      print('Lado Ruim: Impulsivo, imprudente, insensível.')

    # Capricórnio
    elif dezembro_2 or janeiro:
      print(f'{dia} de {mes}, Capricórnio.')
      print('Lado Bom: Ambicioso, disciplinado, responsável, realista.')
      print('Lado Ruim: Cético, reservado emocionalmente, pessimista.')

    # Aquário
    elif janeiro_2 or fevereiro:
      print(f'{dia} de {mes}, Aquário.')
      print('Lado Bom: Inovador, progressista, amigável, humanitário.')
      print('Lado Ruim: Distante emocionalmente, teimoso em suas ideias.')

    # Peixes
    elif fevereiro_2 or marco:
      print(f'{dia} de {mes}, Peixes.')
      print('Lado Bom: Empático, intuitivo, gentil, criativo.')
      print('Lado Ruim: Tendência a se vitimizar, escapista, indeciso.')

    else:
        print(f'Essa data: {dia} de {mes} não existe, por favor digite uma data válida.')
