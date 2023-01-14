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

build_local:
	docker build -t postseam-example-python-server . 

run_local:
	docker run -it -p 8000:8000 postseam-example-python-server:latest

test_docker:
	docker run postseam-example-python-server:latest make unit_test
