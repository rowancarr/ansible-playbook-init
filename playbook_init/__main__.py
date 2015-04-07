__author__ = 'rc'

import argparse
import os
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Path of new playbook", default="./")
parser.add_argument("-n", "--name", help="Playbook name")

args = parser.parse_args()

if not args.name:
    print parser.print_help()
    exit(1)

path = args.directory + args.name + "/"


def shell_command(cmd_text):
    global out
    p = subprocess.Popen(cmd_text, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if out:
        return True

    return False


def create_base(_path, name, directory):

    dirs = ['group_vars', 'tasks', 'templates', '.librarian/ansible']
    files = ['hosts', 'group_vars/main.yml', 'templates/main.yml', 'tasks/main.yml']

    if os.path.exists(_path):
        print("[ERROR] - Playbook " + name + "already exists in " + directory + "\n")
        exit(1)

    for new_dir in dirs:
        if not os.path.exists(_path + new_dir):
            os.makedirs(_path + new_dir)

    for new_file in files:
        if not os.path.exists(_path + new_file):
            with open(_path + new_file, 'w') as new_file_fout:
                new_file_fout.write('')


def create_files(fileo, lines, _path):

    with open(_path + fileo, 'w') as fout:
        fout.writelines(lines)

if not shell_command(['which', 'gem']):
    print('[ERROR] - Please install Gem before proceeding')

if not shell_command(['which', 'bundle']):
    print('[INFO] - Installing bundle')
    shell_command(['gem', 'install', 'bundler'])


def main():

    """


    """
    data_files = {
        '.gitignore': ["*.lock\n", "tmp\n", "roles\n"],
        'Readme.md': [args.name + " playbook\n"],
        'Gemfile': ["source \"https://rubygems.org\"\n", "gem \'librarian-ansible\'\n"],
        '.librarian/ansible/config': ["---\n", "LIBRARIAN_ANSIBLE_PATH: ./roles"],
        'Ansiblefile': ["#!/usr/bin/env ruby\n", "#^syntax detection\n\n",
                        "site \"https://galaxy.ansible.com/api/v1\"\n"]
    }

    create_base(path, args.name, args.directory)

    for key in data_files:
        create_files(key, data_files[key], path)

if __name__ == "__main__":
    main()