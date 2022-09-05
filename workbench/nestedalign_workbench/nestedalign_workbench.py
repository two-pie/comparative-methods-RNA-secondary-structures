#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import argparse


def __setup_driver():
    options = Options()

    # active headless mode
    options.add_argument('--headless')

    # use no sandbox
    options.add_argument('--no-sandbox')

    # suppress console output
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # create web driver
    dr = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    return dr


def __nestedalign(directory, df, driver):
    # list of molecules in the directory
    molecules = sorted(os.listdir(directory))

    # use list comprehension to get all pairs of molecules
    molecule_pairs = [(molecule_1, molecule_2) for i, molecule_1 in enumerate(molecules, start=1) for molecule_2 in
                      molecules[i:]]
    i = 1
    # iterate over all pairs of molecules
    for molecule_1, molecule_2 in molecule_pairs:
        print(f'{i}/{len(molecule_pairs)}')
        i += 1
        with open(os.path.join(directory, molecule_1), 'r') as file_1:
            # get the content of the first molecule
            content_molecule_1 = file_1.read()
            with open(os.path.join(directory, molecule_2), 'r') as file_2:
                # get the content of the second molecule
                content_molecule_2 = file_2.read()

                # send the content of the two molecules to the website
                driver.find_element(By.ID, 'arn1').send_keys(f'>{molecule_1}\n{content_molecule_1}')
                driver.find_element(By.ID, 'arn2').send_keys(f'>{molecule_2}\n{content_molecule_2}')

                # click on the button to start the alignment
                driver.find_element(By.XPATH, '//*[@id="comparison_form"]/div/input[1]').click()

                # get the score
                score = driver.find_element(By.XPATH, "//*[@id='align_score']").text

                # return to the previous page
                driver.back()

                # reset the input fields
                driver.find_element(By.XPATH, '//*[@id="comparison_form"]/div/input[2]').click()

                # save the data in the dataframe
                df.loc[len(df)] = [molecule_1.split('.')[0], molecule_2.split('.')[0], score]


def csv(molecules_dir, output_file):
    # creating web driver
    driver = __setup_driver()

    # nagivate to nestedalign website
    driver.get('https://nestedalign.lri.fr/index.php')

    # remove unnecessary blank line created by selenium
    print("\033[F", end="")

    # create a csv file for each directory of molecules
    df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance'])
    # fill the dataframe with the data from the nestedalign website
    __nestedalign(molecules_dir, df, driver)

    # save the dataframe as a csv file
    df.to_csv(output_file, index=False)
    print(f'{output_file} created')

    # shutting down driver
    driver.quit()


parser = argparse.ArgumentParser(description='nesdtedalign tool')
parser.add_argument('molecules_dir', help='directory containing all molecules in db format (without header)')
parser.add_argument('output_file_csv',
                    help='file used to store the calculation as csv file. if the file does not exist it is created, '
                         'otherwise it is overwritten')
args = parser.parse_args()
csv(args.molecules_dir, args.output_file_csv)
