#! /bin/bash

# Server common name
SERVER_CN=localhost

# Generate Certificate Authority + Trust Certificate (client.crt)
openssl genrsa -passout pass:123456 -des3 -out client.key 4096
openssl req -passin pass:123456 -new -x509 -days 3650 -key client.key -out client.crt -subj "/CN=${SERVER_CN}"

# Generate the Server Private Key (server.key)
openssl genrsa -passout pass:123456 -des3 -out server.key 4096
# Get a certificate signing request from the CA (server.csr)
openssl req -passin pass:123456 -new -key server.key -out server.csr -subj "/CN=${SERVER_CN}"

# Sign the certificate with the CA - server.crt
openssl x509 -req -passin pass:123456 -days 3650 -in server.csr -CA client.crt -CAkey client.key -set_serial 01 -out server.crt

# Convert the server certificate to .pem (server.pem) - usable by gRPC
openssl pkcs8 -topk8 -nocrypt -passin pass:123456 -in server.key -out server.pem

# HAProxy pem
cat server.pem server.crt > haproxy.pem