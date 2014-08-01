# SIADE

SIADE é um sistema para coleta de dados realizada pelos agentes de endemias, eliminando todo o trabalho manual.

## Requisitos

* Python (2.7)
* Django (1.6)
* South
* reportlab (3.1+)
* djangorestframework (2.3+)
* django-oauth-toolkit

## Instalando

Baixar o SIADE pelo repositõrio git

	git clone https://github.com/holocronifrn/siade-server.git

Instalar requisitos

	pip install -r requirements.txt

Criar o banco de dados execute os comandos

	python manage.py syncdb --all
	python manage.py migrate --fake

Para inicar o servidor de desenvolvimento basta executar o comando:

	python manage.py runserver
