# Documentação do projeto Chat-Django

### 1. Clone o repositório
```bash
git clone https://github.com/viniciusmbpro/django-chat.git
```
### 2. Crie um ambiente virtual, ative e instale as dependências do projeto
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Entre na pasta App/ e edite o arquivo .env-example e adicione as variáveis de ambiente

### 4. Execute as migrações e inicie o servidor
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Acesso ao site
```bash
http://127.0.0.1:8000/
```
### Documentação da API pelo swagger
```bash
http://127.0.0.1:8000/api/swagger/
```

## Endpoints da API
| Endpoint | Descrição |
| --- | --- |
| POST /api/accounts/ | Create account |
| GET /api/accounts/{id}/ | Retrieve account by ID |
| PUT /api/accounts/{id}/ | Update account by ID |
| PATCH /api/accounts/{id}/ | Partially update account by ID |
| DELETE /api/accounts/{id}/ | Delete account by ID |
| GET /api/accounts/me/ | Retrieve current user account |
| GET /api/accounts/my-chats/ | Retrieve chats of current user |
| GET /api/accounts/participant-chats/ | Retrieve chats of current user as participant |
| GET /api/accounts/search/ | Search account by email and/or username |
| GET /api/chats/ | List all chats |
| POST /api/chats/ | Create a chat |
| GET /api/chats/{id}/ | Retrieve chat by ID |
| PUT /api/chats/{id}/ | Update chat by ID |
| PATCH /api/chats/{id}/ | Partially update chat by ID |
| DELETE /api/chats/{id}/ | Delete chat by ID |
| POST /api/chats/{id}/add-message/ | Add message to chat |
| POST /api/chats/{id}/add-participant/ | Add participant to chat |
| POST /api/chats/{id}/remove-participant/ | Remove participant from chat |
| GET /api/messages/{id}/ | Retrieve message by ID |
| PUT /api/messages/{id}/ | Update message by ID |
| PATCH /api/messages/{id}/ | Partially update message by ID |
| DELETE /api/messages/{id}/ | Delete message by ID |
