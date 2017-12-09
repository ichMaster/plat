# exit
# help
# ls
# cat
# cd
# mkdir
# rm
# cp
# mv

import os
import sys

from messages import *
from environment import *


def int_current_directory_set(dir):
    global env_current_directory
    env_current_directory = dir


def int_prompt_create(dir):
    global PROMPT
    global PROMPT_PRE
    global PROMPT_POST

    PROMPT = PROMPT_PRE + dir + PROMPT_POST


def int_init_env():
    global env_current_directory
    int_current_directory_set(os.getcwd())
    int_prompt_create(env_current_directory)


def command_help(cmd):
    print("""REPL Commands:
    exit
    ls
    cd
    cat
    help
    """)


def command_ls(cmd):
    MARK_DIR = "/"
    MARK_TAB = "\t"
    MaKR_DELIM = "-----"
    MART_HEADER = "Name"
    items = os.listdir(env_current_directory)
    outp = []
    for i in items:
        if os.path.isdir(os.path.join(env_current_directory, i)):
            i = i + MARK_DIR
        outp.append(i)
    print(MART_HEADER)
    print(MaKR_DELIM)
    for i in outp:
        print(i)


def command_cd(cmd):
    global env_current_directory
    try:
        os.chdir(os.path.join(env_current_directory, cmd[1]))
    except Exception:
        print(ERR_WRONGDIR)
    int_current_directory_set(os.getcwd())
    int_prompt_create(env_current_directory)


def command_cat(cmd):
    try:
        out_file = open(cmd[1], "r")
        for l in out_file.readlines():
            sys.stdout.write(l)
        out_file.close()
    except Exception:
        print(ERR_FILENOTFOUND)


#REPL Body

print (MSG_HELLO)
int_init_env()
while env_current_command != COMMAND_EXIT:
    env_current_command = input(PROMPT)
    cmd = env_current_command.split(" ")

    if cmd[0] == COMMAND_EXIT:
        break
    elif cmd[0] == COMMAND_HELP:
        command_help(cmd)
    elif cmd[0] == COMMAND_LS:
        command_ls(cmd)
    elif cmd[0] == COMMAND_CD:
        command_cd(cmd)
    elif cmd[0] == COMMAND_CAT:
        command_cat(cmd)
    else:
        print(ERR_COMMANDNOTFOUD)


print(MSG_EXIT)
exit(0)



