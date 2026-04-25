# Checkout

## Purpose
Convert cart into orders and manage order lifecycle.

## Can run alone?
No

## Required dependencies
- Cart
- Product
- Accounts

## Models
- Order
- OrderItem

## Selectors
- get_user_orders

## Services
- create_order_from_cart
- mark_order_paid
- cancel_order

## URLs
/api/checkout/