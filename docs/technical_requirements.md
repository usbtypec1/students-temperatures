# 1. Project purposes
The system where students of 11-J class 
could mark their temperatures in telegram bot need to be developed. 
I am doing it because it annoys me when someone sends 
his senseless message to main whatsapp group.

# 2. Description
There will be two different types of users - students and admins.
Authentication via telegram id.

1. Student:
   - Mark his own temperature
   - Mark his classmate's temperature
   - View his own temperature's history
2. Admin:
   - View all temperatures
   - Export all temperatures as excel
   - Send notifications to students to mark their temperatures
3. Non-user:
   - Non-users have no access to the telegram bot
   
# 3. Technology stack
- aiogram
- peewee orm
- openpyxl
- fuzzywuzzy
- pendulum

# 4. Hosting
The project will be hosted on Heroku