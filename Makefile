all:
	docker exec -it python3 python suimei.py
build:
	docker-compose build
up:
	docker-compose up -d
ps:
	docker-compose ps
version:
	docker exec -it python3 python --version
down:
	docker-compose down
bash:
	docker-compose exec python3 bash
