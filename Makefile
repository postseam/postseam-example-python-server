create_submodule:
	git submodule add https://github.com/postseam/postseam-example-api

update_submodules:
	git submodule update --remote

pip_compile:
	pip-compile -o requirements.txt

generate_server:
	python3 -m grpc_tools.protoc \
		--python_out=./ \
		--grpc_python_out=./ \
		--proto_path=./postseam-example-api \
		./postseam-example-api/pb/postseam/example/v1/*.proto 

unit_test:
	python -m coverage run -m unittest

coverage:unit_test
	python -m coverage report --omit='pb/*','test/*'

build_docker:
	docker build -t postseam-example-python-server . 

run_docker:
	docker run --network="host"  -it -p 8000:8000 postseam-example-python-server:latest

test_docker:
	docker run postseam-example-python-server:latest make unit_test

postgres_docker:
	docker run \
    -p 5432:5432 \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=postseam \
	-e POSTGRES_HOST_AUTH_METHOD=trust \
    -v /var/lib/postgres/data:/var/lib/postgres/data \
	-it postgres
