prepare_network:
	docker network create prlmntq_net

set_venv:
	python3 -m venv env && source env/bin/activate && pip install -r requirements.txt 

start_db:
	docker-compose up

populate_db:
	python populate.py 

setup_db: prepare_network set_venv start_db populate_db
	