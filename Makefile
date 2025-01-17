default: clean test build

clean:
	find . -name '__pycache__' -delete -print \
		-o -name '*.pyc' -delete -print

build:
	docker build --target runner -t src_container .

build-test:
	docker build --target tester -t src_test .

test: build-test
	docker rm -f src_test || echo "container removed"
	docker run --name src_test src_test
	docker rm -f src_test || echo "container removed"

run: build
	docker run --rm -p 8080:8000 --name src_container src_container
