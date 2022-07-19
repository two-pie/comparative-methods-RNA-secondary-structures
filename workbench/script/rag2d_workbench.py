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


def __rag2d(directory, output, driver):
    # list of molecules in the directory
    molecules = sorted(os.listdir(directory))

    # iterate over all pairs of molecules
    for m in molecules:
        # click on the button to upload file
        e = driver.find_element(By.XPATH,
                                '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/div['
                                '3]/div/div/div/div/div/div/div/div/form/fieldset/p[1]/input[2]').click()

        # send path file to the website
        e.send_keys(os.path.join(directory, m))

        # click on the button to send file
        driver.find_element(By.XPATH,
                            '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/div['
                            '3]/div/div/div/div/div/div/div/div/form/fieldset/p[6]/input[1]').click()

        # get the rna matrix
        var = driver.find_element(By.XPATH,
                                  '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/div['
                                  '3]/div/div/div/div/div/div/div/div/pre').text

        print('****' + var)

        # save the matrix in outputfile
        # with open(os.path.join(output), 'w') as file:

        # return to the previous page
        driver.back()


def csv(molecules_dirs, output_files):
    # creating web driver
    driver = __setup_driver()

    # nagivate to nestedalign website
    driver.get('http://www.biomath.nyu.edu/?q=rag/rna_matrix')

    # create a txt file for each file of molecules of all directories
    for directory, output in zip(molecules_dirs, output_files):
        # write matrixes to txt files
        __rag2d(directory, output, driver)
        print(f'{output} created')

    # shutting down driver
    driver.quit()
