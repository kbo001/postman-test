from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.mobile_workers_page import MobileWorkerPage
from HQSmokeTests.testPages.users.group_page import GroupPage
from HQSmokeTests.testPages.users.roles_permissions_page import RolesPermissionPage
from HQSmokeTests.testPages.users.org_structure_page import OrganisationStructurePage
from HQSmokeTests.testPages.users.webapps_permission_page import WebAppPermissionPage
from HQSmokeTests.testPages.users.web_user_page import WebUsersPage

""""Contains test cases related to the User's Mobile Worker and Roles and Permissions module"""


def test_case_02_create_mobile_worker(driver):

    worker = MobileWorkerPage(driver)
    worker.mobile_worker_menu()
    worker.create_mobile_worker()
    worker.mobile_worker_enter_username("username_" + str(fetch_random_string()))
    worker.mobile_worker_enter_password(fetch_random_string())
    worker.click_create()


def test_case_03_create_and_assign_user_field(driver):

    create = MobileWorkerPage(driver)
    create.mobile_worker_menu()
    create.edit_user_field()
    create.add_field()
    create.add_user_property("user_field_" + fetch_random_string())
    create.add_label("user_field_" + fetch_random_string())
    create.add_choice("user_field_" + fetch_random_string())
    create.save_field()
    create.select_mobile_worker_created()
    create.enter_value_for_created_user_field()
    create.update_information()


def test_case_05_create_group_and_assign_user(driver):

    menu = HomePage(driver)
    menu.users_menu()
    visible = GroupPage(driver)
    visible.add_group()
    visible.add_user_to_group()


def test_case_05_edit_user_groups(driver):
    menu = HomePage(driver)
    menu.users_menu()
    edit = GroupPage(driver)
    edit.click_group_menu()
    edit.edit_existing_group()
    edit.remove_user_from_group()


def test_case_10_download_and_upload_users(driver):

    user = MobileWorkerPage(driver)
    user.download_mobile_worker()
    user.upload_mobile_worker()


def test_case_04_deactivate_user(driver):

    user = MobileWorkerPage(driver)
    user.mobile_worker_menu()
    user.deactivate_user()
    user.verify_deactivation_via_login()


def test_case_04_reactivate_user(driver):

    user = MobileWorkerPage(driver)
    user.mobile_worker_menu()
    user.reactivate_user()
    user.verify_reactivation_via_login()


def test_cleanup_items_in_users_menu(driver):
    clean = MobileWorkerPage(driver)
    clean2 = GroupPage(driver)

    clean.mobile_worker_menu()
    clean.select_mobile_worker_created()
    clean.cleanup_mobile_worker()
    print("Deleted the mobile worker")

    clean.mobile_worker_menu()
    clean.edit_user_field()
    clean.cleanup_user_field()
    clean.save_field()
    print("Deleted the user field")

    clean.mobile_worker_menu()
    clean2.click_group_menu()
    clean2.cleanup_group()
    print("Deleted the group")


def test_case_13_new_webuser_invitation(driver):

    webuser = WebUsersPage(driver)
    webuser.invite_new_web_user('admin')
    webuser.assert_invite()
    webuser.delete_invite()


def test_case_54_add_custom_user_data_profile_to_mobile_worker(driver):

    create = MobileWorkerPage(driver)
    create.mobile_worker_menu()
    create.create_new_mobile_worker()
    create.create_new_user_fields("field_" + fetch_random_string())
    create.click_profile()
    create.add_profile("field_" + fetch_random_string())
    create.save_field()
    create.select_user_and_update_fields("user_" + str(fetch_random_string()))
    create.add_phone_number()
    create.select_profile()
    create.update_information()
    create.select_location()
    create.mobile_worker_menu()
    create.select_and_delete_mobile_worker("user_" + str(fetch_random_string()))
    create.mobile_worker_menu()
    create.edit_user_field()
    create.click_profile()
    create.remove_profile()
    create.save_field()
    create.click_fields()
    create.remove_user_field()
    create.save_field()
