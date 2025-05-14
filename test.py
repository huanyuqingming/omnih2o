import joblib
from itertools import islice

data_path = "/home/szsh/ztj/human2humanoid/legged_gym/resources/motions/h1/amass_phc_filtered.pkl"
# data_path = "/home/szsh/ztj/human2humanoid/legged_gym/resources/motions/h1/stable_punch.pkl"

data = joblib.load(data_path)


print(type(data))
# print(data.keys() if isinstance(data, dict) else dir(data))
print(len(data))

# n = 1
# first_item = dict(islice(data.items(), n, n + 1))

# print(type(first_item))
# print(first_item.keys())

