import xlrd
import os
import time
import win32com.client
from tkinter import Tk
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import inputs

class Export_Data:

    def __init__(self, driver):  # initialize each WebElement here
        self.driver = driver

        wait = WebDriverWait(self.driver.instance, 10)

        self.data_dropdown = None  # Data dropdown
        self.view_all_link = None  # View All link

        #Delete Export
        self.no_exports_to_display = None
        self.existing_form_export_name = None
        self.existing_case_export_name = None
        self.delete_form_export_button = None
        self.delete_case_export_button = None
        self.delete_confirmation_button = None


        #Add Export
        self.add_export_button = None  # Add Export button
        self.app_dropdown = None #Application dropdown in the modal
        self.select_app = None #Selecting first app
        self.menu_dropdown = None #Menu dropdown in the modal
        self.select_menu = None #Selecting first menu item
        self.form_dropdown = None  # Form dropdown in the modal
        self.select_form = None  # Selecting first form item
        self.add_export_conf = None #Confirm and add export
        self.export_name = None #Custom name for the export
        self.export_settings_create = None #Creating export with the default settings

        # Export Form data variables
        self.export_form_data_link = None  # Export Form Data link on the left panel
        self.export_form_data_button = None  # click form exports
        self.prepare_export_button = None  # click prepare exports
        self.download_button = None  # click download
        self.find_data_by_ID_link = None  # Click findDataByID link
        self.find_data_by_ID_textbox = None  # Find data by ID textbox
        self.find_data_by_ID_button = None
        self.view_FormID = None
        self.womanName_HQ = None  # Property 'Woman's name' value on HQ
        oldest = None
        newest = None

        # Export Case data variables
        self.export_case_data_link = None  # Export Case Data link on the left panel
        self.export_case_data_button = None
        self.prepare_case_export_button = None
        self.case_download_button = None

        # Export SMS variables
        self.export_sms_link = None  # Export Case Data on the left panel
        self.prepare_sms_export_button = None
        self.sms_download_button = None

        # Daily Saved Export variables
        self.edit_form_export = None  # Edit an existing form export
        self.create_DSE_checkbox = None # Create a Daily Saved Export checkbox
        self.save_DSE_button = None # Create a Daily Saved Export confirmation button
        self.DSE_Name = None # DSE's name

        # Excel Dashboard Integrations, form
        self.export_excel_dash_int_link = None # Excel Dashboard Integrations link on the left panel
        self.add_dashboard_feed_button1 = None
        self.model_dropdown = None
        self.select_form_model = None
        self.add_dashboard_feed_button2 = None
        self.update_data = None
        self.update_data_conf = None
        self.copy_dashfeed_link = None

        # Excel Dashboard Integrations, case
        self.select_case_model = None
        self.case_type_dropdown = None

        # Power BI / Tableau Integration, Form
        self.powerBI_tab_int_link = None
        self.add_Odata_feed_button1 = None
        self.feed_type_dropdown = None
        self.select_form_feed_type = None
        self.add_Odata_feed_button2 = None
        self.copy_odatafeed_link = None
        self.odata_username = None
        self.odata_password = None

        #Manage Forms
        self.manage_forms_link = None
        self.apply_button = None
        self.checkbox1 = None
        self.checkbox2 = None
        self.archive_button = None
        self.view_normal_form_link = None
        self.archived_restored_dropdown = None
        self.archived_forms_option = None
        self.view_archived_form_link = None


    def data_tab(self):
        #print(type(self.driver))
        self.data_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="ProjectDataTab"]/a')))
        self.data_dropdown.click()
        print("Data drop down clicked")
        time.sleep(2)

        self.view_all_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="ProjectDataTab"]/ul/li[6]/a')))
        self.view_all_link.click()
        print("View All link clicked")
        # time.sleep(2)

