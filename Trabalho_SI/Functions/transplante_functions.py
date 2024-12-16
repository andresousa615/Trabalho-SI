def determinar_recetores_compativeis(orgao, recetores):
    """
    Determina os recetores compatíveis com um dado órgão, com base no tipo de órgão, compatibilidade sanguínea e urgência.

    :param orgao: Objeto Orgao.
    :param recetores: Lista de objetos Recetor.
    :return: Lista de recetores compatíveis ordenados por prioridade (urgência).
    """
    # Mapeamento de compatibilidade de sangue (dadores universais, etc.)
    compatibilidade_sanguinea = {
        "O-": ["O-"],  # O- é o dador universal
        "O+": ["O-", "O+"],
        "A-": ["O-", "A-"],
        "A+": ["O-", "O+", "A-", "A+"],
        "B-": ["O-", "B-"],
        "B+": ["O-", "O+", "B-", "B+"],
        "AB-": ["O-", "A-", "B-", "AB-"],
        "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]  # AB+ é o recetor universal
    }

    # Definição de prioridades de urgência
    prioridade = {"Alta": 1, "Média": 2, "Baixa": 3, "Pouco Urgente": 4}

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
