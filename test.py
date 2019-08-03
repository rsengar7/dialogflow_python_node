def multipliers():
    return [lambda x: i*x for i in range(4)]

# print([m(3) for m in multipliers()])

# print(multipliers())
import numpy as np

# i = 5 if a > 7 else 0
#--------------------------------------------------------------------------------------------
# def negate_some(x):
#     return -x

# def negate_some(x):
#     return x[(x >= 1) & (x <= 3)] * -1


# def negate_some(x):
#     x[1:-1] *= -1; return x

def negate_some(x):
    x[(x >= 1) & (x <= 3)] *= -1; return x

x1 = negate_some(np.arange(4))

assert (x1 == np.array([0, -1, -2, -3])).all()

x2 = negate_some(np.arange(5))

assert (x2 == np.array([0, -1, -2, -3, 4])).all()
#--------------------------------------------------------------------------------------------
# get_closest = lambda x, c: np.abs(x - c).min()
# get_closest = lambda x, c: x[[(x - c).argmin()]
get_closest = lambda x, c: x[np.abs(x - c).argmin()]
# get_closest = lambda x, c: np.sort(x - c)[0]




x = np.array([3.431, 7.290, 4.385, 0.596, 3.980, 7.379, 1.824, 1.754, 5.315, 5.318])

c = 6.344
assert get_closest(x, c) == 7.29

#--------------------------------------------------------------------------------------------

# get_product_diag = lambda A, B: np.diag(np.dot(A, B))
# get_product_diag = lambda A, B: np.sum(A * B, axis=1)         # Not operatable
get_product_diag = lambda A, B: np.sum(A * B.T, axis=1)
# get_product_diag = lambda A, B: np.einsum("ij,ji->i", A, B)


A = np.arange(9).reshape(3, 3)

B = np.arange(9).reshape(3, 3)

trace = get_product_diag(A, B)

assert (trace == np.array([ 15,  54, 111])).all()
#--------------------------------------------------------------------------------------------

# A.indptr = array([0, 1, 3, 4])
# A.indices = array([2, 0, 1, 2])
# A.data = array([9, 5, 8, 1])

# # A.indptr = array([0, 1, 2, 4])
# # A.indices = array([1, 1, 0, 2])
# # A.data = array([5, 8, 9, 1])

# A.indptr = array([0, 1, 1, 2])
# A.indices = array([2, 0, 1, 2])
# A.data = array([9, 5, 8, 1])

# print(A)

#--------------------------------------------------------------------------------------------
from scipy.sparse import csr_matrix

mat = csr_matrix((100, 200), dtype=np.int8).toarray()
print(type(mat))
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]], dtype=int8)
print()
no = 0
mat1 = []
for item in mat:
    mat2 = []
    # print(item)
    for index,i in enumerate(item):
        if index <=9:
            mat2.append(np.random.randint(1,10))
        else:
            mat2.append(0)
        # print(mat2)
    mat1.append(mat2)
arr = np.array(mat1)

x = csr_matrix(arr)

print(x.indptr.astype(np.int32).nbytes + x.indices.astype(np.int32).nbytes + x.data.astype(np.float64).nbytes)

#--------------------------------------------------------------------------------------------

import torch

from torch import nn

conv = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=0)

b, c, h, w = 16, 16, 16, 16

x = torch.zeros((b, c, h, w))

print(tuple(conv(x).shape))