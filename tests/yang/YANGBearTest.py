import requests

from bears.yang.YANGBear import YANGBear
from coalib.testing.LocalBearTestHelper import verify_local_bear


VALID = requests.get(
    'https://raw.githubusercontent.com/OpenNetworkingFoundation/CENTENNIAL'
    '/master/models/yang/core-model.yang'
).text


# several missing module sub-statements
INVALID = """
module invalid-yang {

  namespace "http://coala.io/invalid-yang";
  prefix invalid;
}
"""


YANGBearTest = verify_local_bear(
    YANGBear, valid_files=(VALID, ), invalid_files=(INVALID, ))
