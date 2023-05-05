from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import pyperclip


class TestSeleniumFunctional:
    def test_get_pwd(self):
        """Opens the project and tests if a password is generated on btn click"""

        # options = Options()
        # options.binary_location = r'mnt/c/Program Files/Mozilla Firefox/firefox.exe'
        # Loads Geckodriver
        browser = webdriver.Firefox(
            service=Service(executable_path=GeckoDriverManager().install())  # ,
            # options=options
        )

        # Opens HE-Arc website.
        browser.get("http://127.0.0.1:5000/")

        # - Cliquer sur le bouton "Ra&D"
        generate_button = browser.find_element(By.ID, "home_submit")
        generate_button.click()

        generated_pwd = browser.find_element(By.ID, "generated_pwd").text
        
        regenerat_btn = browser.find_element(By.ID, "regenerate")
        regenerat_btn.click()

        new_pwd = browser.find_element(By.ID, "generated_pwd").text

        # https://stackoverflow.com/questions/101128/how-do-i-read-text-from-the-windows-clipboard-in-python
        copy_button = browser.find_element(By.ID, "copy_pwd")
        copy_button.click()

        copied_pwd = pyperclip.paste()

        # Close Geckodriver
        browser.quit()
        assert len(generated_pwd) == 15
        assert len(new_pwd) == 15
        assert new_pwd == copied_pwd
