import os
import matplotlib.pyplot as plt
import imageio
import random
import math

random.seed(37)

def cal_pi(n):
    in_c = 0
    out_c = 0

    in_c_x = []
    out_c_x = []
    in_c_y = []
    out_c_y = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x ** 2 + y ** 2)

        if distance < 1:
            in_c += 1
            in_c_x.append(x)
            in_c_y.append(y)
        else:
            out_c += 1
            out_c_x.append(x)
            out_c_y.append(y)
    total = in_c + out_c
    pi = in_c * 4 / total
    return pi, in_c_x, in_c_y, out_c_x, out_c_y

def plot(n):
    pi, in_c_x, in_c_y, out_c_x, out_c_y = cal_pi(n)
    fig = plt.figure(figsize = (8, 8))
    plt.plot(in_c_x, in_c_y, 'ro', label = 'Inside circle')
    plt.plot(out_c_x, out_c_y, 'bo', label = 'Outside circle')
    plt.xlabel('')
    plt.ylabel('')
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.title(f'Random {n} times')
    plt.legend(loc = 'upper right')

    plt.text(-0.18, -1.3, f'Pi = {pi:0.4f}', fontsize = 12, bbox = dict(facecolor = 'green', alpha = 0.5))
    fig.savefig(f'pigif\\{n:09d}.png')
    plt.close(fig)

n = [3, 10, 50, 100, 300, 700, 1000, 3000, 7000, 10000, 30000, 70000, 100000, 500000]

def main():
    for i in n:
        plot(i)

    with imageio.get_writer('pigif.gif', mode = 'I', duration = 0.5) as writer:
        for filename in os.listdir('pigif'):
            img = imageio.imread(f'pigif\\{filename}')
            writer.append_data(img)

if __name__ == '__main__':
    main()

