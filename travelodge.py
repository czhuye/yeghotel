import requests
import json

json_payload = "Tk_Tot=1&Tk_MinMax=0&no_adult=2&no_child=0&arr_dt=11%2F11%2F2025&no_nights=3&no_rooms=1&Pkg_Code=W21X3&Pkg_Code_Sel=W21X3&Disp_Type=0&region=&RmSu_Type=&Prp_ID=&prop_id=&opt_child_0=&opt_child_1=&opt_child_2=&opt_child_3=&opt_child_4=&Off_50=&Prop_Name=&RmSu_Type=&txtReturnDate=&Seach_For=&Partner_ID=&Start_At=1&Prop_Bonus=&Pkg_Type=&Lng=English&PkTk_1=Winte116"
post = 'https://www.bookings.edmontonsbesthotels.com/English/Central_Packages_Hotels.asp'

response = requests.get(post)
print(response.text)
html_content = response.text

url = 'https://www.bookings.edmontonsbesthotels.com/English/GetCentralHotelRate.asp?propid=ARM&custid=104.219.10.26_867113300|926202541056PM&DoGlobalSearch=Yes&opt_child_0=1&opt_child_1=1&opt_child_2=1&opt_child_3=1&opt_child_4=1&Sort_Str=Disp_Ord&PegsMeta_SearchType=&Listing_Order=1&Tot_Price_Tk=0.00&Tot_Price_Inventory_Tkt=0.00&Pkg_Code=W21X3&Pkg_Rate_Code=PKG_Rates&Call_From=Listing'

response = requests.get(url)
print(response.text)
