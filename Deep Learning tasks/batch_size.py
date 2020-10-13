def generate_batches(X, y, batch_size):
    assert len(X) == len(y)
    np.random.seed(42)
    X = np.array(X)
    y = np.array(y)
    perm = np.random.permutation(len(X))
    cur = 0
    stop = len(X) // batch_size
    while cur < stop*batch_size:
        yield X[perm][cur : cur + batch_size,], y[perm][cur : cur + batch_size,]
        cur += batch_size