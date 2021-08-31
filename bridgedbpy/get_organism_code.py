import sys
import pandas

def get_organism_code(name):
    df = pandas.read_csv("https://github.com/bridgedb/datasources/raw/main/organisms.tsv", sep="\t")
    if name == "Unspecified":
        return "Uns"
    elif not (df['generic_name'] + " " + df['specific_name'] == name).any():
        sys.exit("Unknown species:" + name)
    else:
        return list(df[df['generic_name'] + " " + df['specific_name'] == name]['symbol'])[0]
