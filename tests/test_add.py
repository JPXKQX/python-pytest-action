from pkg_name.ops import add_squared
import random
import torch

def test_op():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)

    res = torch.tensor(x ** 2 + y ** 2)
    op_res = add_squared(torch.tensor(x), torch.tensor(y))
    assert res == op_res, f"add_squared({x}, {y}) returns {op_res} != {res}"
