# source ./.venv/bin/activate

run:
	uvicorn main:app --reload


db:
	docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=user -e POSTGRES_DB=db -d postgres

psql:
	docker exec -ti postgres psql db user