# Test Case 20_a - Verify Export functionality for Forms

    def del_form_exports(self):
    
        print("Printing page source...")
        print(self.driver.instance.page_source)
        if inputs.text_no_exports_to_display in self.driver.instance.page_source:
            print("No export present")
            time.sleep(2)
        else:
            print("Export doc present")
            self.delete_form_export_button = WebDriverWait(self.driver.instance, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/a')))
            self.delete_form_export_button.click()
            print("Delete Button clicked")
            time.sleep(2)

            self.delete_confirmation_button = WebDriverWait(self.driver.instance, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div/div/div/div/form/div[2]/button')))
            self.delete_confirmation_button.click()
            print("Delete Confirmation Button clicked")
            time.sleep(2)


    def add_form_exports(self):
        self.add_export_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="create-export"]/p/a')))
        self.add_export_button.click()
        print("add_export_button clicked")
        time.sleep(2)

        self.app_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_application"]/div/span/span[1]/span')))
        self.app_dropdown.click()
        print("app_dropdown clicked")
        #time.sleep(2)
        self.select_app = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_application-results"]/li')))
        self.select_app.click()
        print("First app selected")
        #time.sleep(2)

        self.menu_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_module"]/div/span/span[1]/span')))
        self.menu_dropdown.click()
        print("menu_dropdown clicked")
        #time.sleep(2)
        self.select_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_module-results"]/li[1]')))
        self.select_menu.click()
        print("First menu item selected")
        #time.sleep(2)

        self.form_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_form"]/div/span/span[1]/span')))
        self.form_dropdown.click()
        print("form_dropdown clicked")
        #time.sleep(2)
        self.select_form = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_form-results"]/li[1]')))
        self.select_form.click()
        print("First form item selected")
        #time.sleep(2)

        self.add_export_conf = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]')))
        self.add_export_conf.click()
        print("Export added!!")
        time.sleep(2)

        self.export_name = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-name"]')))
        self.export_name.clear()
        self.export_name.send_keys(inputs.form_export_name)

        self.export_settings_create  = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.export_settings_create .click()
        print("Export created!!")
        time.sleep(2)

    def form_exports(self):
        self.export_form_data_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr/td[2]/a[1]')))
        self.export_form_data_button.click()
        print("Export form button clicked")
        # time.sleep(2)

        self.prepare_export_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="download-export-form"]/form/div[2]/div/div[2]/div[1]/button')))
        self.prepare_export_button.click()
        print("Prepare Form Export button clicked")
        # time.sleep(2)

        try:
            self.download_button = WebDriverWait(self.driver.instance, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="download-progress"]/div/div/div[2]/div[1]/form/a')))
            self.download_button.click()
            print("Download form button clicked")
            path = inputs.download_path
            os.chdir(path)
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
            oldest = files[0]
            newest = files[-1]
            print("Oldest:", oldest)
            print("Newest:", newest)
            # print ("All by modified oldest to newest:","\n".join(files))
            # check if size of file is 0
            if os.stat(newest).st_size == 0:
                print('Form Exports file is empty')
            else:
                print('Form Exports file is not empty')
        except Exception as e:
            print(e)
            print("Download task failed to start")
        finally:
            time.sleep(2)

