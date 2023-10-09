"""
The module to convert root file's trees into csv files
"""
from os import sys
from enum import Enum
import uproot
from pathlib import Path
from typing import Dict
import awkward as ak
from enum import Enum
from progress.bar import IncrementalBar


class file_type(Enum):
    csv = 1,
    excel = 2,
    pdf = 3

def __open_file(path:str):
    '''
        Opens root file for reading
    '''

    if not Path(path).exists():
        raise FileNotFoundError(f'Root file not found: {path}')           
    file = uproot.open(path)
    if not file:
        raise ValueError(f"No data inside the root file: {path}")

    return file

def __get_trees(file) -> list:
    '''
        Gets trees in the root file
    '''
    trees = file.keys()
    if not trees:
        raise ValueError(f"No trees found in the file")       
    
    return trees 

def __export(root_path:str, export_to:str, export_type:file_type=file_type.csv):

    try:
        import os

        file = __open_file(root_path)
        trees = __get_trees(file)

        if export_to == "" or export_to == None:
            export_to = os.path.join(Path.home(), Path(root_path).stem) #export to home folder
        
        print(f"Exporting to = {export_to}")
        if not Path(export_to).exists():
            os.mkdir(export_to)
        
        bar = IncrementalBar('Exporting...', max = len(trees))

        for tree in trees:
            branches = file[tree].keys()
            df = ak.to_dataframe(file[tree].arrays(branches))

            if export_type == export_type.csv:
                df.to_csv(os.path.join(export_to, f'{tree}.csv'), header=True
                                                                , index=False
                                                                , chunksize=100000
                                                                # , compression='gzip'
                                                                , encoding='utf-8-sig')
            bar.next()

        bar.finish()   
    except Exception as e:
        # logger.error(f'Failed to open {root_path}. Reason: {e}')
        print(f'Failed to open {root_path}. Reason: {e}')
        raise    

def export_to_csv(root_path:str, export_to:str=""):
    '''
        Exports root file into one more csv files
    '''   
    __export(root_path, export_to, file_type.csv)

# if __name__ == "__main__":
#     export_to_csv(r"C:\5.VAC\Tasks\Root Analysis\RootFiles\GF Singapore\__1.root", "ADT_Comparison1")