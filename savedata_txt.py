
# python savedata_txt.py *.txt -e . pkl
# python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py path of txt/180420-savedata.txt -e . pkl


import functools
from pathlib import Path, PosixPath

from joblib import Memory
import matplotlib as mpl
from matplotlib import pyplot as plt
import mplcursors
from nucleosome_unzipping import __main__ as nu
import numpy as np
import mplcursors
from qtlib.types import OpenFilesType
from tweezers import api as tz, get_option
from fleezers import gui as fz
# import os

def saveRawData(data_dir, export, specs, value):
    fname = None
    if data_dir is not None:
        data_path = data_dir.resolve()
        if data_path.is_file():
            fname = data_path.name
            data_path = data_path.parent
        global CONFIG
        CONFIG = {**fz.CONFIG, "data_dir": data_path}
        if export:
            dm = fz.DirModel(data_path)
            export_path, export_fmt = export
            export_path.mkdir(exist_ok=True, parents=True)
            if specs is not None:
                specs = [tuple(map(int, spec.split(":")))
                         for spec in specs.split(",")]
            fz.export_folder(
                dm, specs=specs, exported_value=value, suffix=export_fmt,
                dest=data_dir)
                # dest=export_path)
            return
    else:
        if export:
            raise ValueError("No data folder passed to --export")

# def main(path: Path, *,
#          save: bool = False):
def main(path: Path,
          data_dir: Path = None, *,
          export: fz.NamedTuple("_", DEST=Path, FMT=str) = None,
          # specs: str = None,
          value: fz.ExportedValue = fz.ExportedValue.BeadToBead):
    # or TrapToTrap
    # dirpath = path.with_suffix("")
    # print(dirpath)
    data_dir = path.parents[0]
    # print(data_dir)
    # data_dir = Path.cwd()
    # print(data_dir)
    with path.open() as file:
        for line in file:
            if line.startswith("#"):
                continue
            specs = line.rstrip().replace(' ', ':')
            # print("start to print:")
            print(data_dir,export,specs,value)
            saveRawData(data_dir,export,specs,value)
            # file = (dirpath.parent/name).with_suffix(".pkl")
            # fz.main._('/Volumes/Zhijie_Chen/Fleezers-data/180409');    
            # print(file
if __name__ == "__main__":
    import defopt
    defopt.run(main)