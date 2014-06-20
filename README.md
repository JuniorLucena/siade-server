# SIADE

SIADE é um sistema web para coleta de dados realizada pelos agentes de endemias, eliminando todo o trabalho manual.

## Requerimentos

	Django==1.6.5
	South==0.8.4
	django-extensions==1.3.7
	django-filter==0.7
	django-oauth2-provider==0.2.6.1
	django-xadmin==0.5.0
	djangorestframework==2.3.14
	djangorestframework-bulk==0.1.3
	reportlab==3.1.8

## Instalando

Baixar o SIADE pelo repositõrio git

	git clone https://github.com/roldaojr/siade.git

Criar o banco de dados execute os comandos

	python manage.py syncdb
	python manage.py migrate

Para inicar o servidor de desenvolvimento basta executar o comando:

	python manage.py runserver
