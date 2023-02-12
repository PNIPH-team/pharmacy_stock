# Code Configuration File
import calendar
from datetime import date, datetime
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
# Most frequently requested Medications (الوصفة الطبية للأدوية الأكثر طلباً)
stageForFrequentlyMedications = "tJQ1UCpkCy2"
# Prescribed medications (الوصفة الطبية)
stageForPrescribedMedications = "JV6n7FhC7xp"

# DHIS2 DataElement Configuration For Frequent TODO::
#Atorvastatin 40mg tab
Pharmacy_FrequentlyMedication_Despensed_1 = "gTreHa9FsAJ"
#AMLODIPINE 5MG TAB
Pharmacy_FrequentlyMedication_Despensed_2 = "nubIuNPn6kP"
#BISOPROLOL 5MG TAB
Pharmacy_FrequentlyMedication_Despensed_3 = "UOVMe9Hftr8"
#METFORMIN 850MG TAB
Pharmacy_FrequentlyMedication_Despensed_4 = "cMVX1z75Uvh"
#SITAGLIPTIN 50 MG FC TAB
Pharmacy_FrequentlyMedication_Despensed_5 = "B3rbznpTyjJ"
#ENALAPRIL MALEATE 20 MG TAB
Pharmacy_FrequentlyMedication_Despensed_6 = "nxfbinD79RB"
#ENALAPRIL MALEATE 5MG TAB
Pharmacy_FrequentlyMedication_Despensed_7 = "BIP1buozD2e"
#glimepiride 4mg tab
Pharmacy_FrequentlyMedication_Despensed_8 = "xGxzPWNaSuz"
#glimepiride 2mg tab
Pharmacy_FrequentlyMedication_Despensed_9 = "Fe9k17OVHPe"
#ISOSORBIDE 5-MONONITRATE 20MG TAB
Pharmacy_FrequentlyMedication_Despensed_10 = "wiLMg4LNV3V"
#losartan 50mg tab
Pharmacy_FrequentlyMedication_Despensed_11 = "z8F0ZEgFeeY"
#SALBUTAMOL 100 MCG/INHAL.AERESOL
Pharmacy_FrequentlyMedication_Despensed_12 = "btTycEIdfBr"
#ipratropium br. 20mcg/inh aerosol
Pharmacy_FrequentlyMedication_Despensed_13 = "vO16pLLv3u8"
#OMEPRAZOLE 20MG TAB
Pharmacy_FrequentlyMedication_Despensed_14 = "mIKc81UxFte"
#ASPIRIN 100MG TAB > ASA100 
Pharmacy_FrequentlyMedication_Despensed_15 = "E9jrv79ERKn"

