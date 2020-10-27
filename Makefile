all: py js php

py:
	mkdir -p ./hello_py/compiled; true
	rm ./hello_py/compiled/*; true
	protoc -I=./protos  --python_out=hello_py/compiled ./protos/*.proto

js:
	mkdir -p ./hello_js/compiled; true
	rm ./hello_js/compiled/*; true
	#protoc -I=./protos --js_out=import_style=commonjs,binary:compiled_js ./protos/*.proto
	protoc -I=./protos --js_out=import_style=commonjs,binary:hello_js/compiled ./protos/*.proto

php:
	mkdir -p ./hello_php/compiled; true
	rm ./hello_php/compiled/*; true
	protoc -I=./protos  --php_out=./hello_php/compiled ./protos/hello.proto
