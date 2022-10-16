all:
	docker exec -it meishiki python suimei.py $(BIRTH) $(SEX)
build:
	docker-compose build --no-cache
install:
	docker-compose build
up:
	docker-compose up -d
ps:
	docker-compose ps
version:
	docker exec -it meishiki python --version
down:
	docker-compose down
bash:
	docker-compose exec meishiki bash
ls:
	docker container ls
