import time
import os

def get_commands(fname):
    day_dir = os.path.realpath(__file__).split('/')[:-1]
    fname = os.path.join('/',*day_dir, fname)

    commands = []
    with open(fname) as f:
        for line in f:
            commands.append([l.strip() for l in line.split(' ')])
    return commands

def part1(coms):
    # h, v
    pos = [0 , 0]
    for c, val in coms:
        if c == 'forward':
            pos[1] = pos[1]+int(val)
        elif c == 'down':
            pos[0] = pos[0]+int(val)
        elif c == 'up':
            pos[0] = pos[0]-int(val)

    print('Part 1:',pos[0]*pos[1])

def part2(coms):
    # h, v, aim
    pos = [0 , 0, 0]
    for c, val in coms:
        if c == 'forward':
            pos[1] = pos[1]+int(val)
            pos[0] = pos[0] + pos[2]*int(val)
        elif c == 'down':
            pos[2] = pos[2]+int(val)
        elif c == 'up':
            pos[2] = pos[2]-int(val)

    print('Part 2:',pos[0]*pos[1])

# fname = 'test-input.csv'
fname = 'input.csv'

commands = get_commands(fname)

t0 = time.time()
part1(commands)
print('Part 1 took '+str(time.time()-t0)+' sec')

t0 = time.time()
part2(commands)
print('Part 2 tool '+str(time.time()-t0)+' sec')
