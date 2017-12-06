import random


def pso(x_min, x_max, num, c1, c2, iters, dir):
    g = [[0, 0]] * 2
    f = []
    v = [0] * num
    p = [[0, 0]] * num
    for i in range(num):
        f.append([random.uniform(x_min, x_max), 0])
    iter = 0
    while (iter < iters):
        for i in range(num):
            f[i][1] = f[i][0] ** 3 - 5 * f[i][0] ** 2 - 2 * f[i][0] + 3
            if dir & (f[i][1] > p[i][1]):
                p[i][0] = f[i][0]
                p[i][1] = f[i][1]
                if p[i][1] > g[1][1]:
                    g[1] = p[i].copy()
            elif ~dir & (f[i][1] < p[i][1]):
                p[i][0] = f[i][0]
                p[i][1] = f[i][1]
                if p[i][1] < g[1][1]:
                    g[1] = p[i].copy()
            v[i] = v[i] + c1 * random.random() * (p[i][0] - f[i][0]) + c2 * random.random() * (g[1][0] - f[i][0])
            f[i][0] = f[i][0] + v[i]
            if f[i][0] < x_min:
                f[i][0] = x_min
            elif f[i][0] > x_max:
                f[i][0] = x_max
        if g[0] == g[1]:
            iter += 1
        else:
            g[0] = g[1].copy()
            iter = 0
    return g[1]


if __name__ == '__main__':
    print(pso(-2, 5, 5, 2, 2, 50, False))