#ALLOPURINOL 100MG TAB
Pharmacy_FrequentlyMedication_Despensed_16 = "ry8kRsZatrw"
#ATENOLOL 100 MG TAB
Pharmacy_FrequentlyMedication_Despensed_17 = "IvezvIj11iz"
#atenolol 25mg tab
Pharmacy_FrequentlyMedication_Despensed_18 = "D347s7IUkjK"
#BETAHISTINE 16 MG TAB
Pharmacy_FrequentlyMedication_Despensed_19 = "Q84esKzMmYs"
#CALCIUM CARBONATE 600MG TAB
Pharmacy_FrequentlyMedication_Despensed_20 = "G66ZdNC3FqY"
#spiranolactone 25mg tab
Pharmacy_FrequentlyMedication_Despensed_21 = "UC6JHXwx3Hz"
#SPIRONOLACTONE 100MG TAB
Pharmacy_FrequentlyMedication_Despensed_22 = "DFVoiFY5yYB"
#ALFACALCIDOL 0.25MCG CAP
Pharmacy_FrequentlyMedication_Despensed_23 = "bzw3bRoK3BK"
#FERROUS SLF160MG (50 mg iron)+FOLIC ACID 400MCG TAB
Pharmacy_FrequentlyMedication_Despensed_24 = "UEdekMTLaOD"
#FUROSEMIDE 40MG TAB
Pharmacy_FrequentlyMedication_Despensed_25 = "MLOaEJLcXdr"
#METHOTREXATE SOD 2.5MG TAB
Pharmacy_FrequentlyMedication_Despensed_26 = "Gb1rLlO88Aw"
#DOXAZOCIN 2MG TAB
Pharmacy_FrequentlyMedication_Despensed_27 = "XDynXCU80K9"
#PREDNISOLONE 20MG TAB
Pharmacy_FrequentlyMedication_Despensed_28 = "jhXKcFrD2H5"
#PREDNISOLONE 5MG TAB
Pharmacy_FrequentlyMedication_Despensed_29 = "gWNkIQhm83O"
#HYDROCHLORTHIAZIDE 25MG TAB
Pharmacy_FrequentlyMedication_Despensed_30 = "Ba6tDEJazGg"
#thyroxine 50mcg tab
Pharmacy_FrequentlyMedication_Despensed_31 = "Lgu3fy8j3nI"
#THYROXINE 100MCG TAB
Pharmacy_FrequentlyMedication_Despensed_32 = "s0f27FZvhYA"
#clopidogrel 75mg tab
Pharmacy_FrequentlyMedication_Despensed_33 = "TXQCucsLPN6"
#sitaGLIPTIN 100 MG FC TAB
Pharmacy_FrequentlyMedication_Despensed_34 = "p72J1JjnMgY"
#INSULIN HUMAN30/70 100U/ML 10ML
Pharmacy_FrequentlyMedication_Despensed_35 = "rD0kNTy5tb7"
#LONG ACTING INSULIN ANALOGUE (GLARGINE ) 100 U / ML PFP
Pharmacy_FrequentlyMedication_Despensed_36 = "DxLjtPNi2bQ"
#LONG ACTING INSULIN ANALOGUE ( DETEMIR ) 100 U / ML PFP
Pharmacy_FrequentlyMedication_Despensed_37 = "SYDoi6GvYIR"
#INSULIN NPH HM 100U/ML 10ML
Pharmacy_FrequentlyMedication_Despensed_38 = "T26sgrwec0u"
#INSULIN ACTRAPID 100U/ML VIAL 10ML
Pharmacy_FrequentlyMedication_Despensed_39 = "oQsgVbFL86L"
#RAPID ACTING INSULIN ANALOGUE(LISPRO  ) 100 U / ML PFP
Pharmacy_FrequentlyMedication_Despensed_40 = "V0pLuvHjCEV"
#RAPID ACTING INSULIN ANALOGUE( GLULISINE ) 100 U / ML PFP
Pharmacy_FrequentlyMedication_Despensed_41 = "jo7BBm7d2Mr"
#RAPID ACTING INSULIN ANALOGUE(ASPART ) 100 U / ML PFP
Pharmacy_FrequentlyMedication_Despensed_42 = "kHpybDQh3Cl"
#Famotidine 20
Pharmacy_FrequentlyMedication_Despensed_43 = "ckmKHgOXCVE"
#Famotidine40
Pharmacy_FrequentlyMedication_Despensed_44 = "EJEcZe7joMr"
##
# 1
Pharmacy_Frequently_Order_Atorvastatin = "g3jYfDWMlju"
Pharmacy_Frequently_Order_Atorvastatin_code = "M-301-1001"
# 2
Pharmacy_Frequently_Order_AMLODIPINE = "ezwWMPb12eO"
Pharmacy_Frequently_Order_AMLODIPINE_code = "M-123-1004"
# 3
Pharmacy_Frequently_Order_BISOPROLOL = "iifVrszTRRz"
Pharmacy_Frequently_Order_BISOPROLOL_code = "M-123-1018"
# 4
Pharmacy_Frequently_Order_METFORMIN = "KIZvcIfQvpT"
Pharmacy_Frequently_Order_METFORMIN_code = "M-192-1010"
# 5
Pharmacy_Frequently_Order_SITAGLIPTIN = "qs0I9NsfUxu"
Pharmacy_Frequently_Order_SITAGLIPTIN_code = "M-192-1035"
# 6
Pharmacy_Frequently_Order_ENALAPRIL20 = "YxFGAkRihhj"
Pharmacy_Frequently_Order_ENALAPRIL20_code = "M-123-1030"
# 7
Pharmacy_Frequently_Order_ENALAPRIL5 = "x2qkkLksG0N"
Pharmacy_Frequently_Order_ENALAPRIL5_code = "M-123-1035"
# 8
Pharmacy_Frequently_Order_glimepiride4 = "uuaO52vR7Sc"
Pharmacy_Frequently_Order_glimepiride4_code = "M-192-1016"
# 9
Pharmacy_Frequently_Order_glimepiride2 = "cgKw0UiSSzA"
Pharmacy_Frequently_Order_glimepiride2_code = "M-192-1012"
# 10
Pharmacy_Frequently_Order_ISOSORBIDE = "A0WmBW0xr3Q"
Pharmacy_Frequently_Order_ISOSORBIDE_code = "M-121-1020"
# 11
Pharmacy_Frequently_Order_losartan = "igbaI5cMEch"
Pharmacy_Frequently_Order_losartan_code = "M-123-1041"
# 12
Pharmacy_Frequently_Order_SALBUTAMOL = "tXnR137oYs6"
Pharmacy_Frequently_Order_SALBUTAMOL_code = "M-251-4012"
# 13
Pharmacy_Frequently_Order_ipratropium = "joyfXYlQ0aS"
Pharmacy_Frequently_Order_ipratropium_code = "M-251-4013"
# 14
Pharmacy_Frequently_Order_OMEPRAZOLE = "Oh5NachZvua"
Pharmacy_Frequently_Order_OMEPRAZOLE_code = "M-181-1018"
# 15
Pharmacy_Frequently_Order_ASA100 = "PTofmQ8rssJ"
Pharmacy_Frequently_Order_ASA100_code = "M-129-1005"




