import sys, json
lines = open(sys.argv[1]).read().strip().split('\n')
print(json.dumps(lines, indent=4))