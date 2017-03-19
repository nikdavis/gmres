import subprocess
import argparse
import uuid
import os
import sys
from datetime import datetime

#get custom name
git_sha = subprocess.check_output('git rev-parse --short HEAD'.split(' ')).decode('utf-8').rstrip()
directory = './profiles/profile_' + git_sha + '_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

if not os.path.exists(directory):
    os.makedirs(directory)

stats_file = directory + '/profile.stats'
svg_file = directory + '/profile.svg'
comment_file = directory + '/comment.md'
time_file_handle = open(directory + '/time.txt', 'w')

profile_cmd = 'time python -m cProfile -o ' + stats_file + ' gmres_example.py'
prof_to_dot_cmd = 'gprof2dot -f pstats ' + stats_file
svg_gen_cmd = 'dot -Tsvg -o ' + svg_file

subprocess.call(['touch', comment_file])
subprocess.call(profile_cmd.split(' '), stderr=time_file_handle)
gen_dot_proc = subprocess.Popen(prof_to_dot_cmd.split(' '), stdout=subprocess.PIPE)
subprocess.call(svg_gen_cmd.split(' '), stdin=gen_dot_proc.stdout)

gen_dot_proc.wait()