#Test Case 22_a -  Find Data By ID, forms
    def validate_downloaded_form_exports(self):
        path = inputs.download_path
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        #oldest = files[0]
        newest = files[-1]
        #print("Oldest:", oldest)
        #print("Newest:", newest)
        # print ("All by modified oldest to newest:","\n".join(files))
        # check if size of file is 0
        #if os.stat(newest).st_size == 0:
        #    print('File is empty')
        #else:
        #    print('File is not empty')

        # Reading an excel file using Python
        # To open Workbook
        wb = xlrd.open_workbook(newest)
        sheet = wb.sheet_by_index(0)
        # Extract a particular row value
        # print(sheet.row_values(1))
        # For row 0 and column 1, extracting first formID
        formID_colName = sheet.cell_value(0, 1)
        formID = sheet.cell_value(1, 1)
        print(formID_colName, ": ", formID)
        womanName_colName = sheet.cell_value(0, 2)
        womanName_excel = sheet.cell_value(1, 2)
        print("Woman's name in Excel- ", womanName_colName, ": ", womanName_excel)
        # return formID
        # def find_data_by_ID(self,validate_downloaded_form_exports):
        self.find_data_by_ID_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[4]/a')))
        self.find_data_by_ID_link.click()
        print("Find data by ID link clicked")
        self.find_data_by_ID_textbox = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="find-form"]/div[2]/div[1]/input')))
        self.find_data_by_ID_textbox.clear()
        self.find_data_by_ID_textbox.send_keys(formID)
        print("Form ID fed in the textbox")
        self.find_data_by_ID_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="find-form"]/div[2]/div[2]/button')))
        self.find_data_by_ID_button.click()
        print("find_data_by_ID_button clicked")
        self.view_FormID = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="find-form"]/div[2]/div[1]/div[2]/a')))
        self.view_FormID.click()
        print("view_FormID link clicked")
        time.sleep(5)
        # self.driver.instance.get("https://www.commcarehq.org/accounts/login/")

        # Switch tab logic is required here
        winHandles = self.driver.instance.window_handles
        window_before = winHandles[0]
        print(window_before)
        window_after = winHandles[1]
        print(window_after)
        self.driver.instance.switch_to.window(window_after)

        self.womanName_HQ = self.driver.instance.find_element_by_xpath(
            '//*[@id="form-data"]/div[3]/div/div/table/tbody/tr[2]/td[2]/div').text
        print("Woman's name on HQ")
        print(self.womanName_HQ)

        if womanName_excel == self.womanName_HQ:
            print("Values match!")
        else:
            print("Values don't match")
        self.driver.instance.close()  # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0])  # Switch back to the

# Test Case 20_b - Verify Export functionality for Cases
    def add_case_exports(self):
        self.export_case_data_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[2]/a')))
        self.export_case_data_link.click()
        print("export_case_data_link clicked")
        time.sleep(2)

        self.add_export_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="create-export"]/p/a')))
        self.add_export_button.click()
        print("add_export_button clicked")
        time.sleep(2)

        self.app_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_application"]/div/span/span[1]/span')))
        self.app_dropdown.click()
        print("app_dropdown clicked")
        # time.sleep(2)
        self.select_app = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_application-results"]/li')))
        self.select_app.click()
        print("First app selected")
        # time.sleep(2)

        self.case_type_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_case_type"]/div/span/span[1]/span')))
        self.case_type_dropdown.click()
        print("case_type_dropdown clicked")
        # time.sleep(2)
        self.select_case_type = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_case_type-results"]/li')))
        self.select_case_type.click()
        print("First Case Type selected")
        # time.sleep(2)

        self.add_export_conf = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]')))
        self.add_export_conf.click()
        print("Export added!!")
        time.sleep(2)

        self.export_name = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-name"]')))
        self.export_name.clear()
        self.export_name.send_keys(inputs.case_export_name)

        self.export_settings_create = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.export_settings_create.click()
        print("Export created!!")
        time.sleep(2)

    def case_exports(self):
        self.export_case_data_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[2]/a')))
        self.export_case_data_link.click()
        print("export_case_data_link clicked")
        time.sleep(2)

        self.export_case_data_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr/td[3]/a[1]')))
        self.export_case_data_button.click()
        print("Export Case button clicked")
        # time.sleep(2)

        self.prepare_case_export_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="download-export-form"]/form/div[2]/div/div[2]/div[1]/button')))
        self.prepare_case_export_button.click()
        print("Prepare Case Export button clicked")
        time.sleep(2)

        try:
            self.case_download_button = WebDriverWait(self.driver.instance, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="download-progress"]/div/div/div[2]/div[1]/form/a')))
            self.case_download_button.click()
            print("Download Case button clicked")
        except Exception as e:
            print(e)
            print("Download task failed to start")
        finally:
            time.sleep(2)

