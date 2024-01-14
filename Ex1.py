import argparse
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Copy file to new dir")
    parser.add_argument('-i', '--input', type=Path,
                        required=True, help="Dir with input files")
    parser.add_argument('-o', '--output', type=Path,
                        default=Path('Dist'), help='Dir with the copied files')
    return parser.parse_args()


def recursive_copy(input_path: Path, output_path: Path):
    # Iterate over items in the input directory
    for item in input_path.iterdir():
        try:
            # Check if the item is a directory
            if item.is_dir():
                # If it's a directory, recursively call this function
                recursive_copy(item, output_path)
            else:
                # Extract the file extension, default to 'no_extension' if none
                extension = item.suffix[1:] or 'no_extension'
                # Create a new directory in the output path based on the file extension
                ext_dir = output_path / extension
                # Create the directory if it doesn't exist, including any parent directories
                ext_dir.mkdir(exist_ok=True, parents=True)
                # Copy the file to the new directory
                shutil.copy(item, ext_dir)
        except Exception as e:
            print(f"Error processing {item}: {e}")


def main():
    args = parse_args()
    # Set the input and output paths
    input_path = args.input
    output_path = args.output
    # Create the output directory if it doesn't exist
    output_path.mkdir(exist_ok=True)
    recursive_copy(input_path, output_path)


if __name__ == "__main__":
    main()
