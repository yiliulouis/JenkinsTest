

from BDDCommon.CommonFuncs import webcommon

from behave import given, when, then, step

@step("I go to the '{page}' Page")
@given('I go to the site "{page}"')
def go_to_page(context,page):
    # print ("Navigate to the site:{url}".format(url))
    # context.driver = webdriver.Chrome(executable_path="E:\Downloads\chromedriver_win32 (1)\chromedriver")

    # import pdb;pdb.set_trace()
    webcommon.go_to(context,page)

@then('the page title should be "{expected_title}"')
def verify_homepage_title(context,expected_title):
    webcommon.assert_page_title(context, expected_title)

@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context,expected_url)

@when('the page is loaded')
def page_loaded(context):
    pass