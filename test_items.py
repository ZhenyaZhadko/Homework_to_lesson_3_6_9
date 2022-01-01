import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_item_has_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    btn = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert btn is not None, 'no add to cart button'
    