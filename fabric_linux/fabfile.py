# -*- coding: utf-8 -*-
from fabric.api import *
import time
from IP_List import *
import subprocess
import ftplib
import os

# 사용법 fab dataa -t 5

# 명령이 실행되는 서버
#  '10.1.222.2'
# env.hosts = [IP_address.address] 사용 불가능한 방식
# ['IP주소','IP주소','IP주소','IP주소']
# 비밀번호 입력하라고함

env.hosts = Ip_Get_List

env.warn_only = True # 2.5 이상은 명령어 뒤에 , warn=True 만 하면되지만, 그이하는 이렇게 설정해줘야함, 접속 안되는경우 무시
env.skip_bad_hosts = True #  접속 안되는경우 무시
hosts_len = len(env.hosts)


yearmonth = input('년도, 월수 입력하세요 [ex) 202107] : ')
def dataa():
    # 원격 명령에 사용할 사용자
    env.user = 'ID'
    env.password = 'Password'
    
    dir = '/usr1/cps/data/ErrLog/'
    # 매게변수로 년도월수 입력 ex)202107
    with cd(dir):
        run('echo 발신 에러 개수 >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep 발신 | wc -l  >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep 발신 | head -n 20  >> full.txt')


        run('echo 국번 에러 개수 >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep 국번 | wc -l  >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep 국번| head -n 20 >> full.txt')

        run('echo Access Code  에러 개수 >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep Ac | wc -l  >> full.txt')
        run('more or' + str(yearmonth) +'*|grep Ac | head -n 20 >> full.txt')

        run('echo 결기 에러 개수 >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep 결기 | wc -l  >> full.txt')
        run('more  or' + str(yearmonth) +'*|grep 결기 head -n 20 >> full.txt')



        get(dir + 'full.txt')
        run('rm -rf full.txt')
        time.sleep(2)


    


# ●fabric의 주요 명령어
# - run('{command}') : 원격 서버에서 명령어를 수행한다.
# - local('{command}'): 로컬 서버에서 명령을 수행한다.
# - sudo('{command}'): 원격 서버에서 루트권한으로 명령을 수행한다.
# - reboot('{command}'): 원격의 시스템을 재시작 한다.
# - put('{path}'): 로컬 서버에서 원격 서버로 파일을 전송한다.
# - get('{path}'): 원격 서버에서 로컬 서버로 파일을 전송한다.
# - require(): 다양한 함수들간의 의존성을 만든다.(전제조건 없이 함수가 실행되는 것을 방지한다.)
# - execute('{command}'): 명령어를 실행한다.
# - with cd('{path}') : 특정 디렉토리를 베이스로 명령어등을 수행할때 사용        

# fab --help
# Usage: fab [options] <command>[:arg1,arg2=val2,host=foo,hosts='h1;h2',...] ...

# Options:
#   -h, --help            show this help message and exit
#   -d NAME, --display=NAME
#                         print detailed info about command NAME
#   -F FORMAT, --list-format=FORMAT
#                         formats --list, choices: short, normal, nested
#   -I, --initial-password-prompt
#                         Force password prompt up-front
#   --initial-sudo-password-prompt
#                         Force sudo password prompt up-front
#   -l, --list            print list of possible commands and exit
#   --set=KEY=VALUE,...   comma separated KEY=VALUE pairs to set Fab env vars
#   --shortlist           alias for -F short --list
#   -V, --version         show program's version number and exit
#   -a, --no_agent        don't use the running SSH agent
#   -A, --forward-agent   forward local agent to remote end
#   --abort-on-prompts    abort instead of prompting (for password, host, etc)
#   -c PATH, --config=PATH
#                         specify location of config file to use
#   --colorize-errors     Color error output
#   -D, --disable-known-hosts
#                         do not load user known_hosts file
#   -e, --eagerly-disconnect
#                         disconnect from hosts as soon as possible
#   -f PATH, --fabfile=PATH
#                         python module file to import, e.g. '../other.py'
#   -g HOST, --gateway=HOST
#                         gateway host to connect through
#   --gss-auth            Use GSS-API authentication
#   --gss-deleg           Delegate GSS-API client credentials or not
#   --gss-kex             Perform GSS-API Key Exchange and user authentication
#   --hide=LEVELS         comma-separated list of output levels to hide
#   -H HOSTS, --hosts=HOSTS
#                         comma-separated list of hosts to operate on
#   -i PATH               path to SSH private key file. May be repeated.
#   -k, --no-keys         don't load private key files from ~/.ssh/
#   --keepalive=N         enables a keepalive every N seconds
#   --linewise            print line-by-line instead of byte-by-byte
#   -n M, --connection-attempts=M
#                         make M attempts to connect before giving up
#   --no-pty              do not use pseudo-terminal in run/sudo
#   -p PASSWORD, --password=PASSWORD
#                         password for use with authentication and/or sudo
#   -P, --parallel        default to parallel execution method
#   --port=PORT           SSH connection port
#   -r, --reject-unknown-hosts
#                         reject unknown hosts
#   --sudo-password=SUDO_PASSWORD
#                         password for use with sudo only
#   --system-known-hosts=SYSTEM_KNOWN_HOSTS
#                         load system known_hosts file before reading user
#                         known_hosts
#   -R ROLES, --roles=ROLES
#                         comma-separated list of roles to operate on
#   -s SHELL, --shell=SHELL
#                         specify a new shell, defaults to '/bin/bash -l -c'
#   --show=LEVELS         comma-separated list of output levels to show
#   --skip-bad-hosts      skip over hosts that can't be reached
#   --skip-unknown-tasks  skip over unknown tasks
#   --ssh-config-path=PATH
#                         Path to SSH config file
#   -t N, --timeout=N     set connection timeout to N seconds
#   -T N, --command-timeout=N
#                         set remote command timeout to N seconds
#   -u USER, --user=USER  username to use when connecting to remote hosts
#   -w, --warn-only       warn, instead of abort, when commands fail
#   -x HOSTS, --exclude-hosts=HOSTS
#                         comma-separated list of hosts to exclude
#   -z INT, --pool-size=INT
#                         number of concurrent processes to use in parallel mode

