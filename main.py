"""
Module to navigate json file.
"""
import json
import argparse


def parse():
    """
    parse the argument and read file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    with open(parser.parse_args().path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def process(current_folder, folder_name):
    """
    Recursive function for navigating json file.
    """
    while True:
        if isinstance(current_folder, list):
            print(f"You are currently in '{folder_name}' folder.")
            print(f"There are {len(current_folder)} elements in the folder.")
            print(f"Type in number from 1 to {len(current_folder)}.")
        elif isinstance(current_folder, dict):
            print(f"You are currently in '{folder_name}' folder.")
            print(
                f"Here is the list of subfolders names {current_folder.keys()}.")
            print("Choose the key.")
        else:
            print(f"{folder_name}: {current_folder}")
        print(f"Type in '.' to exit the folder")
        while True:
            print("Type 'exit' to quit the program")
            inp = input()
            if inp == '.':
                return
            if inp == 'exit':
                quit()
            if isinstance(current_folder, dict) and inp in current_folder.keys():
                if isinstance(current_folder[inp], list) and len(current_folder[inp]) == 1:
                    process(current_folder[inp][0], inp)
                else:
                    process(current_folder[inp], inp)
                break
            else:
                try:
                    inp = int(inp)
                    if isinstance(current_folder, list) and (inp - 1) <= len(current_folder) and inp >= 1:
                        process(current_folder[inp - 1],
                                folder_name + '/' + str(inp))
                        break
                except:
                    pass


def main():
    """
    The main function.
    """
    data = parse()
    process(data, 'main')


if __name__ == "__main__":
    main()
