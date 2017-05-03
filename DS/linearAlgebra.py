import unittest
import math
from functools import reduce

##### VECTOR CACUL
def vector_add(v, w):
    return [ v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [ v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multipy(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multipy(1/n, vector_sum(vectors))

def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

def sum_of_squares(v):
    return dot(v, v)

def magnituede(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnituede(vector_subtract(v, w))

##### MATRIX CACUL
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_col(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0


##### TEST SECTION #####
class TestForVectorCacul(unittest.TestCase):
    def test_vector_add(self):
        self.assertEqual(vector_add([1,2], [2,1]), [3,3])
    def test_vector_subtract(self):
        self.assertEqual(vector_subtract([1,2],[2,1]), [-1, 1])
    def test_vector_sum(self):
        self.assertEqual(vector_sum([[1,0],[0,1]]), [1,1])
    

if __name__ == '__main__':
    unittest.main()
