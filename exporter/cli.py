"""
The command-line interface for the exporter
"""
import argparse
from .root_exporter import export_to_csv

def main():
    parser = argparse.ArgumentParser(
        description="Tool to export ROOT file data into different formats such a csv."
    )
    parser.add_argument(
        "root_path", type=str,
        help="The path of the ROOT file to be exported."
    )
    parser.add_argument(
        "--output", "-o",
        help=("Destination folder path. If not set, a folder with same name as the ROOT file "
                "will be created in HOME directory and files will be exported in it.")
    )
    args = parser.parse_args()
    print("Starting to Export...")
    export_to_csv(args.root_path, export_to=args.output)
    print("Exported successfully!")

if __name__ == "__main__":
    main()