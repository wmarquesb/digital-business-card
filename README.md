# Cartão de Visitas Digital com Análise de Cliques

![Captura de tela da página de links](https://prnt.sc/5mSqsWySBMHP)

![Captura de tela da página admin](https://prnt.sc/o5Xw9c6Nfvz9)

Uma aplicação web Full Stack, construída com Python e Flask, que permite criar uma página de links personalizada, similar ao Linktree. O projeto inclui um painel de administração para gerenciar os links e visualizar a popularidade de cada um através de um gráfico de cliques.

### Funcionalidades Principais

- **Painel de Administração:** Interface completa para Criar, Ler, Atualizar e Apagar (CRUD) links.
- **Reordenação Drag-and-Drop:** Permite organizar a ordem dos links facilmente, arrastando e soltando na posição desejada.
- **Análise de Cliques:** Um gráfico de barras exibe visualmente os links mais populares com base na contagem de cliques.
- **Ícones Personalizados:** Suporte para adicionar URLs de ícones para cada link, melhorando a identidade visual.
- **Geração de QR Code:** Gera e permite o download de um QR Code que aponta para a página pública, facilitando o compartilhamento em mídias físicas e digitais.

### Tecnologias Utilizadas

- **Backend:** Python, Flask, SQLite
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS)
- **Bibliotecas:** Chart.js (gráficos), SortableJS (drag-and-drop), qrcode (geração de QR Code), Bootstrap 5 (estilização)

### Jornada e Aprendizados

Este foi o projeto fundamental que marcou minha transição do aprendizado teórico para a prática do desenvolvimento Full Stack.

Tudo começou com uma ideia simples: um agregador de links pessoal. O primeiro desafio foi construir uma API funcional com Flask e fazê-la interagir de forma persistente com um banco de dados SQLite, escrevendo SQL puro para entender a base de tudo. Em seguida, o foco passou para a experiência do usuário no painel de administração, onde implementei funcionalidades complexas como a reordenação com "arrastar e soltar" e a visualização de dados com Chart.js.

Cada nova feature, como a geração do QR Code, foi uma oportunidade para aprender a integrar novas bibliotecas e resolver problemas práticos do mundo real. Este projeto foi um exercício completo que me ensinou o ciclo de vida de uma aplicação web, da concepção de uma API até a criação de uma interface de usuário interativa e funcional.

### Como Executar Localmente

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/wmarquesb/digital-business-card.git](https://github.com/wmarquesb/digital-business-card.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicialize o banco de dados:**

    ```bash
    python setup_database.py
    ```

5.  **Inicie o servidor Flask:**

    ```bash
    python app.py
    ```

6.  **Acesse as páginas:**
    - **Página Pública:** `http://127.0.0.1:5000/`
    - **Painel de Admin:** `http://127.0.0.1:5000/admin`
