from setuptools import setup

setup(
    name='ansible-playbook-init',
    version='0.0.2',
    packages=['playbook_init'],
    url='https://github.com/rowancarr/ansible-playbook-init.git',
    license='Apache2.0',
    author='Rowan Carr',
    author_email='',
    description='Simple tool to setup ansible playbook template with librarian-ansible',
    entry_points={
        'console_scripts': [
            'ansible-playbook-init = playbook_init.__main__:main'
        ]
    },

)
