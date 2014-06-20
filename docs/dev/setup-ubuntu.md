# Configurar ambiente de desenvolvimento no Ubuntu

Instalar pip, virtualenv e virtualenvwrapper

	sudo apt-get install -y python-pip python-virtualenv
	sudo pip install virtualenvwrapper

Criar novo virtualenv e ativar

	mkvirtualenv siade
	workon siade

Instalar pacotes python requeridos

	pip install -r requirements-dev.txt

Executar o comandos para criar o banco de dados

	python manage.py syncdb
	python manage.py migrate
