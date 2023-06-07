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
### 3. Edite o arquivo .env-example e adicione as variáveis de ambiente

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
### Acesso a api pelo swagger
```bash
http://127.0.0.1:8000/api/swagger/
```