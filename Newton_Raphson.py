def newton_raphson(func, deriv, t0, tol=1e-6, max_iter=100):
    t = t0
    for i in range(max_iter):
        ft = func(t)
        dft = deriv(t)
        if dft == 0:
            print("The derivative at this point is zero")
            return None
        t_new = t - ft / dft
        if abs(t_new - t) < tol:
            print(f" Approximate root: x = {t_new}، after {i+1} repetition")
            return t_new
        t = t_new
    print("We reached the maximum number of repetitions.")
    return t
func = lambda x: x** 2 - 2
deriv = lambda x: 2 * x
t0 = 1.0
root = newton_raphson(func, deriv, t0)
print("Approximate root", root)