# 16 ALLOPURINOL 100MG TAB
Pharmacy_Frequently_Order_ALLOPURINOL = "vQgn6p43wLx"
Pharmacy_Frequently_Order_ALLOPURINOL_code = "M-023-1005"
# 17 ATENOLOL 100 MG TAB
Pharmacy_Frequently_Order_ATENOLOL = "hUNjHS135uW"
Pharmacy_Frequently_Order_ATENOLOL_code = "M-123-1005"
# 18 atenolol 25mg tab
Pharmacy_Frequently_Order_atenolol25  = "jIpsHz7RZzT"
Pharmacy_Frequently_Order_atenolol25_code = "M-123-1007"

# 19 BETAHISTINE 16 MG TAB
Pharmacy_Frequently_Order_BETAHISTINE = "WZ0MhAO5wf0"
Pharmacy_Frequently_Order_BETAHISTINE_code = "M-161-1006"

# 20 CALCIUM CARBONATE 600MG TAB
Pharmacy_Frequently_Order_CALCIUM = "lzK3njVRwOZ"
Pharmacy_Frequently_Order_CALCIUM_code = "M-181-1015"

# 21 spiranolactone 25mg tab
Pharmacy_Frequently_Order_spiranolactone = "f03rinjJRR2"
Pharmacy_Frequently_Order_spiranolactone_code = "M-276-1024"

# 22 Pharmacy_Frequently_Order_SPIRONOLACTONE 100MG TAB
Pharmacy_Frequently_Order_SPIRONOLACTONE  = "oTzQwOTWdlQ"
Pharmacy_Frequently_Order_SPIRONOLACTONE_code  = "M-276-1025"
# 23 Pharmacy_Frequently_Order_ALFACALCIDOL
Pharmacy_Frequently_Order_ALFACALCIDOL = "JbPF7d4IDMl"
Pharmacy_Frequently_Order_ALFACALCIDOL_code = "M-281-1010"

