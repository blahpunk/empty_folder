<<<<<<< HEAD
# empty_folder
Simple python script to recursively remove empty folders from the specified path
=======
# Empty Folder Script

This script recursively deletes specified file types and removes empty folders within the given directory paths.

## Usage

```sh
python empty_folder.py <path1> <path2> ... -ext1 -ext2 ...
```

### Example

```sh
python empty_folder.py P:\Path\DataStore_5\0jT5skIo -txt -nfo -exe
```

This command will recursively delete `.txt`, `.nfo`, and `.exe` files and then remove empty folders within the directory `0jT5skIo`.

## Requirements

- Python 3.x
- tqdm
- colorama

## Installation

Install the required packages using pip:

```sh
pip install tqdm colorama
```
>>>>>>> 3735a5e (Initial commit)
