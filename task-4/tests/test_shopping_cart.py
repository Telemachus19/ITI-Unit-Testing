import pytest
from src.shopping_cart import ShoppingCart

def test_add_new_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    items = cart.get_items()
    assert "Apple" in items
    assert items["Apple"]["price"] == 1.5
    assert items["Apple"]["quantity"] == 3

def test_add_existing_item_increases_quantity():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Apple", 1.5, 2)
    items = cart.get_items()
    assert items["Apple"]["quantity"] == 5

def test_add_existing_item_updates_price():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Apple", 1.8, 2)
    items = cart.get_items()
    assert items["Apple"]["price"] == 1.8
    assert items["Apple"]["quantity"] == 5

def test_add_item_strips_whitespace():
    cart = ShoppingCart()
    cart.add_item("  Apple  ", 1.5, 3)
    items = cart.get_items()
    assert "Apple" in items
    assert "  Apple  " not in items

def test_add_item_invalid_name():
    cart = ShoppingCart()
    correct_string = "Item name must be a non-empty string"
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("", 1.5, 3)
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("   ", 1.5, 3)
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item(None, 1.5, 3)
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item(123, 1.5, 3)

def test_add_item_invalid_price():
    cart = ShoppingCart()
    correct_string = "Price must be a non-negative number"
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("Apple", -0.5, 3)
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("Apple", "free", 3)

def test_add_item_invalid_quantity():
    cart = ShoppingCart()
    correct_string = "Quantity must be an integer greater than zero"
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("Apple", 1.5, 0)
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("Apple", 1.5, -3)
    with pytest.raises(ValueError, match=correct_string):
        cart.add_item("Apple", 1.5, 1.5)

def test_remove_item_fully_by_default():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.remove_item("Apple")
    assert "Apple" not in cart.get_items()

def test_remove_item_partially():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.remove_item("Apple", 1)
    items = cart.get_items()
    assert items["Apple"]["quantity"] == 2

def test_remove_item_more_than_exists_removes_completely():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.remove_item("Apple", 5)
    assert "Apple" not in cart.get_items()

def test_remove_item_not_in_cart():
    cart = ShoppingCart()
    # I hope this doesn't break.
    correct_string = "Item 'Banana' is not in the shopping cart"
    with pytest.raises(ValueError, match=correct_string):
        cart.remove_item("Banana")

def test_remove_item_invalid_name():
    cart = ShoppingCart()
    correct_string = "Item name must be a non-empty string"
    with pytest.raises(ValueError, match=correct_string):
        cart.remove_item("")
    with pytest.raises(ValueError, match=correct_string):
        cart.remove_item(None)

def test_remove_item_invalid_quantity():
    cart = ShoppingCart()
    correct_string = "Quantity to remove must be an integer greater than zero"
    cart.add_item("Apple", 1.5, 3)
    with pytest.raises(ValueError, match=correct_string):
        cart.remove_item("Apple", 0)
    with pytest.raises(ValueError, match=correct_string):
        cart.remove_item("Apple", -1)
    with pytest.raises(ValueError, match=correct_string):
        cart.remove_item("Apple", 1.5)

def test_calculate_total_empty_cart():
    cart = ShoppingCart()
    assert cart.calculate_total() == 0.0

def test_calculate_total_multiple_items():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)  # 4.5
    cart.add_item("Banana", 0.8, 5) # 4.0
    assert cart.calculate_total() == 8.5

def test_calculate_total_float_precision():
    cart = ShoppingCart()
    cart.add_item("Apple", 0.1, 1)
    cart.add_item("Banana", 0.2, 1)
    assert cart.calculate_total() == 0.3

def test_clear_cart():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.clear()
    assert len(cart.get_items()) == 0
    assert cart.calculate_total() == 0.0
