import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSavingGoals:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://qa-assignment.useorigin.com.s3-website-us-east-1.amazonaws.com/")

        yield

        self.driver.quit()

    @pytest.mark.smoke
    @pytest.mark.saving_goals
    def test_tc_0001(self):
        money_input_locator = self.driver.find_element(By.XPATH, "//input['1,000']")
        money_input_locator.send_keys(250000)

        time.sleep(5)