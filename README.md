# install kernels
npm install -g ijavascript
ijsinstall
npm install -g jp-babel
jp-babel-install

# build, run and debug container
docker build -t jupyter .
docker run -it --rm --name jupyter -p 8888:8888 -v "$PWD"/notebooks:/home/jovyan/work jupyter
docker exec -it jupyter bash

# After running the docker container you should see this line in the logs:

http://(df5c4a4c87f5 or 127.0.0.1):8888/?token=a187e8feac1749b0a9163a5f789fee8fffe4169d44dae409

# You can access the Jupyter online here:
# Jupyter notebooks will be saved in "notebooks" folder
http://localhost:8888/?token=a187e8feac1749b0a9163a5f789fee8fffe4169d44dae409

# or use the kernel gateway with this token:
a187e8feac1749b0a9163a5f789fee8fffe4169d44dae409

# language mappings at hydrogen settings
{"javascript": "javascript", "babel": "babel es6 javascript"}

# kernel gateways at hydrogen settings
[{
  "name": "Remote server",
  "options": {
    "baseUrl": "http://localhost:8888",
    "token": "123"
  }
}]

# TODO: starup code at hydrogen settings
# TODO: custom token at hydrogen settings
# TODO: JSX syntax
