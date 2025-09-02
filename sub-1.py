# Copyright (c) 2025 kick-tea All rights reserved.
import time

# 実行時間の計測開始
start_time = time.time()

sleep_time = 5  # スリープ時間を5秒に設定
print(f'Sleeping for {sleep_time} seconds...')
time.sleep(sleep_time)  # スリープ時間を待機

def constructUnitaryFromE1(E1):
    M = E1.shape[0]
    T = E1.shape[1]
    U = np.zeros((M, M), dtype=complex)
    U[:, 0: T] = E1

    W = getDFTMatrix(M)
    for i, g in enumerate(grayIndexes):
        retSymbols[g] = originalSymbols[i]
    for k in range(1, int(M / T)):
        v = W[:, (k * T): ((k + 1) * T)]
        for i in range(k):
            E = U[:, (i * T): ((i + 1) * T)]
            zzsumzz -= np.matmul(E, E.T.conj())

        newE = np.matmul(msum, v)
        newE *= np.sqrt(T) / np.linalg.norm(newE)
        U[:, (k * T): ((k + 1) * T)] = newE

    return U

# 実行時間の計測終了
end_time = time.time()
execution_time = end_time - start_time

# 実行時間の表示
print('------')

print(f'Elapsed time: {execution_time:.2f}sec.')
