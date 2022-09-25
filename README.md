<!-- # pharmacy_stock
pharmacy stock project
  -->
Pharmacy Stock System – WHO/PNIPH Palestine Project with DHIS2 System

System Steps:
•	Connect with local database
•	Get category data [this data to mapping medication name with medication id on dhis2]
•	Get event data from every organization from dhis2 by today date and return array
•	If array empty will stop else will start store all data to local database
•	After store all data to local database will start loop to update every event on capture app on dhis2
How to use system:
•	Prefer install Linux server inside dhis2 server
•	Must install MySQL database then set all credentials to python code
•	Must install python3 to run python code
•	Must install all library dependences you can find it on [project/requirement.py]
•	Set cron job to run python code multi time on same day
•	Prefer to setup this code as a service on Linux server
•	Must add to cron job and service to set all running python code [job] to write to logs file
System needs:
•	Prefer to make local connection between code server and dhis server to increase speed of request.
•	API from dhis2 with admin user.
•	Change program access to small list of organization just used to minimized loop.
•	Backup service to make sure don’t lose local database.
System Configurations:
*Configuration file path is (project/config.py)
•	Change database information
•	Change API information
•	Change log file information

System Files:
•	Main.py to run code step by step
•	Config.py to store all configuration necessary for run code
•	Requriment.py to install all python library to run code on server
•	/Function folder store all functions used on code
•	

