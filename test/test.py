from sympy import init_printing
from sympy import symbols
from sympy import sin
from sympy import cos
from sympy import integrate
from sympy import Matrix

from numpy import array
from pandas import DataFrame
from pandas import Timestamp
from pandas import Series
from pandas import Categorical

from IPython.display import Image

import matplotlib.pyplot as plt
import numpy as np

init_printing(use_latex='mathjax')

M = Matrix([[1, 2, 3], [1, 2, 3]])
M
N = Matrix([1, 2, 3])
N
M * N

Image('http://jakevdp.github.com/figures/xkcd_version.png')

dataframe = DataFrame({'A': 1.,
                       'B': Timestamp('20130102'),
                       'C': Series(1, index=list(range(4)), dtype='float32'),
                       'D': array([3] * 4, dtype='int32'),
                       'E': Categorical(["test", "train", "test", "train"]),
                       'F': 'foo'})

dataframe

%matplotlib inline
%config InlineBackend.figure_format = 'svg'
t = np.linspace(0, 20, 500)

plt.plot(t, np.sin(t))
plt.show()
