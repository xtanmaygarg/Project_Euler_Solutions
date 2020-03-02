from functools import reduce

from itertools import combinations_with_replacement as c;
from string import digits as d
n = lambda num, digits: sorted(str(num)) == sorted(digits)
p = lambda comb: sum([int(n) ** 5 for n in comb])
print(sum(set(reduce(list.__add__, ([p(cb) for cb in c(d, x) if n(p(cb), cb)] for x in range(7))))))
