from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import time


def __setup_driver(url):
    options = Options()
    options.add_argument('--headless')
    dr = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    dr.get(url)
    return dr


def __workbench(molecules_dir, output_dir, driver):
    df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance', 'Execution time [ns]'])
    molecules = os.listdir(molecules_dir)
    for i, filename_1 in enumerate(sorted(molecules), start=1):
        with open(os.path.join(molecules_dir, filename_1), 'r') as f:
            molecules_1 = f.read()
            for filename_2 in molecules[i:]:
                with open(os.path.join(molecules_dir, filename_2), 'r') as f:
                    molecules_2 = f.read()
                    driver.find_element(By.ID, 'arn1').send_keys(f'>{filename_1}\n{molecules_1}')
                    driver.find_element(By.ID, 'arn2').send_keys(f'>{filename_2}\n{molecules_2}')
                    initial_time = time.time_ns()
                    driver.find_element(By.XPATH, '//*[@id="comparison_form"]/div/input[1]').click()
                    final_time = time.time_ns() - initial_time
                    score = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/h5[1]/span").text
                    df.loc[len(df)] = [filename_1, filename_2, score, final_time]
                    driver.back()
                    driver.find_element(By.XPATH, '//*[@id="comparison_form"]/div/input[2]').click()
    df.to_csv(output_dir, index=False)


def csv(molecules, output_dir):
    # creating web driver
    driv = __setup_driver('https://nestedalign.lri.fr/index.php')

    # creating csv for each molecule
    for molecules, output_dir in zip(molecules, output_dir):
        __workbench(molecules, output_dir, driv)

    # closing web driver
    driv.quit()
