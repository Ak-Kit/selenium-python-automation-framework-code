import logging

import pytest
import softest
from utilities.utils import Utils
from pages.yatra_launch_page import LaunchPage
from ddt import ddt, data,file_data, unpack
from openpyxl import Workbook, load_workbook

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.uti = Utils()
    # @data(("New Delhi", "New York", "27/02/2023", "1 Stop"), ("BOM", "JFK", "17/03/2023", "1 Stop"))
    # @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyaml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\Python-selenium\\TestFrameworkDemo\\testdata\\tdataexcel.xlsx", "tdataexcel"))
    @data(*Utils.read_data_from_csv("C:\\Python-selenium\\TestFrameworkDemo\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        search_flight_result= self.lp.search_flights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stops)
        allstops1= search_flight_result.get_search_flights_results()
        self.log.info(len(allstops1))
        self.uti.assetListItemText(allstops1, stops)

    # def test_search_flights_2_stop(self):
    #     search_flight_result= self.lp.search_flights("New Delhi", "New York", "31/01/2023")
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stop("2 Stop")
    #     allstops1= search_flight_result.get_search_flights_results()
    #     self.log.info(len(allstops1))
    #     self.uti.assetListItemText(allstops1, "2 Stops ")