import os
from datetime import date
from datetime import datetime
import time

from functions.connect_database import connect_database
from functions.category_options import category_options
from functions.module.get_org_data import get_org_data
def main():
    connect_database()
    today = date.today()
    today_date = today.strftime("%Y-%m-%d")
    if not os.path.exists('categoryOptions.json'):
        category_options()
    get_org_data(today_date)
if __name__ == "__main__":
    main()