# ansible-playbook-init

Simple python tool to set up a role based [ansible](http://www.ansible.com) playbook template with [librarian-ansible](https://github.com/bcoe/librarian-ansible)

## Requirements
Tested working on osx 10.10.2 however should work on most if not all linux/unix os

## Install 

```
python setup.py install
```
 
## Usage

Run the following command to get your new template setup
```
ansible-playbook-init -n ansible-playbook-name -d ~/ansible_playbooks
```
Once setup take a look at the [librarian-ansible](https://github.com/bcoe/librarian-ansible) documentation and make appropriate changes to the ```Ansiblefile``` and run ```librarian-ansible``` in your new playbook directory. Checkout [playbooks_role](http://docs.ansible.com/playbooks_roles.html) for more detail on role based playbooks.


