def validar_notas(notas):
    if not notas:
        return False
    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False
    return True

def processar_alunos(dados_alunos):
    resultados = []
    top_student = {"nome": "", "media": -1}
    
    for nome, notas in dados_alunos:
        if validar_notas(notas):
            media = sum(notas) / len(notas)
            status = "Recuperação" if media < 7.0 else "Aprovado"
            
            if media > top_student["media"]:
                top_student = {"nome": nome, "media": media}
                
            resultados.append((nome, round(media, 2), status))
        else:
            resultados.append((nome, None, "Dados Inválidos/Corrompidos"))
            
    return resultados, top_student