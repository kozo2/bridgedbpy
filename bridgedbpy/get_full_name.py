import sys
import pandas

def get_full_name(syscode):
    df = pandas.read_csv("https://github.com/bridgedb/datasources/raw/main/datasources.tsv", sep="\t", header=None)
    if not (df[1] == syscode).any():
        sys.exit("You must provide a system code")
    else:
        return list(df[df[1] == syscode][0])[0]
