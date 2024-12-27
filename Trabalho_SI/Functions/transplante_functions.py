import math

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

    print('Possíveis Recetores: ')
    for recetor in recetores:
        if recetor.get_orgao_atribuido()==False:
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



def determinar_recetor_transporte(recetores_compativeis, orgao_recebido, recetores_dic, hospitais_dic, transportes_dic):
    # verificar se algum recetor é emergencia
    for recetor_em_causa in recetores_compativeis:
        # Verificar se o hospital do recetor tem vagas/salas
        hospital_jid = None
        for jid_hospital, recetores in recetores_dic.items():
            if recetor_em_causa in recetores:
                hospital_jid = jid_hospital
                break

        if hospital_jid is None:
            print(f"Hospital do recetor {recetor_em_causa.get_jid_recetor()} não encontrado.")
            continue

        # Verificar disponibilidade de salas e equipas médicas no hospital
        hospital = hospitais_dic.get(hospital_jid)
        if not hospital:
            print(f"Informações do hospital {hospital_jid} não encontradas.")
            continue

        if hospital.salas > 0 and hospital.equipasMedicas > 0:
            print(f"Hospital {hospital_jid} tem recursos disponíveis (salas: {hospital.salas}, equipas médicas: {hospital.equipasMedicas}).\n Avaliando transporte...")

            # Verificar se o recetor é emergência
            if recetor_em_causa.urgencia == 'Emergencia':
                heli = transportes_dic.get('transporte_heli0@laptop-hjqmpgkj')
                if heli and heli.get_disponibilidade():

                    print("Helicópetro irá realizar o transporte do orgão.")
                    return( {'recetor_selecionado': recetor_em_causa, 'transporte': 'transporte_heli0@laptop-hjqmpgkj'} )

                else:
                    print(
                        "Helicóptero não está disponível. Outro transporte será avaliado.")  # tenta selecionar outro transporte
                    transporte_selecionado_jid= selecionar_transporte(recetor_em_causa, orgao_recebido, hospital, transportes_dic)

                    if transporte_selecionado_jid==False:
                        print(
                            f"Recetor {recetor_em_causa.get_jid_recetor()} é de emergência, mas não tem transporte. Próximo recetor será avaliado.") #passa para o próximo recetor
                    else:
                        print(
                            f"Foi selecionado o transporte {transportes_dic[transporte_selecionado_jid].get_tipo_transporte()} ao invés do Helicópetro, para transportar o orgão ao Recetor {recetor_em_causa.get_jid_recetor()}")
                        return( {'recetor_selecionado': recetor_em_causa, 'transporte': transporte_selecionado_jid} )


            else: #para Recetores não Emergencia
                transporte_selecionado_jid = selecionar_transporte(recetor_em_causa, orgao_recebido, hospital, transportes_dic)
                if transporte_selecionado_jid == False:
                    print(
                        f"Recetor {recetor_em_causa.get_jid_recetor()}, não tem transporte capaz de lhe entregar o orgão atempadamente. Próximo recetor será avaliado.")  # passa para o próximo recetor
                else:
                    print(
                        f"Foi selecionado o transporte {transportes_dic[transporte_selecionado_jid].get_tipo_transporte()}, para transportar o orgão ao Recetor {recetor_em_causa.get_jid_recetor()}.")
                    return ({'recetor_selecionado': recetor_em_causa, 'transporte': transporte_selecionado_jid})

        else:
            print(
                f"Hospital {hospital_jid}, onde se encontra o Recetor {recetor_em_causa.get_jid_recetor()}, não tem recursos suficientes (salas: {hospital.salas}, equipas médicas: {hospital.equipasMedicas}). Próximo recetor será avaliado.")

    print("Não existe nenhum recetor compatível para este orgão dentro de uma distância viável.")







def selecionar_transporte(recetor, orgao_recebido, hospital, transportes_dic):
    orgao_x = orgao_recebido.get_x()
    orgao_y = orgao_recebido.get_y()
    hospital_x = hospital.get_coordenada_x()
    hospital_y = hospital.get_coordenada_y()
    print(f"Validade do órgão: {orgao_recebido.get_validade()} km")

    urgencia=recetor.get_urgencia()

    # Calcular a distância entre o órgão e o hospital
    distancia_orgao_hospital = math.ceil(math.sqrt((orgao_x - hospital_x) ** 2 + (orgao_y - hospital_y) ** 2))
    print(f"Distância entre o órgão e o hospital: {distancia_orgao_hospital} km")

    # Inicializar variáveis para transporte terrestre
    transporte_mais_proximo = None
    jid_transporte_mais_proximo = None
    distancia_orgao_transporte = float('inf')

    # Variáveis para transporte de helicóptero
    helicopetro_disponivel = None

    # Selecionar o transporte mais próximo ao órgão
    for transporte_jid, transporte in transportes_dic.items():
        if transporte.get_disponibilidade():
            transporte_x = transporte.get_x()
            transporte_y = transporte.get_y()
            transporte_distancia = math.ceil(math.sqrt((orgao_x - transporte_x) ** 2 + (orgao_y - transporte_y) ** 2))

            if transporte.get_tipo_transporte() == "Helicóptero":  # Identificar helicóptero disponível
                helicopetro_disponivel = transporte_jid

            # Atualizar se este transporte for terrestre e o mais próximo encontrado
            elif transporte_distancia < distancia_orgao_transporte:
                distancia_orgao_transporte = transporte_distancia
                transporte_mais_proximo = transporte
                jid_transporte_mais_proximo = transporte_jid

    # Avaliar transporte terrestre mais próximo
    if transporte_mais_proximo:

        distancia_total = distancia_orgao_transporte + distancia_orgao_hospital
        print(f"Distância total a percorrer {distancia_total} km. Validade do órgão: {orgao_recebido.get_validade()} km")

        if distancia_total <= orgao_recebido.get_validade():
            print(
                f"Transporte terrestre selecionado: {transporte_mais_proximo.get_tipo_transporte()}. Distância do transporte até ao órgão: {distancia_orgao_transporte} km")
            return jid_transporte_mais_proximo  # Retornar transporte terrestre mais próximo

        # Se não houver transporte terrestre viável, verificar helicóptero
        if distancia_total > orgao_recebido.get_validade() and helicopetro_disponivel and (urgencia=="Muito Urgente"):
            print(f"Distância excede a validade do órgão. Medida de contingência ativada, utiliza-se o helicóptero {helicopetro_disponivel} para transporte do orgão.")
            return helicopetro_disponivel

    elif transporte_mais_proximo is None and helicopetro_disponivel and urgencia== "Muito Urgente":
            print(f"Não existe nenhum veículo disponível. Medida de contingência ativada, utiliza-se o helicóptero {helicopetro_disponivel} para transporte do orgão.")
            return helicopetro_disponivel

    print("Nenhum transporte disponível ou adequado encontrado.")
    return False


