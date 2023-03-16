import sys
import time

def ft_progress(listy):
    inicio_time = time.time()
    relation = len(listy) // 4
    for i, elems in enumerate(listy):
        yield elems
        elapsed_time = time.time() - inicio_time
        eta = elapsed_time / (i + 1) * (len(listy) - i - 1)
        percent = (i + 1) / len(listy) * 100
        sys.stdout.write("\rETA: {:0.2f}s [ {:2.0f}% ][{}] {}/{} | elapsed time {:0.2f}s".format(
            eta, percent, "".join(['#' if i * 100 / 20 <= elems * 100 / len(listy) else ' ' for i in range(20)]), i + 1, len(listy), elapsed_time))
        sys.stdout.flush()

listy = range(1000)
ret = 0
inicio_time = time.time()
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print("\nTime elapsed: {:.2f}s".format(time.time() - inicio_time))
print(ret)
