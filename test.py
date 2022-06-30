from base import *
from locators import *
from constants import *

print("In test.py")
try:
    launch_browser()
    load_url(base_url)
    wait_and_find_element(change_address)
    wait_and_click('Change Button', change_address)
    wait_and_enter_text(location_input_field, zip_code)
    wait_and_click('Submit Zip Code', location_update_submit_button)
    press_escape_button()
    wait_and_find_element(search_field)
    wait_and_enter_text(search_field, search_parameter)
    time.sleep(2)
    wait_for_element_and_press_enter(search_field)
    shoeElement = wait_and_find_element(shoe_colors)
    parentNode = shoeElement.find_element_by_xpath('./../../../../..')
    shoeName = parentNode.find_element_by_xpath("./div[2]/h2/a/span").text
    print(shoeName)
    shoeElement.click()
    time.sleep(2)
    productName = get_element_text(shoe_heading)
    if (shoeName in productName):
        print("Item Verified")
    else:
        print("Items do not match")
    selectSizeText = get_element_text(shoe_size_heading)
    newSizeText = get_element_text(first_shoe_size_heading)
    wait_and_click("Clicking on Shoe", first_shoe_size)
    updatedSelectSizeText = get_element_text(shoe_size_heading)

    if (selectSizeText != updatedSelectSizeText):
        print("Select Size text updated")
    else:
        print("Select Size text not updated")

    updatedPrice = get_element_text(price_heading)
    print("Price Updated - $" + updatedPrice)

    shoeCost = updatedPrice + '.' + get_element_text(price_decimal_fraction)
    print("Shoe Cost - $" + shoeCost)

    wait_and_click("Add to Cart", add_to_cart_button)
    cartPrice = get_element_text(cart_page_price)
    print("Cart Page Price - $" + cartPrice)

    if (updatedPrice == cartPrice):
        print("Cart Price verified with Shoe cost")
    else:
        print("Shoe cost and Cart Price do not match")

    press_back_button()
    wait_and_click("Add to Cart", add_to_cart_button)
    newCartPrice = get_element_text(cart_page_price) + '.0'
    print("Updated Cart Page Price - $" + newCartPrice)
    totalShoesCost = (float(shoeCost)) * 2
    print("Total Cost of Shoes - $" + str(math.modf(totalShoesCost)[1]))
    if (newCartPrice == str(math.modf(totalShoesCost)[1])):
        print("Updated Cart Page Price after adding more shoes - Price: $" + newCartPrice)
    else:
        print("Cart Price not updated")

    close_browser()

except Exception as e:
    print(e)