# 24 Pharmacy_Frequently_Order_FERROUS
Pharmacy_Frequently_Order_FERROUS = "EibobwKam9U"
Pharmacy_Frequently_Order_FERROUS_code = "M-282-1015"
# 25 Pharmacy_Frequently_Order_FUROSEMIDE
Pharmacy_Frequently_Order_FUROSEMIDE = "aINleJ8qczK"
Pharmacy_Frequently_Order_FUROSEMIDE_code = "M-276-1020"
# 26 Pharmacy_Frequently_Order_METHOTREXATE
Pharmacy_Frequently_Order_METHOTREXATE = "PF7eaoiv0tm"
Pharmacy_Frequently_Order_METHOTREXATE_code = "M-101-1035"
# 27 Pharmacy_Frequently_Order_DOXAZOCIN
Pharmacy_Frequently_Order_DOXAZOCIN = "wpjFPdATwbX"
Pharmacy_Frequently_Order_DOXAZOCIN_code = "M-123-1051"
# 28 Pharmacy_Frequently_Order_PREDNISOLONE
Pharmacy_Frequently_Order_PREDNISOLONE = "CTo1ENfBsCJ"
Pharmacy_Frequently_Order_PREDNISOLONE_code = "M-195-1020"
# 29 Pharmacy_Frequently_Order_PREDNISOLONE 5MG TAB
Pharmacy_Frequently_Order_PREDNISOLONE5  = "zEU3LxkgeX3"
Pharmacy_Frequently_Order_PREDNISOLONE5_code  = "M-195-1025"
# 30 Pharmacy_Frequently_Order_HYDROCHLORTHIAZIDE
Pharmacy_Frequently_Order_HYDROCHLORTHIAZIDE  = "cFL18VLURqD"
Pharmacy_Frequently_Order_HYDROCHLORTHIAZIDE_code  = "M-276-1050"
# 31 Pharmacy_Frequently_Order_thyroxine 50mcg tab
Pharmacy_Frequently_Order_thyroxine50   = "E2EIutFNVX3"
Pharmacy_Frequently_Order_thyroxine50_code  = "M-194-1013"
# 32 Pharmacy_Frequently_Order_THYROXINE
Pharmacy_Frequently_Order_THYROXINE  = "pci1aFjbTIp"
Pharmacy_Frequently_Order_THYROXINE_code  = "M-194-1015"
# 33 Pharmacy_Frequently_Order_clopidogrel
Pharmacy_Frequently_Order_clopidogrel  = "kCD8Xwtjcgy"
Pharmacy_Frequently_Order_clopidogrel_code  = "M-112-1003"
# 34 Pharmacy_Frequently_Order_sitaGLIPTIN
Pharmacy_Frequently_Order_sitaGLIPTIN  = "Ld7JRKE8g48"
Pharmacy_Frequently_Order_sitaGLIPTIN_code  = "M-192-1036"
# 35 Pharmacy_Frequently_Order_INSULIN
Pharmacy_Frequently_Order_INSULIN  = "JvnUNViHBVa"
Pharmacy_Frequently_Order_INSULIN_code  = "M-191-0010"
# 36 Pharmacy_Frequently_Order_GLARGINE
Pharmacy_Frequently_Order_GLARGINE  = "JH1RjqRXdRB"
Pharmacy_Frequently_Order_GLARGINE_code  = "GLARGINE"
# 37 Pharmacy_Frequently_Order_DETEMIR
Pharmacy_Frequently_Order_DETEMIR  = "DETEMIR"
Pharmacy_Frequently_Order_DETEMIR_code  = "T09111EdJZ6"
# 38 Pharmacy_Frequently_Order_INSULIN NPH HM
Pharmacy_Frequently_Order_INSULIN_NPH   = "mXQgGN5ixoK"
Pharmacy_Frequently_Order_INSULIN_NPH_code  = "M-191-0015"
# 39 Pharmacy_Frequently_Order_INSULIN ACTRAPID
Pharmacy_Frequently_Order_INSULIN_ACT   = "vBREaiw8hXQ"
Pharmacy_Frequently_Order_INSULIN_ACT_code   = "M-191-0005"
# 40 Pharmacy_Frequently_Order_LISPRO
Pharmacy_Frequently_Order_LISPRO  = "JFeLUqPdPzS"
Pharmacy_Frequently_Order_LISPRO_code  = "LISPRO"
# 41 Pharmacy_Frequently_Order_GLULISINE
Pharmacy_Frequently_Order_GLULISINE  = "Pul8hn2O9Yv"
Pharmacy_Frequently_Order_GLULISINE_code  = "GLULISINE"
# 42 Pharmacy_Frequently_Order_ASPART
Pharmacy_Frequently_Order_ASPART  = "al2QYMnQXGv"
Pharmacy_Frequently_Order_ASPART_code  = "ASPART"
# 43 Pharmacy_Frequently_Order_Famotidine 20
Pharmacy_Frequently_Order_Famotidine   = "v0np97mr2po"
Pharmacy_Frequently_Order_Famotidine_code   = "FAMOTIDINE 20mg"
# 44 Pharmacy_Frequently_Order_Famotidine40
Pharmacy_Frequently_Order_Famotidine40  = "C02vkeyiJXv"
Pharmacy_Frequently_Order_Famotidine40_code  = "FAMOTIDINE 40mg"




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

# Time Settings
todayDateTime = datetime.now().today()
first_day = todayDateTime.replace(day=1).strftime("%Y-%m-%d")
last_day = todayDateTime.replace(day=calendar.monthrange(
    todayDateTime.year, todayDateTime.month)[1]).strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")