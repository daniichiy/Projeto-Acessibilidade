# routes.py

from flask import render_template, request
from forms import AnalisarForm  # Alterado para importação absoluta
from tool.rastreador_de_url import gerar_resposta_json
from tool.analisa_imagem import analisa
from tool.baixar_img import baixar, limpar_pasta_img
from tool.gerar_relatorio import gerar_relatorio_docx
from tool.database import criar_tabela, salvar_relatorio
import os
import json

def index():
    form = AnalisarForm()

    if form.validate_on_submit():
        url = form.url.data
        profundidade = int(form.profundidade.data)  # Converte para inteiro
        relatorio_nome = request.form['relatorio_nome']  # Captura o nome do relatório informado pelo usuário
        
        # Cria a tabela no banco se não existir
        criar_tabela()

        # Limpar a pasta de imagens antes de começar
        limpar_pasta_img()

        # Iniciar a extração de links e gerar o relatório
        entrada = gerar_resposta_json(url, profundidade)
        entrada_dict = json.loads(entrada)

        # Dicionário para armazenar os resultados da análise
        resultado_analises = {}
        imagens_baixadas = set()

        # Pasta para armazenar imagens
        pasta_img = "img"
        os.makedirs(pasta_img, exist_ok=True)

        # Processar os links extraídos
        for url_info in entrada_dict['urls']:
            link = url_info['link']
            try:
                analise_resultado = analisa(link)

                for imagem in analise_resultado.get('detalhes_imagens_sem_alt', []):
                    img_url = imagem['img_url']
                    if img_url not in imagens_baixadas:
                        nome_arquivo = img_url.split('/')[-1]
                        baixar(img_url, nome_arquivo)
                        imagens_baixadas.add(img_url)

                resultado_analises[link] = analise_resultado
            except Exception as e:
                print(f"Erro ao analisar {link}: {e}")

        # Definindo o caminho para salvar o relatório na pasta 'relatorios_gerados'
        pasta_relatorios = 'relatorios_gerados'
        os.makedirs(pasta_relatorios, exist_ok=True)  # Garante que a pasta existe

        # Gerar o relatório de auditoria com o nome do usuário
        nome_arquivo_docx = os.path.join(pasta_relatorios, f"{relatorio_nome}.docx")  # Usando o nome informado pelo usuário e o caminho da pasta
        gerar_relatorio_docx(resultado_analises, nome_arquivo_docx)

        # Salvar as informações no banco de dados
        total_imagens = 0
        imagens_sem_alt = 0
        for resultado in resultado_analises.values():
            total_imagens += resultado.get('total_imagens', 0)
            imagens_sem_alt += len(resultado.get('detalhes_imagens_sem_alt', []))

        salvar_relatorio(nome_arquivo_docx, os.path.abspath(nome_arquivo_docx), total_imagens, imagens_sem_alt)

        # Retornar uma mensagem de sucesso
        return render_template('index.html', form=form, success_message=f"Relatório '{relatorio_nome}' gerado e salvo com sucesso!")

    return render_template('index.html', form=form)
