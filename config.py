# Code Configuration File
from datetime import date

#Database Configuration
host='localhost'
database='stock'
user='root'
port=3306
password='root'

#DHIS2 Configuration 
dhis_url="https://hmis.moh.ps/tr-dev-integration"
dhis_user='Saleh'
dhis_password='Test@123'

# global variable Configuration
today = date.today()
today_date = today.strftime("%Y-%m-%d")