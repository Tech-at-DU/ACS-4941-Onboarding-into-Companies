import pytest

from checkout import apply_coupon, order_total, shipping, subtotal

MUG = {"name": "Mug", "price": 12.00, "qty": 1}
HOODIE = {"name": "Hoodie", "price": 52.00, "qty": 1}


def test_subtotal_single_item():
    assert subtotal([MUG]) == 12.00


def test_subtotal_multiplies_by_quantity():
    assert subtotal([{"name": "Sticker", "price": 3.50, "qty": 4}]) == 14.00


def test_shipping_charged_under_threshold():
    assert shipping(49.99) == 5.99


def test_free_shipping_at_threshold():
    assert shipping(50.00) == 0.0


def test_order_total_small_order_pays_shipping():
    # 12.00 + 8% tax (0.96) + 5.99 shipping
    assert order_total([MUG]) == 18.95


def test_order_total_with_quantity():
    # 3 mugs = 36.00 + 2.88 tax + 5.99 shipping
    assert order_total([{"name": "Mug", "price": 12.00, "qty": 3}]) == 44.87


def test_percent_coupon():
    assert apply_coupon(100.00, {"percent": 10}) == pytest.approx(90.00)


def test_fixed_coupon():
    assert apply_coupon(100.00, {"amount": 15}) == 85.00


def test_coupon_never_goes_below_zero():
    assert apply_coupon(10.00, {"amount": 15}) == 0.00


def test_coupon_does_not_remove_free_shipping():
    # Subtotal 52.00 qualifies for free shipping BEFORE the coupon.
    # 10% off -> 46.80, + 8% tax (3.744) -> 50.54, shipping stays free.
    assert order_total([HOODIE], {"percent": 10}) == 50.54
