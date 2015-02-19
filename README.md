# SIADE

SIADE é um sistema para coleta de dados realizada pelos agentes de endemias, eliminando todo o trabalho manual.

## Requisitos

* Python (2.7)
* Django (1.7)
* reportlab (3.1+)
* djangorestframework (2.4)
* django-extensions (1.4)
* django-oauth-toolkit (0.7)
* [Entre outros](https://github.com/holocronifrn/siade-server/blob/master/requirements/common.txt)

## Instalando

Baixar o SIADE pelo repositõrio git

	git clone https://github.com/holocronifrn/siade-server.git

Instalar requisitos

	pip install -r requirements/dev.txt

Criar o banco de dados e criar um usuario superusuário inicial

	python manage.py migrate
	python manage.py createuseruser

Criar grupos e permissões iniciais

	python manage.py atualizar_grupos

Criar árvore de navegação

	python manage.py sitetree_resync_apps

Para inicar o servidor de desenvolvimento basta executar o comando:

	python manage.py runserver
