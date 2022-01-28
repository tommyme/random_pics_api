import pickle
import os

pic_list = os.listdir("random_pics/")
with open("pic_list.pkl","wb") as f:
    pickle.dump(pic_list, f)

print("pic list dumped.")
