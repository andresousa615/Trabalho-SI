def determinar_recetores_compativeis(orgao, recetores):
    """
    Determina os recetores compatíveis com um dado órgão, com base no tipo de órgão, compatibilidade sanguínea e urgência.

    :param orgao: Objeto Orgao.
    :param recetores: Lista de objetos Recetor.
    :return: Lista de recetores compatíveis ordenados por prioridade (urgência).
    """
    # Mapeamento de compatibilidade de sangue (dadores universais, etc.)
    compatibilidade_sanguinea = {
        "O-": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],  # Doador universal
        "O+": ["O+", "A+", "B+", "AB+"],  # Doa apenas para positivos
        "A-": ["A-", "A+", "AB-", "AB+"],  # A- doa para A e AB
        "A+": ["A+", "AB+"],  # A+ doa apenas para positivos A e AB
        "B-": ["B-", "B+", "AB-", "AB+"],  # B- doa para B e AB
        "B+": ["B+", "AB+"],  # B+ doa apenas para positivos B e AB
        "AB-": ["AB-", "AB+"],  # AB- doa para AB
        "AB+": ["AB+"]  # Receptor universal
    }

    # Definição de prioridades de urgência
    prioridade = {"Emergencia": 1, "Muito Urgente": 2, "Medio Urgente": 3, "Pouco Urgente": 4}

    print(orgao)
    for recetor in recetores:
        print(recetor)

    # Filtrar recetores compatíveis
    recetores_compativeis = [
        recetor for recetor in recetores
        if recetor.nome_orgao == orgao.nome_orgao  # Tipo de órgão é o mesmo
        and recetor.sangue in compatibilidade_sanguinea.get(orgao.sangue, [])  # Sangue compatível
        and not recetor.orgao_atribuido  # Órgão ainda não foi atribuído
    ]

    # Ordenar por urgência
    recetores_compativeis.sort(key=lambda r: prioridade.get(r.urgencia, float('inf')))
    return recetores_compativeis
