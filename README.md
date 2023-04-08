
# Django E-commerce

Um e-commerce com django no back-end.

## Instalação

Clone o repositorio no seu computador
```bash
git clone git@github.com:wezlleyv/django-ecommerce.git
```

Entre no diretório do repositorio
```bash
cd django-ecommerce
```

Crie e inicie um ambiente virtual em python (LINUX)
```bash
python -m venv venv
source ./venv/bin/activate
```

Instale as dependencias
```bash
pip install -r requirements.txt
```

Inicie as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

Inicie o projeto usando

```bash
python manage.py runserver
```
