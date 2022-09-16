import os
import requests

PATHS = {
    "s3_train": "https://gic-hackathon.s3.ap-southeast-1.amazonaws.com/train.csv",
    "s3_test": "https://gic-hackathon.s3.ap-southeast-1.amazonaws.com/test.csv",
    "train": "train.csv",
    "test": "test.csv",
}

if __name__ == "__main__":
    req = requests.get(PATHS["s3_train"])
    if os.path.isfile(PATHS["train"]):
        os.remove(PATHS["train"])
    with open(PATHS["train"], mode="wb") as f:
        f.write(req.content)

    req = requests.get(PATHS["s3_test"])
    if os.path.isfile(PATHS["test"]):
        os.remove(PATHS["test"])
    with open(PATHS["test"], mode="wb") as f:
        f.write(req.content)
