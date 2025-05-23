# Sistema para Analisar Acessibilidade Web

Este projeto tem como objetivo automatizar a **análise de acessibilidade** dos sites do governo do Estado de Mato Grosso do Sul.  O sistema utiliza ferramentas para extrair, analisar e gerar relatórios detalhados sobre as condições de acessibilidade, com foco especial na verificação de **textos alternativos em imagens**. Isso ajuda a garantir que os sites estejam acessíveis para pessoas com deficiência visual, promovendo inclusão digital.

---

## Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Autores](#autores)

---

## Sobre o Projeto

A acessibilidade digital é um direito fundamental, e este sistema busca identificar e melhorar o acesso à web para pessoas com deficiência. Ao analisar os sites governamentais, o projeto foca na presença de textos descritivos alternativos para imagens, proporcionando uma melhor experiência para usuários com deficiência visual.

### Principais funcionalidades:

- **Verificação de Texto Alternativo em Imagens**:
  - O sistema analisa todas as imagens de uma página web e verifica se possuem **texto alternativo** (atributo "alt"). Isso ajuda a identificar falhas de acessibilidade relacionadas a imagens que não têm descrições adequadas para usuários com deficiência visual.
  
- **Download de Imagens para Relatório**:
  - O sistema realiza o **download das imagens** diretamente da página web para inclusão nos relatórios de auditoria, garantindo que os relatórios tenham uma apresentação visual clara e completa das imagens sem texto alternativo.

- **Geração de Relatórios em PDF e Word**:
  - O sistema gera **relatórios de auditoria em formato PDF e DOCX** com um resumo da análise das imagens. Isso inclui o total de imagens, quantas possuem o atributo "alt", e quantas estão faltando. Para imagens sem "alt", miniaturas e URLs das imagens são incluídas no relatório.
  
- **Criação de Tabelas e Detalhamento**:
  - Os relatórios em Word incluem tabelas com o resumo da análise, detalhando as imagens que não possuem **texto alternativo**. Cada imagem sem "alt" é apresentada com sua respectiva URL, facilitando a navegação e a correção das falhas encontradas.

- **Links Clicáveis no Relatório**:
  - Nos relatórios DOCX, o sistema permite a inclusão de **hyperlinks clicáveis**, tornando o acesso direto às imagens ou páginas da web mais fácil para os revisores.

- **Análise Recursiva de Links**:
  - O sistema também realiza a análise recursiva de links internos, permitindo a verificação de todas as páginas vinculadas dentro de um site, expandindo a abrangência da auditoria de acessibilidade.

- **Armazenamento de Relatórios no Banco de Dados**:
  - Os relatórios gerados são armazenados na pasta `relatorios_gerados` e registrados no banco de dados, garantindo um registro organizado das análises feitas.

---

## Como utilizar este projeto:

1. Clone este repositório em sua máquina local:
    ```bash
    git clone https://github.com/daniichiy/Projeto-Acessibilidade.git
    ```

2. Crie um ambiente virtual e instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure o arquivo `.env` com as variáveis necessárias, como a chave secreta e a chave de CSRF:
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Defina as variáveis no arquivo `.env`:
    ```plaintext
    SECRET_KEY=SuaChaveSecretaAqui
    CSRF_SECRET_KEY=SuaChaveCSRFAqui
    ```

4. Para rodar o projeto, digite:
    ```bash
    python app.py
    ```

5. Acesse o sistema através do navegador em:
    ```plaintext
    http://127.0.0.1:5000
    ```

---

## Tecnologias Utilizadas

As principais tecnologias e ferramentas usadas no desenvolvimento deste sistema incluem:

- **Python**: Linguagem principal utilizada para o desenvolvimento do projeto.
- **Flask**: Framework utilizado para criar o servidor web.
- **Flask-WTF**: Extensão para trabalhar com formulários no Flask, incluindo proteção CSRF.
- **WTForms**: Biblioteca para criação de formulários.
- **SQLAlchemy**: ORM para interagir com o banco de dados PostgreSQL.
- **PostgreSQL**: Banco de dados utilizado para armazenar informações dos relatórios.
- **dotenv**: Para carregar variáveis de ambiente a partir do arquivo `.env`.
- **WCAG 2.1**: Diretrizes Internacionais de Acessibilidade para Conteúdo Web.

---

## Autores
- **Daniele Ichiy** - *Tecnologia da Informação* - [GitHub](https://github.com/daniichiy) | [LinkedIn](https://www.linkedin.com/in/daniele-lins-ichiy-5001b928b/)
- **Fabio** - *Engenharia de Software* - [GitHub](https://github.com/fabioramos-02) | [LinkedIn](https://www.linkedin.com/in/fabio-ramos-7b8608204/)
- **Geraldo Neto** - *Tecnologia de Ciência dos Dados* - [GitHub](https://github.com/geraldoneto) | [LinkedIn](https://www.linkedin.com/in/geraldobneto)
- **Júlia Kuroishi** - *Tecnologia da Informação* - [GitHub](https://github.com/juliakuroishi) | [LinkedIn](https://www.linkedin.com/in/julia-kuroishi-244bb0248/)

