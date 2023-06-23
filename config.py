# Code Configuration File
import calendar
from datetime import date, datetime,timedelta
# Database Configuration
host = 'localhost'
database = 'stock'
user = 'root'
port = 8889
password = 'root'

# DHIS2 Configuration
dhis_url = "https://hmis.moh.ps/tr-family-prod"
dhis_user = 'Saleh'
dhis_password = 'Test@123'

# DHIS2 Program Configuration pharmacy program
programId = "vj5cpA2OOfZ"
# DHIS2 Program Configuration pharmacy stock program
programIdStock = "JK1cEZufnoP"

#LijzB622Z22 > Pharmacy_QTY_Stock_Despensed
dataElementForQuantity = "LijzB622Z22"
#bry41dJZ99x > Pharmacy_QTY_Stock_Total
dataElementForTotalQuantity = "bry41dJZ99x"
#eskqGfai0gc > Pharmacy_QTY_Stock
dataElementForQuantityStock = "eskqGfai0gc"

# DHIS2 Program Stage Configuration
# Prescribed medications (الوصفة الطبية)
stageForPrescribedMedications = "JV6n7FhC7xp"

# DHIS2 DataElement Configuration For Prescribed
Pharm_Medicine_Name = "aM2Vn0UUPJB"
Pharm_Medicine_Name_1 = "WSeukMBwbQ3"
Pharm_Medicine_Name_2 = "TORfS27wR0q"
Pharm_Medicine_Name_3 = "TnrWDEL4PoR"
Pharm_Medicine_Name_4 = "iy166uomfXk"
Pharm_Medicine_Name_5 = "ntECq4xEo24"
Pharm_Medicine_Name_6 = "Ne2veOUhPw0"
Pharm_Medicine_Name_7 = "R2rxr1Z8i4v"
Pharm_Medicine_Name_8 = "Dlx79ePwf1g"
Pharm_Medicine_Name_9 = "oTCRn8enMzd"
Pharm_Medicine_Name_10 = "nTd67mb0PJe"

Pharmacy_QTY_Despensed = "HS5mppnnRUD"
Pharmacy_QTY_Despensed_1 = "Kzxa8SKjCdp"
Pharmacy_QTY_Despensed_2 = "wmkND48fkvf"
Pharmacy_QTY_Despensed_3 = "sm78nae74E0"
Pharmacy_QTY_Despensed_4 = "YR7bARfLBay"
Pharmacy_QTY_Despensed_5 = "Pl3jCeEVYVG"
Pharmacy_QTY_Despensed_6 = "J6s8Ju9Y1xk"
Pharmacy_QTY_Despensed_7 = "xFAUNJilvDg"
Pharmacy_QTY_Despensed_8 = "tn3XjDR6aUt"
Pharmacy_QTY_Despensed_9 = "H2g1tcKI0sK"
Pharmacy_QTY_Despensed_10 = "wFeFcxSnOO0"

# global variable Configuration
today = date.today()
today_date = today.strftime("%Y-%m-%d")
# yesterday = today - timedelta(days=1)
# today_date = yesterday.strftime("%Y-%m-%d")

# Time Settings
todayDateTime = datetime.now().today()
first_day = todayDateTime.replace(day=1).strftime("%Y-%m-%d")
last_day = todayDateTime.replace(day=calendar.monthrange(
    todayDateTime.year, todayDateTime.month)[1]).strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")