# Test Case 22_b - Find Data by ID for Case Exports
    def validate_downloaded_case_exports(self):
        path = inputs.download_path
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        # oldest = files[0]
        newest = files[-1]
        # print("Oldest:", oldest)
        # print("Newest:", newest)
        # print ("All by modified oldest to newest:","\n".join(files))
        # check if size of file is 0
        # if os.stat(newest).st_size == 0:
        #    print('File is empty')
        # else:
        #    print('File is not empty')

        # Reading an excel file using Python
        # To open Workbook
        wb = xlrd.open_workbook(newest)
        sheet = wb.sheet_by_index(0)
        # Extract a particular row value
        # print(sheet.row_values(1))
        # For row 0 and column 1, extracting first formID
        caseID_colName = sheet.cell_value(0, 1)
        caseID = sheet.cell_value(1, 1)
        print(caseID_colName, ": ", caseID)
        womanName_colName = sheet.cell_value(0, 2)
        womanName_excel = sheet.cell_value(1, 2)
        print("Woman's name in Excel- ", womanName_colName, ": ", womanName_excel)
        # return formID
        # def find_data_by_ID(self,validate_downloaded_form_exports):
        self.find_data_by_ID_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[4]/a')))
        self.find_data_by_ID_link.click()
        print("Find data by ID link clicked")
        self.find_data_by_ID_textbox = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="find-form"]/div[2]/div[1]/input')))
        self.find_data_by_ID_textbox.clear()
        self.find_data_by_ID_textbox.send_keys(caseID)
        print("Form ID fed in the textbox")
        self.find_data_by_ID_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="find-form"]/div[2]/div[2]/button')))
        self.find_data_by_ID_button.click()
        print("find_data_by_ID_button clicked")
        self.view_caseID = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="find-form"]/div[2]/div[1]/div[2]/a')))
        self.view_caseID.click()
        print("view_FormID link clicked")
        time.sleep(5)
        # self.driver.instance.get("https://www.commcarehq.org/accounts/login/")

        # Switch tab logic is required here
        winHandles = self.driver.instance.window_handles
        window_before = winHandles[0]
        print(window_before)
        window_after = winHandles[1]
        print(window_after)
        self.driver.instance.switch_to.window(window_after)

        self.womanName_HQ = self.driver.instance.find_element_by_xpath(
            '//*[@id="form-data"]/div[3]/div/div/table/tbody/tr[2]/td[2]/div').text
        print("Woman's name on HQ")
        print(self.womanName_HQ)

        if womanName_excel == self.womanName_HQ:
            print("Values match!")
        else:
            print("Values don't match")
        self.driver.instance.close()  # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0])  # Switch back to the

    # Test Case 21 - Export SMS Messages
    def sms_exports(self):
        self.export_sms_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[3]/a')))
        self.export_sms_link.click()
        print("export_sms_link clicked")
        time.sleep(2)

        self.prepare_sms_export_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//*[@id="download-export-form"]/form/div[2]/div/div[2]/div[1]/button')))
        self.prepare_sms_export_button.click()
        print("Prepare SMS Export button clicked")
        time.sleep(2)

        try:
            self.sms_download_button = WebDriverWait(self.driver.instance, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="download-progress"]/div/div/div[2]/div[1]/form/a')))
            self.sms_download_button.click()
            print("Download SMS button clicked")
            time.sleep(2)
            path = inputs.download_path
            os.chdir(path)
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
            oldest = files[0]
            newest = files[-1]
            print("Oldest:", oldest)
            print("Newest:", newest)
            # print ("All by modified oldest to newest:","\n".join(files))
            # check if size of file is 0
            if os.stat(newest).st_size == 0:
                print('File is empty')
            else:
                print('File is not empty')
        except Exception as e:
            print(e)
            print("Download task failed to start")
        finally:
            time.sleep(2)

