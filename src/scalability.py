import random
import seaborn
from matplotlib import pyplot as plt
from matcher import match 
from verifier import verify
from time import time_ns

def test_time(callback, name):
    count = 12
    x_axis = []
    y_axis = []
    for i in range(0, count):
        n = 2**i
        possible = range(1, n + 1)
        h = [
            random.sample(possible, n) for y in range(0, n)
        ]
        a = [
            random.sample(possible, n) for y in range(0, n)
        ]
        # Run matcher
        start = time_ns()
        callback(n, h, a)
        duration = time_ns() - start
        x_axis.append(n)
        y_axis.append(duration)
    
    plot = seaborn.lineplot(x=x_axis, y=y_axis, label=name)
    

if __name__ == "__main__":
    random.seed(1)

    def both(n, h, a):
        # copy these since they will be modified by match()
        h2 = [row[:] for row in h]
        a2 = [row[:] for row in a]
        matching = match(n, h, a)
        verify(n, h2, a2, matching)

    fig, ax = plt.subplots()

    # matcher only
    test_time(match, "Match only")
    # matcher + verifier
    test_time(both, "Match and verifier")

    ax.set_xlabel("n")
    ax.set_ylabel("Runtime (ns)")
    ax.set_title("Matching vs. Matching and Verifying")
    fig.savefig("img/graph.png")
