

LOCATORS = {
    'main navigation' : {'type':'id', 'locator':'mainnav'},
    'top navigation': {'type':'id', 'locator':'top'},
    'options':{'type':'css selector','locator':'.options-bar'}

}

MY_ACCOUNT_LOCATORS = {
    'login_user_name':{'type':'id', 'locator':'username'},
    'login_user_password':{'type':'id', 'locator':'password'},
    'login_btn':{'type':'css selector', 'locator':'button[name="login"]'},
    'left_nav':{'type':'css selector', 'locator':'div.entry-content nav.woocommerce-MyAccount-navigation'},
    'left_nav_logout_btn':{'type':'css selector', 'locator':'div.entry-content nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)'},
    'error_box':{'type':'css selector', 'locator':'ul.woocommerce-error'},
}