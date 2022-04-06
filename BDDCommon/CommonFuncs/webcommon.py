from multiprocessing import context
from selenium import webdriver
from BDDCommon.CommonConfigs import urlconfig

def go_to(context,location):

    if not location.startswith('http'):
        _url = urlconfig.URLCONFIG.get(location)
        base_url = urlconfig.URLCONFIG.get('base_url')
        url = base_url + _url


    browser = context.config.userdata.get('browser')
    if not browser:
        browser = 'chrome'

    if browser.lower() == 'chrome':
        context.driver = webdriver.Chrome(executable_path="E:\Downloads\chromedriver_win32 (1)\chromedriver")
    elif browser.lower() in ('firefox','ff'):
        context.driver = webdriver.Firefox()
    else:
        raise Exception("The browser type '{}' is not supported. ".format(browser))

    url = url.strip()
    # import time; time.sleep(2)
    context.driver.get(url)

    return context.driver

def assert_page_title(context,expected_title):
    actual_title = context.driver.title

    print(f"The actual title is {actual_title}")
    print(f"The Expectd title is {expected_title}")

    assert actual_title == expected_title, f"Title is not expected, expected is {expected_title}, but actual"\
    f"is {actual_title}"

    print("the title is as expected")

def assert_current_url(context, expected_url):
    actual_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert actual_url == expected_url, f"Url is not expected, expected is {expected_url}, actual is {actual_url}"
    print("the url is as expected")



def find_element(context, locator_attribute, locator_text):
    possible_locators = ["id","xpath","link text","partial link text","name","tag name","class name", "css selector"]
    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling or format is not \
            supported. The approved attributes are : %s ' %possible_locators)
        
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


def is_element_visible(element):

    if element.is_displayed():
        return True
    else:
        return False


def assert_element_visible(context_or_element,locator_att, locator_text):

    if isinstance(context_or_element,webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att,locator_text)
    
    if not element.is_displayed():
        raise AssertionError('The element is not displayed')


def type_into_element(context_or_element, input_value, locator_att, locator_text):
    
    if isinstance(context_or_element,webdriver.remote.webelement.WebElement):
        input_field = context_or_element
    else:
        input_field = context_or_element.driver.find_element(locator_att,locator_text)
    input_field.send_keys(input_value)


def click(context_or_element,locator_att, locator_text):
    
    if isinstance(context_or_element,webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att,locator_text)
    element.click()


def element_contains_text(context_or_element,expected_text, locator_att, locator_text, case_sensitive=False):
    
    if isinstance(context_or_element,webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att,locator_text)
    
    element_text = element.text
    if not case_sensitive:
        if expected_text.lower() in element_text.lower():
            return True
        else: return False
    else:
        return True if expected_text in element_text else False
        
