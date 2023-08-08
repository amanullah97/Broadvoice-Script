import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


class BroadVoicePatients:
    driver = webdriver.Chrome()

    def start_request(self, url):
        self.driver.get(url)
        self.login()

    def login(self):
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("********")
        button = self.driver.find_element(By.CSS_SELECTOR, "._button-login-id")
        button.click()
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("*********")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "._button-login-password")
        login_button.click()
        self.after_login()

    def after_login(self):
        phone_numbers = self.read_phone_numbers()
        self.driver.get("https://chat.broadvoice.com/chat/conversations/d933fdf8-141f-11ee-b7c4-f596fcac1e6c/menu")
        time.sleep(10)
        message = """ Dear Patients,

        We are writing to share an important update regarding the location of AZZ Medical Associates, Oldbridge Office, at 10 Cindy St, Old Bridge, NJ 08857. Effective 06/26/2023, our office has been relocated to a new physical location at 177 Main St, Matawan, NJ 07747.
        
        Our commitment to exceptional healthcare remains unchanged.
        
        Old Address : 10 Cindy St, Old Bridge, NJ 08857
        New Address : 177 Main St, Matawan, NJ 07747
        
        For directions, visit :https://shorturl.at/dgprZ.
        
        We're here to support you during this transition.
        
        Thank you for your trust. We look forward to serving you at our new location.
        
        Warm regards,
        
        AZZ Medical Associates,
        (732) 607-2447
        (609) 890-1050
        
        """
        for phone_number in phone_numbers:
            time.sleep(15)
            query = self.driver.find_element(By.CSS_SELECTOR, "input.search")
            query.send_keys(phone_number)
            self.driver.implicitly_wait(15)
            button = self.driver.find_elements(By.CSS_SELECTOR, ".user-info div.name")
            button[0].click()
            time.sleep(10)
            send_message = self.driver.find_element(By.CSS_SELECTOR, ".ce-new-message._lr-hide")
            send_message.send_keys(message)
            send_message.send_keys(Keys.ENTER)
            time.sleep(2)

    def read_phone_numbers(self):
        data_import = pd.read_excel("Broad_Voice-Patients.xlsx", usecols="A")
        df = pd.DataFrame(data_import)
        phone_numbers = df["Patient-Phone Numbers"].values.tolist()
        return phone_numbers


x = BroadVoicePatients()
x.start_request("https://login.broadvoice.com/u/login/identifier?state="
                "hKFo2SA2ZUJ2T1pNTjhnbWlvUlVGbGdKeVY5Zmxzam"
                "ZneThHa6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIExUMGV2S2RHMkhOQ2NzUGxucEJTNHBURWFqVUJhZkgto2NpZNkgV0ZBVERUVjhhOWZtTnN5VDFwbFF5cUpUUWtBQzFabkg")











