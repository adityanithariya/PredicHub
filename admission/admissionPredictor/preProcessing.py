import argparse
from os import path, makedirs

parser = argparse.ArgumentParser(description = "Command Line Utility for preprocessing standard Admission data")
parser.add_argument("src", help = "Source csv format file path")
parser.add_argument("-d", "--desc", help = "Destination for the processed file, if not specified then processed file will be saved in 'processed' folder")
args = parser.parse_args()

if args.desc != None:
    desc = args.desc
else:
    desc = "processed"

if not path.exists(desc):
    makedirs(desc)
import pandas as pd

data = pd.read_csv(args.src)
pd.get_dummies(data, drop_first=True).to_csv(f"{desc}/" + args.src.split("\\")[-1].split("/")[-1], index=False)