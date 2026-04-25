# Notification

## Purpose
Store and manage user notifications.

## Can run alone?
Yes

## Required dependencies
- Django AUTH_USER_MODEL

## Models
- Notification

## Selectors
- get_user_notifications
- get_unread_notifications

## Services
- create_notification
- mark_notification_as_read

## Signals listened
- order_created
- product_stock_low (future)

## URLs
/api/notifications/