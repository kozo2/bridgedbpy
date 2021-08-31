import sys
import pandas

def get_system_code(name):
    df = pandas.read_csv("https://github.com/bridgedb/datasources/raw/main/datasources.tsv", sep="\t", header=None)
    if not (df[0] == name).any():
        sys.exit("Unknown name:" + name)
    else:
        return list(df[df[0] == name][1])[0]
