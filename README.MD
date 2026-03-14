🚀 API de Vagas de Emprego

API REST desenvolvida em Python para gerenciamento de vagas de emprego, permitindo que empresas publiquem vagas e candidatos se candidatem.

Este projeto foi desenvolvido com foco em praticar desenvolvimento backend, autenticação e controle de permissões.

🧠 Funcionalidades

    ✔ Cadastro de usuários
    ✔ Login com autenticação JWT
    ✔ Dois tipos de usuários:

    - Empresa
    - Candidato

    ✔ Empresas podem criar vagas
    ✔ Candidatos podem se candidatar às vagas
    ✔ Empresas não podem se candidatar
    ✔ Candidatos não podem criar vagas
    ✔ Listagem de vagas disponíveis
    ✔ Controle de permissões na API

🛠 Tecnologias utilizadas

    * Python

    * Flask

    * PostgreSQL

    * SQLAlchemy

    * Flask-JWT-Extended


📂 Estrutura do projeto

    api_linkedin/
│
├── routes/
│   ├── auth_routes.py
│   └── job_routes.py
│
├── models/
│   ├── user.py
│   ├── job.py
│   └── application.py
│
├── database.py
├── config.py
├── app.py
└── requirements.txt

🔐 Autenticação

A API utiliza autenticação baseada em JWT (JSON Web Token).

Após realizar o login, o usuário recebe um token que deve ser enviado nas requisições protegidas.

Exemplo de header: Authorization: Bearer SEU_TOKEN

📡 Endpoints principais

CRIAR USUÁRIO
POST /register


FAZER LOGIN
POST /login

CRIAR VAGA(somente empresas)
POST /job


LISTAR VAGAS
GET /jobs


CANDIDATAR-SE A UMA VAGA
POST /jobs/<job_id>/apply


⚙️ Como rodar o projeto

1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/api-job-platform.git

2️⃣ Criar ambiente virtual
python -m venv venv

3️⃣ Ativar ambiente

Windows

venv\Scripts\activate

👨‍💻 Autor

Bruno Melo

Estudante de Tecnologia da Informação e entusiasta de desenvolvimento backend.

🚀 Melhorias futuras

    - Filtro de vagas

    - Paginação

    - Documentação da API

    - Deploy em produção

    - Testes automatizados