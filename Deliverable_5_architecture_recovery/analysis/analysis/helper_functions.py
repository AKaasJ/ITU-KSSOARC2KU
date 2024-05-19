
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def plot_len_files(df):
    fig, ax = plt.subplots()
    ax.bar(df.index, df.len_files)
    #ax.set_xticks(df.index, rotation=90)
    ax.tick_params(axis='x', labelrotation=90)
    
    return fig


def count_lines(input_str: str):
    return len(input_str.split("\n"))

def count_tabs(input_str: str):
    count = 0
    for line in input_str.split("\n"):
        count = line.count("\t")
    return count

def count_spaces(input_str: str):
    count = 0
    for line in input_str.split("\n"):
        stripped_line = line.lstrip()
        leading_whitespace = len(line) - len(stripped_line)
        count = count + leading_whitespace
    return count

def count_complexity(input_str : str, strategy = "tabs"):
    if strategy == "tabs":
        return count_tabs(input_str)
    if strategy == "prefix_spaces":
        return count_spaces(input_str)


def get_py_files(path):
    """ gets a list of all .py files in the given path.
    """
    files = []
    for file in Path(path).rglob("*.py"):
        # ignore init files
        if "__init__" not in file.name:
            files.append(file)
    return files