# Test Case 23_a - Daily saved export, form
    def daily_saved_exports(self):
        self.export_form_data_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[1]/a')))
        self.export_form_data_link.click()
        print("export_form_data_link clicked")
        time.sleep(2)

        self.edit_form_export = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/div[2]/div/a')))
        self.edit_form_export.click()
        print("edit_form_export clicked")
        time.sleep(2)

        self.create_DSE_checkbox = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="daily-saved-export-checkbox"]')))
        self.create_DSE_checkbox.click()
        print("create_DSE_checkbox selected")
        time.sleep(2)

        self.save_DSE_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.save_DSE_button.click()
        print("save_DSE_button clicked")
        time.sleep(2)

        if inputs.form_export_name in self.driver.instance.page_source:
            print(inputs.form_export_name," - Export is present")
        else:
            print("Export creation failed")

# Test Case 23_b - Daily saved export, case
#Pending

#Test Case - 24 - Excel Dashboard Integration, form
    def excel_dashboard_integration_form(self):
        self.export_excel_dash_int_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[6]/a')))
        self.export_excel_dash_int_link.click()
        print("export_excel_dash_int_link clicked")
        time.sleep(2)

        self.add_dashboard_feed_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="create-export"]/p/a')))
        self.add_dashboard_feed_link.click()
        print("add_dashboard_feed clicked")
        time.sleep(2)

        self.model_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]')))
        self.model_dropdown.click()
        print("model_dropdown clicked")
        # time.sleep(2)
        self.select_form_model = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]/option[3]')))
        self.select_form_model.click()
        print("select_form_model selected")
        # time.sleep(2)
        self.app_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_application"]/div/span/span[1]/span')))
        self.app_dropdown.click()
        print("app_dropdown clicked")
        # time.sleep(2)
        self.select_app = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_application-results"]/li')))
        self.select_app.click()
        print("First app selected")
        # time.sleep(2)

        self.menu_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_module"]/div/span/span[1]/span')))
        self.menu_dropdown.click()
        print("menu_dropdown clicked")
        # time.sleep(2)
        self.select_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_module-results"]/li[1]')))
        self.select_menu.click()
        print("First menu item selected")
        # time.sleep(2)

        self.form_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_form"]/div/span/span[1]/span')))
        self.form_dropdown.click()
        print("form_dropdown clicked")
        # time.sleep(2)
        self.select_form = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_form-results"]/li[1]')))
        self.select_form.click()
        print("First form item selected")
        # time.sleep(2)
        self.add_dashboard_feed_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]')))
        self.add_dashboard_feed_button.click()
        print("Dashboard Feed added!!")
        time.sleep(2)
        self.export_name = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-name"]')))
        self.export_name.clear()
        self.export_name.send_keys(inputs.dashboard_feed_form)
        # time.sleep(2)

        self.export_settings_create = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.export_settings_create.click()
        print("Dashboard Form Feed created!!")

        self.update_data = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div/button[1]')))
        self.update_data.click()
        print("update_data link clicked!!")

        self.update_data_conf = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/div[4]/div[2]/div/div/div[4]/button')))
        self.update_data_conf.click()
        print("update_data confirmed!!")

        self.driver.instance.refresh()

        self.copy_dashfeed_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/span/a')))
        self.copy_dashfeed_link.click()
        print("Dashboard link copied on the clipboard!!")
        dashboard_feed_link = Tk().clipboard_get()
        print(dashboard_feed_link)
        self.driver.instance.execute_script("window.open('');") # Open a new tab
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[1]) # Switch to the new tab and open feed URL
        self.driver.instance.get(dashboard_feed_link)
        dashboard_feed_data = self.driver.instance.page_source
        #print(dashboard_feed_data)
        if dashboard_feed_data != "":
            print("Excel Dashboard (form) has data")
        else:
            print("Excel Dashboard (form) is empty")
        self.driver.instance.close() # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0]) # Switch back to the first tab with URL A

