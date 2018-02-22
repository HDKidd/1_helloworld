# !usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess

# 子进程 subprocess

# 1.1 启动一个外部子进程nslookup
print('========1.1========')

print(' $ nslookup www.python.org')   # nslookup可以通过主机名查找IP，或反向
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


# 1.2 子进程输入：communicate()   暂跳过
print('========1.2========')

print(' $ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b' set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
