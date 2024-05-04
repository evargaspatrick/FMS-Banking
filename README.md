# FMS-Banking
FMS stands for - Financial Management System. This is a finance management app 
I created as my Database Systems Final project.

Currently it is only set to make new user accounts, associate bank account 
types with users main accounts, make and record transactions with other accounts 
within the programs database. It does feature logging in, 
protection of user sessions and error handling for accounts that don't exist when
making transactions.

How to use:

Pull app.py, FMS.db, and the templates folder into a project in your python IDE.

Then run app.py, and go to the url provided in the console or the host ip set 
in app.run


The database does come with two users already added for testing purposes.

Username1:Matt762
Password1:1234qwer

Username2:Eddy1994
Password2:19941234

Future development of the project will include password hashing for users, and the
following tables:
-Category
  Used for categorizing expenses.
-Budgets
  Used to manage budgets set by users
-Income
  Used to track users income over time
-Financial Reports
  Used to store financial reports for users. Reports generated based on all factors 
  associated with the users accounts, like income, expense, budget limit, etc. Detailing
  how well each users account is meeting their goals and the direction the account is heading.