#Test Case - 25 - Excel Dashboard Integration, case
    def excel_dashboard_integration_case(self):
        self.export_excel_dash_int_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[6]/a')))
        self.export_excel_dash_int_link.click()
        print("export_excel_dash_int_link clicked")
        time.sleep(2)

        self.add_dashboard_feed_button1 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="create-export"]/p/a')))
        self.add_dashboard_feed_button1.click()
        print("add_dashboard_feed clicked")
        time.sleep(2)

        self.model_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]')))
        self.model_dropdown.click()
        print("model_dropdown clicked")
        # time.sleep(2)
        self.select_case_model = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]/option[2]')))
        self.select_case_model.click()
        print("select_case_model selected")
        # time.sleep(2)
        self.app_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_application"]/div/span/span[1]/span')))
        self.app_dropdown.click()
        print("app_dropdown clicked")
        # time.sleep(2)
        self.select_app = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_application-results"]/li')))
        self.select_app.click()
        print("First app selected")
        # time.sleep(2)

        self.case_type_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_case_type"]/div/span/span[1]/span')))
        self.case_type_dropdown.click()
        print("case_type_dropdown clicked")
        # time.sleep(2)
        self.select_case_type = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_case_type-results"]/li')))
        self.select_case_type.click()
        print("First Case Type selected")
        # time.sleep(2)


        # time.sleep(2)
        self.add_dashboard_feed_button2 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]')))
        self.add_dashboard_feed_button2.click()
        print("Dashboard Feed added!!")
        time.sleep(2)
        self.export_name = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-name"]')))
        self.export_name.clear()
        self.export_name.send_keys(inputs.dashboard_feed_case)
        # time.sleep(2)

        self.export_settings_create = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.export_settings_create.click()
        print("Dashboard Form Feed created!!")

        self.update_data = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div/button[1]')))
        self.update_data.click()
        print("update_data link clicked!!")

        self.update_data_conf = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/div[4]/div[2]/div/div/div[4]/button')))
        self.update_data_conf.click()
        print("update_data confirmed!!")

        self.driver.instance.refresh()

        self.copy_dashfeed_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/span/a')))
        self.copy_dashfeed_link.click()
        print("Dashboard link copied on the clipboard!!")
        dashboard_feed_link = Tk().clipboard_get()
        print(dashboard_feed_link)
        self.driver.instance.execute_script("window.open('');") # Open a new tab
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[1]) # Switch to the new tab and open feed URL
        self.driver.instance.get(dashboard_feed_link)
        dashboard_feed_data = self.driver.instance.page_source
        #print(dashboard_feed_data)
        if dashboard_feed_data != "":
            print("Excel Dashboard (case) has data")
        else:
            print("Excel Dashboard (case) is empty")
        self.driver.instance.close() # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0]) # Switch back to the first tab with URL A

