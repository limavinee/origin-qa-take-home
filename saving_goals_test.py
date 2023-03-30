import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

        displayed_value = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div/div/input')\
            .get_attribute('value')
        expected_value = '2,500.00'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"

    @pytest.mark.skip(reason="Not able to properly locate the elements for the arrow buttons")
    @pytest.mark.smoke
    @pytest.mark.saving_goals
    def test_tc_0007(self):
        left_arrow_locator = self.driver.find_element(By.CLASS_NAME, 'sc-furwcr ftJiaC')
        right_arrow_locator = self.driver.find_element(By.CLASS_NAME, 'sc-furwcr gfjHRP')

        for i in range(5):
            right_arrow_locator.click()
        for i in range(5):
            left_arrow_locator.click()

    @pytest.mark.smoke
    @pytest.mark.saving_goals
    def test_tc_0008(self):
        reach_goal_by_locator = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div/div')
        reach_goal_by_locator.click()

        for i in range(5):
            reach_goal_by_locator.send_keys(Keys.RIGHT)
        for i in range(5):
            reach_goal_by_locator.send_keys(Keys.LEFT)

    @pytest.mark.skip(reason="Cannot perform assertion due to missing html element for the left arrow button")
    @pytest.mark.smoke
    @pytest.mark.saving_goals
    def test_tc_0011(self):
        reach_goal_by_locator = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div/div')
        reach_goal_by_locator.click()

        for i in range(5):
            reach_goal_by_locator.send_keys(Keys.RIGHT)
        for i in range(10):
            reach_goal_by_locator.send_keys(Keys.LEFT)

        expected_value = 'sc-furwcr ftJiaC disabled'
        real_value = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div/div/div/svg[1]')\
            .get_attribute('class')
        assert real_value == expected_value, f"Expected {expected_value}, but got {real_value}"

    @pytest.mark.smoke
    @pytest.mark.saving_goals
    def test_tc_0013(self):
        money_input_locator = self.driver.find_element(By.XPATH, "//input['1,000']")
        money_input_locator.send_keys(250000)

        reach_goal_by_locator = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[2]/div/div')
        reach_goal_by_locator.click()

        reach_goal_by_locator.send_keys(Keys.RIGHT)
        displayed_value = self.driver.find_element \
            (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div[2]/p').text
        expected_value = '$1,250.00'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"

        reach_goal_by_locator.send_keys(Keys.RIGHT)
        displayed_value = self.driver.find_element \
            (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div[2]/p').text
        expected_value = '$833.33'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"

        reach_goal_by_locator.send_keys(Keys.RIGHT)
        displayed_value = self.driver.find_element \
            (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div[2]/p').text
        expected_value = '$625.00'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"

    @pytest.mark.smoke
    @pytest.mark.saving_goals
    def test_tc_0014(self):
        money_input_locator = self.driver.find_element(By.XPATH, "//input['1,000']")
        money_input_locator.send_keys(250075)

        reach_goal_by_locator = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/div[2]/div/div')
        reach_goal_by_locator.click()

        reach_goal_by_locator.send_keys(Keys.RIGHT)
        displayed_value = self.driver.find_element\
            (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div[2]/p').text
        expected_value = '$1,250.38'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"

        reach_goal_by_locator.send_keys(Keys.RIGHT)
        displayed_value = self.driver.find_element\
            (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div[2]/p').text
        expected_value = '$833.58'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"

        reach_goal_by_locator.send_keys(Keys.RIGHT)
        displayed_value = self.driver.find_element\
            (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[1]/div/div[2]/p').text
        expected_value = '$625.19'

        assert displayed_value == expected_value, f"Expected {expected_value}, but got {displayed_value}"
