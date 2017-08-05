https://hub.docker.com/r/microsoft/mssql-server-windows-express/

docker run -d -p 1433:1433 -e sa_password=_ -e ACCEPT_EULA=Y microsoft/mssql-server-windows-express