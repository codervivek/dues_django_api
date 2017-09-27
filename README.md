# Dues API

A api that maintains money transaction for multiple users

## Testing

Make POST request on [this link](codervivek.pythonanywhere.com/transaction) to add your transaction to the database. For GET, POST, PUT and DELETE request you need to know the id of your transaction which can be noted from the [previous link](codervivek.pythonanywhere.com/transaction).

For GET, POST, PUT and DELETE, make appropiate request on codervivek.pythonanywhere.com/transaction/(id).

The request should contain user_to, user_from and value variables for borrower, lender and transaction value respectively. An optional name variable can also be added for quick reference without id.
