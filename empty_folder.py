import os
import sys
from colorama import Fore, Style, init
from tqdm import tqdm

init()

def delete_empty_folders(paths, progress_bar):
    for path in paths:
        for root, dirs, files in os.walk(path, topdown=False):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    os.rmdir(dir_path)
                    tqdm.write(f"{Fore.GREEN}Deleted empty folder: {dir_path}{Style.RESET_ALL}")
                    progress_bar.update(1)
                except OSError:
                    pass

def delete_files(paths, extensions, progress_bar):
    for path in paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                for ext in extensions:
                    if file.lower().endswith(ext):
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        tqdm.write(f"{Fore.RED}Deleted file: {file_path}{Style.RESET_ALL}")
                        progress_bar.update(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path1> <path2> ... -ext1 -ext2 ...")
        return

    paths = []
    extensions = []

    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            extensions.append(arg[1:])
        else:
            paths.append(arg)

    if not paths:
        paths.append(os.getcwd())

    total_items = sum(len(dirs) + len(files) for path in paths for _, dirs, files in os.walk(path))
    progress_bar = tqdm(total=total_items, desc="Processing", unit="item", ncols=80, position=0, leave=True)

    if extensions:
        delete_files(paths, extensions, progress_bar)
    delete_empty_folders(paths, progress_bar)

    progress_bar.close()

if __name__ == "__main__":
    main()
