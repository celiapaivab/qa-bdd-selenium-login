# Selenium Template

Este repositório é um template base para automação de testes com Selenium e Pytest, com suporte para:

- Estrutura modular (Page Object Model)
- Pipeline CI/CD com GitHub Actions
- Relatórios HTML (opcional)
- Testes BDD com Gherkin (opcional)


---

## Como usar

Para iniciar um novo projeto baseado neste template, siga os passos:

1. Clique no botão **"Use this template"**.

2. Escolha um nome para o novo repositório e clique em **"Create repository from template"**.

3. Clone o repositório recém-criado para sua máquina local:
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_NOVO_REPOSITORIO.git
cd NOME_DO_NOVO_REPOSITORIO
```

4. Crie e ative um ambiente virtual Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

5. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

6. Execute os testes localmente:
```bash
pytest
pytest --html=reports/report.html # Com relatório HTML
```


## Estrutura do projeto

### `docs/`

Pasta destinada a arquivos de documentação e materiais complementares do projeto.

---

### `.github/workflows/`

Contém o arquivo de configuração do **GitHub Actions**, que executa os testes automaticamente em cada `push` ou `pull request` na branch `main`.

Neste template, o workflow:
- Faz checkout do código
- Cria o ambiente virtual
- Instala as dependências listadas no `requirements.txt`
- Executa os testes com o `pytest`
- (Opcional) Gera um relatório HTML dos testes e salva como artefato

---

### `features/`

Contém os arquivos **Gherkin (.feature)**, que descrevem cenários de teste no formato **BDD**.

- Esta pasta é **opcional**
- Instale o `pytest-bdd` no `requirements.txt`.
- Cada arquivo `.feature` descreve cenários em linguagem natural (Given, When, Then).
- Os testes em Python devem implementar os steps definidos nos `.feature`.

---

### `pages/`

Contém as classes do **Page Object Model (POM)**, padrão de design que organiza elementos e ações de cada página da aplicação em objetos Python.

- Cada página ou componente importante da aplicação tem uma classe própria.
- Isso facilita a manutenção e o reuso dos códigos que interagem com a interface.
- Exemplo: `login_page.py` pode ter métodos para preencher usuário, senha e clicar no botão.

---

### `reports/`

Esta pasta armazena os relatórios gerados pelos testes, como os relatórios HTML criados pelo `pytest-html`.

- Os relatórios são **gerados automaticamente** durante a execução dos testes com o comando:
  ```bash
  pytest --html=reports/report.html
  ```
- A pasta reports/ deve estar incluída no .gitignore.
- Os relatórios ajudam a visualizar os resultados dos testes, com detalhes sobre testes que passaram, falharam, tempos e erros.
- No pipeline do GitHub Actions, esses relatórios são salvos como artefatos para consulta posterior.

---

### `tests/`

Esta pasta contém os scripts de teste automatizados que usam o framework **pytest** para executar as verificações.

- Aqui ficam os testes que interagem com a aplicação por meio dos **Page Objects** definidos em `pages/`.
- Os testes devem ser escritos em funções ou classes seguindo as convenções do pytest.
- Caso use BDD com `pytest-bdd`, esta pasta também conterá as definições dos steps (funções que implementam as ações descritas nos arquivos `.feature`).
- Exemplo: um teste de login simples que utiliza o Page Object `LoginPage`.

---

### `utils/`

Esta pasta armazena **configurações e utilitários** para os testes automatizados.

- **`conftest.py`** — Define **fixtures** compartilhadas para preparar o ambiente de teste, como criar e encerrar o WebDriver (navegador).  
- **`data.py`** — Centraliza informações fixas do projeto (constantes).

---

### `.gitignore`

Arquivo que lista os arquivos e pastas que o Git deve **ignorar** e não versionar no repositório.  
Exemplos comuns no projeto:
- Pastas de ambiente virtual (`venv/`)  
- Arquivos de cache do Python (`__pycache__/`)  
- Pastas com relatórios gerados (`reports/`)   

---

### `README.md`

Arquivo de documentação principal do projeto, que contém informações importantes para quem for usar ou contribuir no repositório.  
Neste template, o README explica:  
- Como iniciar e usar o projeto  
- Estrutura das pastas  
- Detalhes sobre as configurações e testes  

---

### `requirements.txt`

Arquivo que lista todas as **dependências Python** necessárias para rodar os testes.  
Ao executar:  
```bash
pip install -r requirements.txt
```

o ambiente virtual instala todas as bibliotecas necessárias automaticamente, garantindo que o projeto funcione corretamente.

---