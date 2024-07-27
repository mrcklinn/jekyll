"""
This script processes CSV and Markdown files in a specified directory to generate JSON files 
for a web portfolio.
"""

import os
import json
import pandas as pd

# Define working and public directories
RAW_DIR = './data/md/'          # Directory containing CSV and Markdown files
JSON_DIR = './data/json/'       # Directory to store generated JSON files

def list_csv_files(working_dir):
    """Lists all CSV files in the specified working directory.

    Args:
        working_dir (str): Path to the working directory.

    Returns:
        list: A list of CSV file names.
    """
    return [file for file in os.listdir(path=working_dir) if file.endswith('.csv')]

def list_subdirectories(working_dir):
    """Lists all subdirectories in the specified working directory.

    Args:
        working_dir (str): Path to the working directory.

    Returns:
        list: A list of subdirectory names.
    """
    return next(os.walk(working_dir))[1]

def process_markdown_files(subdirectory, working_dir):
    """Processes Markdown files in a given subdirectory and creates a dictionary.

    Args:
        subdirectory (str): Name of the subdirectory.
        working_dir (str): Path to the working directory.

    Returns:
        dict: A dictionary mapping article indices to file names.
    """
    articles = [file for file in os.listdir(path=working_dir + subdirectory) if file.endswith('.md')]
    article_dict = {}
    for i, article in enumerate(articles):
        article_dict[f"article_{i}"] = article
    return article_dict

def process_csv_files(link_list, working_dir, item_number, dict_json):
    """Processes CSV files and adds their content to the main JSON dictionary.

    Args:
        link_list (list): A list of CSV file names.
        working_dir (str): Path to the working directory.
        item_number (int): Starting index for JSON items.
        dict_json (dict): The main JSON dictionary.

    Returns:
        tuple: A tuple containing the updated item number and the modified JSON dictionary.
    """
    for link in link_list:
        local_list = pd.read_csv(working_dir + link)
        local_list.columns = ['name', 'href']
        for row in range(len(local_list)):
            dict_json[f'item_{item_number}'] = {
                "group": "link",
                "name": local_list['name'][row],
                "href": local_list['href'][row]
            }
            item_number += 1
        dict_json[f'item_{item_number}'] = {"group": "spacer"}
        item_number += 1
    return item_number, dict_json

def save_json(data, filename):
    """Saves the given data as a JSON file.

    Args:
        data (dict): The data to be saved.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as js_file:
        json.dump(data, js_file, indent=3)

def save_js(data, filename):
    """Saves the given data as a JavaScript file.

    Args:
        data (str): The data to be saved.
        filename (str): The name of the output JavaScript file.
    """
    with open(filename, 'w', encoding='utf-8') as js_file:
        js_file.write(data)

def main():
    """Main function to orchestrate the entire process.

    This function initializes counters, processes subdirectories and CSV files, 
    and generates the necessary JSON and JavaScript files for the web portfolio.
    """
    item_number = 0  # Counter for items in the main JSON structure
    dict_json = {}   # Main JSON dictionary to store all items

    link_list = list_csv_files(RAW_DIR)
    subdirectories = list_subdirectories(RAW_DIR)
    
    for subdir in subdirectories:
        dict_json[f'item_{item_number}'] = {
            "name": subdir.capitalize(),    # Folder name capitalized
            "file": f'{subdir}.json',       # Name of the JSON file for this folder
            "group": "modal"        
        }

        article_dict = process_markdown_files(subdir, RAW_DIR)
        save_json(article_dict, f'{JSON_DIR}{subdir}.json')

        item_number += 1

    dict_json[f'item_{item_number}'] = {"group": "spacer"}
    item_number += 1

    item_number, dict_json = process_csv_files(link_list, RAW_DIR, item_number, dict_json)

    inverse_dict = dict(sorted(dict_json.items(), reverse=False))
    json_dict = json.dumps(inverse_dict, indent=3)

    js_object = "menu_items = " + str(json_dict) + ';\nexport let menu_items;'
    save_js(js_object, f'{JSON_DIR}menu_items.js')

if __name__ == '__main__':
    main()
