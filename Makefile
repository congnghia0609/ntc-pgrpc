# Author: nghiatc
# Since: 09/01/2021


.PHONY: gen
gen:
	@python -m grpc_tools.protoc -I./ngrpc --python_out=./ngrpc --grpc_python_out=./ngrpc ./ngrpc/calculator.proto

.PHONY: server
server:
	@python server.py

.PHONY: client
client:
	@python client.py

.PHONY: async_server
async_server:
	@python async_server.py

.PHONY: async_client
async_client:
	@python async_client.py

.PHONY: ssl
ssl:
	@cd ./ssl; ./gen_ssl.sh; cd ..;
