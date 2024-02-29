from matplotlib import pyplot as plt

def custom_function(x: float, N: int, alpha: float) -> float:
    return N * ((x / N) + 0.5) ** alpha - N / 2

def tabulate_custom_function(a: float, b: float, n: int, N: int, alpha: float) -> dict:
    x = [a + i * (b - a) / n for i in range(n)]
    y = [custom_function(t, N, alpha) for t in x]
    return {'x': x, 'y': y}

def main():
    N = 5
    alpha = 0.5
    res = tabulate_custom_function(0, 1, 1000, N, alpha)

    plt.plot(res['x'], res['y'])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()