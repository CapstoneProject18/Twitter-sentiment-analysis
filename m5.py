import os
import re
log_file = ("C:\\Users\\764024\\Desktop\\exercises\\sample_log.txt")


exception_lines = []
keep_phrases = ["Exception","Error"]

with open(log_file) as f:
    line = f.readline()
    while line:
        for phrase in keep_phrases:
            if phrase in line:
                exception_lines.append(line)
                print(exception_lines)
        line = f.readline()
