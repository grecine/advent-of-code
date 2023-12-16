import time
import aoctools.utils


def HASH(s):
    val = 0
    for i in s:
        val = (17 * (val + ord(i))) % 256
    return val


def part1(steps):
    print(sum([HASH(s) for s in steps]))


def part2(steps):
    boxes = [[] for _ in range(256)]

    for step in steps:
        label, f = step.replace('-','=').split('=')
        n = HASH(label)
        if f == '':
            boxes[n] = [b for b in boxes[n] if b[0]!=label]
        else:
            idx = [boxes[n].index(l) for l in boxes[n] if l[0]==label]
            if idx:
                boxes[n][idx[0]] = (label, f)
            else:
                boxes[n].append((label, f))

    tot = 0
    for x in [b for b in boxes if b != []]:
        tot += sum([(boxes.index(x)+1)*(x.index(n)+1)*int(n[1]) for n in x])

    print(tot)


def main():
    data = aoctools.utils.read_input('input.txt')
    # data = aoctools.utils.read_input('test-input.txt')

    steps = data[0].split(',')

    # part 1
    t0 = time.time()
    print('Part 1:')
    part1(steps)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')

    # part 2
    t0 = time.time()
    print('\nPart 2:')
    part2(steps)
    print('Elapsed time:',(time.time()-t0)*1E3,' ms')


if __name__ == "__main__":
    main()

