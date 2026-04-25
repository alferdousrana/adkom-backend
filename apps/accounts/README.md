# Accounts

## Purpose
User profile and address management.

## Can run alone?
No

## Required dependencies
- AUTH_USER_MODEL

## Models
- Profile
- Address

## Selectors
- get_user_profile
- get_user_addresses

## Services
- update_profile
- set_default_address

## Signals
- auto create profile on user creation

## URLs
/api/accounts/