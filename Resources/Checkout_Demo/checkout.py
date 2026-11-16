"""Checkout pricing for the online store.

Pricing rules (from the product team):

1. Subtotal is the sum of price x quantity for every line item.
2. A coupon is applied to the subtotal. Coupons are either a percent off
   ({"percent": 10}) or a fixed amount off ({"amount": 15}). A coupon can
   reduce the price to $0 but never below it.
3. Shipping is free when the subtotal BEFORE the coupon is $50.00 or more.
   Otherwise shipping costs $5.99. (Customers see "Free shipping!" in the
   cart before they enter a coupon, so a coupon must not take it away.)
4. Sales tax of 8% applies to the discounted subtotal, not to shipping.
5. The total is rounded to the nearest cent.
"""

FREE_SHIPPING_THRESHOLD = 50.00
SHIPPING_FEE = 5.99
TAX_RATE = 0.08


def subtotal(items):
    return sum(item["price"] for item in items)


def apply_coupon(amount, coupon):
    if coupon is None:
        return amount
    if "percent" in coupon:
        return amount * coupon["percent"] / 100
    if "amount" in coupon:
        return amount - coupon["amount"]
    raise ValueError(f"Unknown coupon: {coupon}")


def shipping(amount):
    return 0.0 if amount >= FREE_SHIPPING_THRESHOLD else SHIPPING_FEE


def order_total(items, coupon=None):
    before_coupon = subtotal(items)
    discounted = apply_coupon(before_coupon, coupon)
    tax = discounted * TAX_RATE
    return round(discounted + tax + shipping(discounted), 2)
