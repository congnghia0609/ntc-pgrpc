# Author:       nghiatc
# Email:        congnghia0609@gmail.com


.PHONY: gen
gen:
	@python -m grpc_tools.protoc -I./ngrpc --python_out=./ngrpc --grpc_python_out=./ngrpc ./ngrpc/calculator.proto

.PHONY: server
server:
	@python server.py

.PHONY: client
client:
	@python client.py

.PHONY: ssl
ssl:
	@cd ./ssl; ./gen_ssl.sh; cd ..;