#Test Case - 28 - Power BI / Tableau Integration, Form
    def powerBI_tableau_integration_form(self):
        self.powerBI_tab_int_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[7]/a')))
        self.powerBI_tab_int_link.click()
        print("powerBI_tab_int_link clicked")
        time.sleep(2)

        self.add_Odata_feed_button1 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="create-export"]/p/a')))
        self.add_Odata_feed_button1.click()
        print("OData_feed_button clicked")
        time.sleep(2)

        self.feed_type_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]')))
        self.feed_type_dropdown.click()
        print("feed_type_dropdown clicked")
        # time.sleep(2)
        self.select_form_feed_type = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]/option[3]')))
        self.select_form_feed_type.click()
        print("select_form_feed_type selected")
        # time.sleep(2)
        self.app_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_application"]/div/span/span[1]/span')))
        self.app_dropdown.click()
        print("app_dropdown clicked")
        # time.sleep(2)
        self.select_app = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_application-results"]/li')))
        self.select_app.click()
        print("First app selected")
        # time.sleep(2)

        self.menu_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_module"]/div/span/span[1]/span')))
        self.menu_dropdown.click()
        print("menu_dropdown clicked")
        # time.sleep(2)
        self.select_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_module-results"]/li[1]')))
        self.select_menu.click()
        print("First menu item selected")
        # time.sleep(2)

        self.form_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_form"]/div/span/span[1]/span')))
        self.form_dropdown.click()
        print("form_dropdown clicked")
        # time.sleep(2)
        self.select_form = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_form-results"]/li[1]')))
        self.select_form.click()
        print("First form item selected")
        # time.sleep(2)
        self.add_Odata_feed_button2 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]')))
        self.add_Odata_feed_button2.click()
        print("Odata form Feed added!!")
        time.sleep(2)
        self.export_name = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-name"]')))
        self.export_name.clear()
        self.export_name.send_keys(inputs.odata_feed_form)
        # time.sleep(2)

        self.export_settings_create = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.export_settings_create.click()
        print("Odata Form Feed created!!")

        self.driver.instance.refresh()

        self.copy_odatafeed_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/span/a')))
        self.copy_odatafeed_link.click()
        print("Odata feed link copied on the clipboard!!")
        odata_feed_link = Tk().clipboard_get()
        print(odata_feed_link)
        self.driver.instance.execute_script("window.open('');") # Open a new tab
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[1]) # Switch to the new tab and open feed URL
        #string manipulation for bypassing the authentication
        final_URL=f"https://{inputs.login_username}:{inputs.login_password}@{odata_feed_link[8:]}"
        self.driver.instance.get(final_URL)
        odata_feed_data = self.driver.instance.page_source
        print(odata_feed_data)
        if odata_feed_data != "":
            print("Odata form feed has data")
        else:
            print("Odata form feed is empty")
        self.driver.instance.close() # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0]) # Switch back to the first tab with URL A

#Test Case - 27 - Power BI / Tableau Integration, Case
    def powerBI_tableau_integration_case(self):
        self.powerBI_tab_int_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[1]/li[7]/a')))
        self.powerBI_tab_int_link.click()
        print("powerBI_tab_int_link clicked")
        time.sleep(2)

        self.add_Odata_feed_button1 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="create-export"]/p/a')))
        self.add_Odata_feed_button1.click()
        print("Add OData_feed_button clicked")
        time.sleep(2)

        self.feed_type_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]')))
        self.feed_type_dropdown.click()
        print("feed_type_dropdown clicked")
        # time.sleep(2)
        self.select_case_feed_type = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="id_model_type"]/option[2]')))
        self.select_case_feed_type.click()
        print("select_case_feed_type selected")
        # time.sleep(2)
        self.app_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_application"]/div/span/span[1]/span')))
        self.app_dropdown.click()
        print("app_dropdown clicked")
        # time.sleep(2)
        self.select_app = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_application-results"]/li')))
        self.select_app.click()
        print("First app selected")
        # time.sleep(2)

        self.case_type_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="div_id_case_type"]/div/span/span[1]/span')))
        self.case_type_dropdown.click()
        print("case_type_dropdown clicked")
        # time.sleep(2)
        self.select_case_type = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-id_case_type-results"]/li')))
        self.select_case_type.click()
        print("First Case Type selected")
        # time.sleep(2)

        # time.sleep(2)
        self.add_Odata_feed_button2 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]')))
        self.add_Odata_feed_button2.click()
        print("Odata Case Feed added!!")
        time.sleep(2)
        self.export_name = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-name"]')))
        self.export_name.clear()
        self.export_name.send_keys(inputs.odata_feed_case)
        # time.sleep(2)

        self.export_settings_create = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="customize-export"]/form/div/div[1]/button')))
        self.export_settings_create.click()
        print("Odata Case Feed created!!")

        self.driver.instance.refresh()

        self.copy_odatafeed_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/span/a')))
        self.copy_odatafeed_link.click()
        print("Odata feed link copied on the clipboard!!")
        odata_feed_link = Tk().clipboard_get()
        print(odata_feed_link)
        self.driver.instance.execute_script("window.open('');") # Open a new tab
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[1]) # Switch to the new tab and open feed URL
        #string manipulation for bypassing the authentication
        final_URL=f"https://{inputs.login_username}:{inputs.login_password}@{odata_feed_link[8:]}"
        self.driver.instance.get(final_URL)
        odata_feed_data = self.driver.instance.page_source
        print(odata_feed_data)
        if odata_feed_data != "": #This condition can be improvised
            print("Odata case feed has data")
        else:
            print("Odata case feed is empty")
        self.driver.instance.close()  # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0])  # Switch back to the first tab with URL A

