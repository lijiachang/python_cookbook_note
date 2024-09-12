import itertools

with open('/etc/passwd') as f:
    for line in itertools.dropwhile(lambda l: l.startswith('#'), f):
        print(line)

