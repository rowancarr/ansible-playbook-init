SHELL = /bin/sh
all: install

install: 
	cp -f ansible-playbook-init /usr/local/bin/ansible-playbook-init