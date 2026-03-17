import processamento

def main():
    alunos = [
        ("Ana", [8.5, 9.0, 7.5]),
        ("Bruno", [5.0, 6.0, 4.5]),
        ("Carlos", []),
        ("Diana", [10.0, 9.5, 9.8]),
        ("Eduardo", [7.0, 8.0, 6.0]) 
    ]

    print("Processando dados...")
    resultados, top_student = processamento.processar_alunos(alunos)
    
    print("Gerando arquivo .txt...")
    processamento.gerar_relatorio(resultados, top_student)
    
    print("Sucesso! Verifique o arquivo 'resultado.txt'.")

if __name__ == "__main__":
    main()