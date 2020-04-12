from jupyter/scipy-notebook

# install dev tools
user root
run apt-get update
run apt-get install -y ranger
run apt-get install -y vim
run apt-get remove cmdtest
RUN apt-get install -y curl

# install node kernel for jupyter
user jovyan
run npm install -g ijavascript
run npm install -g jp-babel

run ijsinstall
run jp-babel-install

# install python dependencies
user root
copy ./requirements.txt /srv/requirements.txt
workdir /srv
run pip install -r requirements.txt

# install js dependencies
user jovyan
env NODE_PATH=/opt/conda/lib
copy ./package.json /home/jovyan/package.json
workdir /home/jovyan
run npm install
copy ./.babelrc /home/jovyan/.babelrc

# run jupyter
env JUPYTER_ENABLE_LAB=1
env JUPYTER_TOKEN=123
user jovyan
workdir /home/jovyan
cmd jp-babel-notebook --ip=* --debug

# use this line instead of the one above to run vanilla js
# cmd ijs --ip=* --debug

# expose 8888
