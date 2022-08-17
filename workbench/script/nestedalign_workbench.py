from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os


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

    # iterate over all pairs of molecules
    for molecule_1, molecule_2 in molecule_pairs:
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
                df.loc[len(df)] = [os.path.splitext(molecule_1)[0], os.path.splitext(molecule_2)[0], score]


def csv(molecules_dirs, output_files):
    # creating web driver
    driver = __setup_driver()

    # nagivate to nestedalign website
    driver.get('https://nestedalign.lri.fr/index.php')

    # remove unnecessary blank line created by selenium
    print("\033[F", end="")

    # create a csv file for each directory of molecules
    for directory, output in zip(molecules_dirs, output_files):
        # create a dataframe for the csv file
        df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance', 'Execution time [ns]'])

        # fill the dataframe with the data from the nestedalign website
        __nestedalign(directory, df, driver)

        # save the dataframe as a csv file
        df.to_csv(output, index=False)
        print(f'{output} created')

    # shutting down driver
    driver.quit()
