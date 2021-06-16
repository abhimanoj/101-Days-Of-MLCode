
from utils import *


def test_error():
    raise DataError("error is here")

try:
    test_error()
except  (DataError) as e:
    print("errro",e)


