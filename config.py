# Code Configuration File
import calendar
from datetime import date,datetime
#Database Configuration
host='localhost'
database='stock'
user='root'
port=8889
password='root'

#DHIS2 Configuration 
dhis_url="https://hmis.moh.ps/tr-family-stg"
dhis_user='Saleh'
dhis_password='Test@123'

#DHIS2 Program Conf pharmacy program
programId="vj5cpA2OOfZ"

#DHIS2 Program Conf pharmacy stock program
programIdStock="JK1cEZufnoP"
dataElementForQuantity="LijzB622Z22"
dataElementForTotalQuantity="bry41dJZ99x"
dataElementForQuantityStock="eskqGfai0gc"
# global variable Configuration
today = date.today()
today_date = today.strftime("%Y-%m-%d")

#Time Settings
todayDateTime = datetime.now().today()
first_day = todayDateTime.replace(day=1).strftime("%Y-%m-%d")
last_day = todayDateTime.replace(day=calendar.monthrange(todayDateTime.year, todayDateTime.month)[1]).strftime("%Y-%m-%d")  
current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")  
#TODO:: Most ADD Program IDs