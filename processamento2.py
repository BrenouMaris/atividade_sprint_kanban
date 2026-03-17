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

def gerar_relatorio(resultados, top_student):
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== RELATÓRIO DE DESEMPENHO ACADÊMICO ===\n\n")
        
        for nome, media, status in resultados:
            if media is not None:
                arquivo.write(f"Aluno: {nome} | Média: {media} | Situação: {status}\n")
            else:
                arquivo.write(f"Aluno: {nome} | Situação: {status}\n")
                
        arquivo.write("\n=== DESTAQUE ===\n")
        arquivo.write(f"Top Student: {top_student['nome']} com média {round(top_student['media'], 2)}\n")