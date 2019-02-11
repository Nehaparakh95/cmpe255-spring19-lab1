import math


def normal_pdf(x, mu=0, sigma=1):
    # TODO
    # hits: math.exp
    term1 = 1 / (math.sqrt(2 * math.pi * sigma * sigma))
    term2 = math.exp(-((x - mu) * (x - mu)) / (2 * sigma * sigma))
    f = term1 * term2
    return f


from matplotlib import pyplot as plt

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()