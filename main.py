import json
from tool.rastreador_de_url import gerar_resposta_json
from tool.analisa_imagem import analisa  # Importar a função analisa do arquivo
from tool.baixar_img import baixar, limpar_pasta_img  # Função para baixar as imagens
from tool.gerar_relatorio import gerar_relatorio_docx  # Importar a função gerar_relatorio_auditoria do arquivo
from tool.database import criar_tabela, salvar_relatorio  # Importar funções do módulo de banco
import os

def main():
    # Cria a tabela no banco, se ainda não existir
    criar_tabela()

    limpar_pasta_img() 
    # Solicitar a URL e a profundidade ao usuário
    url_alvo = input("Digite a URL do site para extração de links: ")

    # Perguntar se o usuário deseja definir um nível de profundidade
    while True:
        escolha = input("Deseja fornecer um nível de profundidade? (s/n): ").strip().lower()
        if escolha == 's':
            profundidade = int(input("Informe a profundidade (Ex: 1, 2, 3...): "))
            break
        elif escolha == 'n':
            profundidade = float('inf')  # Define profundidade como infinita para percorrer todo o site
            break
        else:
            print("Entrada inválida. Por favor, digite 's' para sim e 'n' para não.")

    # Perguntar ao usuário o nome do arquivo para o relatório
    nome_arquivo_docx = input("Digite o nome do arquivo para salvar o relatório DOCX (sem extensão): ") + ".docx"
    # Iniciar o processo de extração com a URL e profundidade fornecidas    
    print("Iniciando extração de links...")
    entrada = gerar_resposta_json(url_alvo, profundidade)
    entrada_dict = json.loads(entrada)  # Converter a string JSON para dicionário Python

    # Criar um dicionário para armazenar os resultados da análise
    resultado_analises = {}
    # Criar um conjunto para armazenar as URLs das imagens já baixadas
    imagens_baixadas = set()

    # Caminho para a pasta de imagens
    pasta_img = "img"
    
    # Criar a pasta se não existir
    os.makedirs(pasta_img, exist_ok=True)
    print("Iniciando análise de URLs...")
    for url_info in entrada_dict['urls']:
        link = url_info['link']
        try:
            analise_resultado = analisa(link)
            
            # Verificar se há imagens sem o atributo 'alt' e tentar baixá-las
            for imagem in analise_resultado.get('detalhes_imagens_sem_alt', []):
                img_url = imagem['img_url']
                
                # Verificar se a URL já foi baixada
                if img_url not in imagens_baixadas:
                    nome_arquivo = img_url.split('/')[-1]  # Nome da imagem com base na URL
                    
                    # Baixar a imagem e salvar na pasta 'img'
                    baixar(img_url, nome_arquivo)
                    
                    # Adicionar a URL da imagem ao conjunto de imagens baixadas
                    imagens_baixadas.add(img_url)
            
            resultado_analises[link] = analise_resultado
        except Exception as e:
            print(f"Erro ao analisar {link}: {e}")

    # Gerar o relatório de auditoria
    print("Gerando relatórios de auditoria...")
    gerar_relatorio_docx(resultado_analises, nome_arquivo_docx)

    # Preparar dados para salvar no banco
    total_imagens = 0
    imagens_sem_alt = 0
    for resultado in resultado_analises.values():
        total_imagens += resultado.get('total_imagens', 0)
        imagens_sem_alt += len(resultado.get('detalhes_imagens_sem_alt', []))

    # Salvar os dados no banco de dados
    salvar_relatorio(nome_arquivo_docx, os.path.abspath(nome_arquivo_docx), total_imagens, imagens_sem_alt)

    print("Relatórios de auditoria gerados e salvos no banco de dados!")

if __name__ == "__main__":
    main()
