default: clean test build

clean:
	find . -name '__pycache__' -delete -print \
		-o -name '*.pyc' -delete -print

build:
	docker build --target runner -t fasi_api_base .

build-test:
	docker build --target tester -t fasi_api_base_test .

test: build-test
	docker rm -f fasi_api_base_test || echo "container removed"
	docker run --name fasi_api_base_test fasi_api_base_test
	docker rm -f fasi_api_base_test || echo "container removed"

run: build
	docker run --rm -p 8080:8000 --env-file .env.local --name fasi_api_base fasi_api_base
