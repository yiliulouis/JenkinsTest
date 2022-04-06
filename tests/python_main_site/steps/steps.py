
from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import locatorsconfig



@then('the "{nav_bar}" bar should be visible')
def verify_nav_bar_visible(context,nav_bar):
    # import pdb; pdb.set_trace()
    expected_bars = ['main navigation','top navigation','options']
    if nav_bar not in expected_bars:
        raise Exception(f"The passed nav bar is not one of the expected.\
            Actual is {nav_bar}, Expected is {expected_bars}")

    # if nav_bar == 'main navigation':
    #     locator="/html/body/div/header/div/nav/ul"
    #     bar = context.driver.find_element_by_xpath(locator)
    #     if not bar.is_visible():
    #         raise Exception

    locator_info = locatorsconfig.LOCATORS.get(nav_bar)
    locator_type = locator_info['type']
    locator_text = locator_info['locator']
    
    nav_element = webcommon.find_element(context, locator_type, locator_text)

    webcommon.assert_element_visible(nav_element)

