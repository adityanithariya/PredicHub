from argparse import ArgumentParser
from os import path, mkdir, system
from shutil import rmtree
import pandas as pd

parser = ArgumentParser(description = "Command Line Utility for merging preprocessed Admission data")

parser.add_argument("srcs", help = "Source csv format file path", nargs="+")
parser.add_argument("-c", "--clgnames", help="Index wise custom college names, if not specified 'clg1'... will be used", nargs="+")
parser.add_argument("-d", "--desc", help = "Destination for the merged file, if not specified then merged file will be saved in 'final_data' folder")
parser.add_argument("-f", "--filename", help = "File name given to the final database file")
args = parser.parse_args()

if args.desc != None:
    desc = args.desc
else:
    desc = "data"

if args.filename != None:
    file = args.filename
else:
    file = "final"

if not path.exists("cache/"):
    mkdir("cache/")

data = pd.DataFrame()
for n, i in enumerate(args.srcs):
    df = pd.read_csv(i)

    if args.clgnames != None:
        df["college"] = args.clgnames[n]
        if file == "final":
            file = "_".join(args.clgnames)
    else:
        df["college"] = f"clg{n}"
    
    df.to_csv("cache/" + i.split('\\')[-1].split("/")[-1], index=False)
    data = pd.concat([data, df], axis="rows")

data.to_csv(f"cache/db_{file}.csv", index=False)
system(f"python preProcessing.py ./cache/db_{file}.csv -d {desc}")

rmtree("cache")