#Test Case - 30 - Verify user is able to manage forms and archive a form
    def manage_forms(self):
        #Forms archival
        self.manage_forms_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[2]/li[3]/a')))
        self.manage_forms_link.click()
        print("manage_forms_link clicked")
        time.sleep(5)

        self.apply_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="apply-btn"]')))
        self.apply_button.click()
        print("apply_button clicked")
        time.sleep(5)

        self.checkbox1 = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="report_table_bulk_archive_forms"]/tbody/tr[1]/td[1]/input')))
        self.checkbox1.click()
        print("checkbox1 selected")
        time.sleep(1)

        self.archive_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="submitForms"]')))
        self.archive_button.click()
        print("archive_button clicked")
        time.sleep(5)
        print("Forms archival successful!!")

        #View Normal Forms

        self.driver.instance.refresh()

        self.manage_forms_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[2]/li[3]/a')))
        self.manage_forms_link.click()
        print("manage_forms_link clicked")

        self.driver.instance.refresh()

        time.sleep(2)
        self.apply_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="apply-btn"]')))
        self.apply_button.click()
        print("apply_button clicked")
        #Good to add a check to verify that there are required forms available; or get the count of forms available
        #Abort if zero
        time.sleep(5)
        self.view_normal_form_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="report_table_bulk_archive_forms"]/tbody/tr[2]/td[2]/a')))
        self.view_normal_form_link.click()
        print("view_normal_form link clicked")
        time.sleep(2)
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[1])  # Switch to the new
        normal_form_data = self.driver.instance.page_source
        print(normal_form_data)
        if normal_form_data != "": #This condition can be improvised
            print("normal_form_data has data")
        else:
            print("normal_form_data is empty")
        self.driver.instance.close()  # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0])  # Switch back to the

        #View Archived Forms
        self.archived_restored_dropdown = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="select2-report_filter_archive_or_restore-container"]')))
        self.archived_restored_dropdown.click()
        print("archived_restored_dropdown clicked")
        # time.sleep(2)
        self.archived_forms_option = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')))
        self.archived_forms_option.click()
        print("Archived type selected")
        # time.sleep(2)
        self.apply_button = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="apply-btn"]')))
        self.apply_button.click()
        print("apply_button clicked")
        time.sleep(5)
        self.view_archived_form_link = WebDriverWait(self.driver.instance, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="report_table_bulk_archive_forms"]/tbody/tr[2]/td[2]/a')))
        self.view_archived_form_link.click()
        print("view_archived_form link clicked")
        time.sleep(2)
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[1])  # Switch to the new
        normal_form_data = self.driver.instance.page_source
        print(normal_form_data)
        if normal_form_data != "": #This condition can be improvised
            print("archived_form_data has data")
        else:
            print("archived_form_data is empty")
        self.driver.instance.close()  # Close the feed URL
        self.driver.instance.switch_to.window(self.driver.instance.window_handles[0])  # Switch back to the


