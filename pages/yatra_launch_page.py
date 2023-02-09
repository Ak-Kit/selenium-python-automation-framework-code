import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flights_research_page import SearchFlightResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log= Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    DEPART_FROM_FIELD= "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD= "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD= "//label[@for='BE_flight_origin_date']"
    ALL_DATES= "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    TRAVELLER= "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']"
    PLUS= "(//span[@class='ddSpinnerPlus'])[1]"
    SEARCH_BUTTON="BE_flight_flsearch_btn"


    def getDepartFromField(self):
        return self.wait_until_elements_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def getGoingToField(self):
        return self.wait_until_elements_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResultList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getSelectDateField(self):
        return self.wait_until_elements_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDates(self):
        return self.wait_until_elements_is_clickable(By.XPATH, self.ALL_DATES)

    def getTraveller(self):
        return self.driver.find_element(By.XPATH, self.TRAVELLER)

    def add_passenger(self):
        return self.driver.find_element(By.XPATH, self.PLUS)

    def getSearchButton(self):
        return self.driver.find_element(By.ID, self.SEARCH_BUTTON)

    def enterGoingToLocation(self, goinglocation):
        self.getGoingToField().click()
        self.log.info("Clicked on Going to")
        time.sleep(2)
        self.getGoingToField().send_keys(goinglocation)
        self.log.info("Typed Text into Going to field Successfully")
        time.sleep(2)

    def enterGoingToResultList(self):
        search_results= self.getGoingToResultList()
        for results in search_results:

            if "New York (JFK)" in results.text:
                results.click()
                break


    def enterSelectDateField(self):
        self.getSelectDateField().click()

    def enterAllDates(self, departuredate):
        all_dates= self.getAllDates().find_elements(By.XPATH, self.ALL_DATES)
        # Select the departure date
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def enterTraveller(self):
        self.getTraveller().click()
        time.sleep(2)

    def enterAdd_passenger(self):
        self.add_passenger().click()
        time.sleep(2)

    def enterSearchButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    def search_flights(self, departlocation, goinglocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goinglocation)
        self.enterSelectDateField()
        self.enterAllDates(departuredate)
        self.enterTraveller()
        self.enterAdd_passenger()
        self.enterSearchButton()
        search_flights_result= SearchFlightResults(self.driver)
        return search_flights_result
