prepare_network:
	docker network create prlmntq_net

start-dev: 
	docker-compose up 

install_requirements:
	pip3 install -r requirements.txt

populate:
	python3 populate.py

setup_db: install_requirements populate

test_db:
	python3 db_test.py