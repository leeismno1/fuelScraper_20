import requests
import feedparser
from pprint import pprint
import os

# Region Codes

regions = {'NORTH_OF_RIVER' : 25,
'SOUTH_OF_RIVER' : 26,
'EAST_HILLS' : 27,
'ALBANY' : 15 ,
'AUGUSTA_MARGARET_RIVER' : 28,  
'BRIDGETOWN_GREENBUSHES' : 30 ,
'BOULDER' : 1,  
'BROOME' : 2, 
'BUNBURY' : 16, 
'BUSSELTON_TOWNSITE' : 3, 
'BUSSELTON_SHIRE' : 29, 
'CAPEL' : 19, 
'CARNARVON' : 4, 
'CATABY' : 33, 
'COLLIE' : 5,
'COOLGARDIE' : 34, 
'CUNDERDIN' : 35,
'DONNYBROOK_BALINGUP' : 31,  
'DALWALLINU' : 36, 
'DAMPIER' : 6, 
'DARDANUP' : 20, 
'DENMARK' : 37, 
'DERBY' : 38, 
'DONGARA' : 39, 
'ESPERANCE' : 7, 
'EXMOUTH' : 40, 
'FITZROY_CROSSING' : 41, 
'GERALDTON' : 17, 
'GREENOUGH' : 21, 
'HARVEY' : 22, 
'JURIEN' : 42, 
'KALGOORLIE' : 8, 
'KAMBALDA' : 43, 
'KARRATHA' : 9,
'KELLERBERRIN' : 44, 
'KOJONUP' : 45, 
'KUNUNURRA' : 10, 
'MANDURAH' : 18, 
'MANJIMUP' : 32, 
'MECKERING' : 58, 
'MEEKATHARRA' : 46, 
'MOORA' : 47, 
'MT_BARKER' : 48, 
'MURRAY' : 23, 
'NARROGIN' : 11, 
'NEWMAN' : 49, 
'NORSEMAN' : 50, 
'NORTHAM' : 12, 
'PORT_HEDLAND' : 13, 
'RAVENSTHORPE' : 51, 
'REGANS_FORD' : 57, 
'SOUTH_HEDLAND' : 14, 
'TAMMIN' : 53, 
'WAROONA' : 24, 
'WILLIAMS' : 54, 
'WUBIN' : 55, 
'WUNDOWIE' : 59, 
'YORK' : 56} 

# Days

TODAY = 'Today'
TOMORROW = 'Tomorrow'
YESTERDAY = 'Yesterday'

# Fuel Types

UNLEADED_PETROL = 1
PREMIUM_UNLEADED = 2 
DIESEL = 4 
LPG = 5 
RON_98 = 6 
E85 = 10 
BRAND_DIESEL = 11

fuel_types = [UNLEADED_PETROL, PREMIUM_UNLEADED, DIESEL, LPG, RON_98, E85, BRAND_DIESEL]

def fuel_day(which_fuel, which_region, which_day):

    response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}&Day={}'.format(which_fuel, which_region, which_day))
    # print("today", response)
   
    

    feed = feedparser.parse(response.content)
    # print("what is running", feed, which_day, which_fuel,which_day)
    # print(which_fuel, which_day, which_region)
    # pprint(feed, indent=4)

    # Create a list of dictionaries
    fuel_output = []

    for entry in feed["entries"]:
        new_dict = {}
        new_dict["Price"] = entry["price"]
        new_dict["Brand"] = entry["brand"]
        new_dict["Address"] = entry["address"]
        new_dict["Location"] = entry["location"]
        new_dict["Day"] = which_day
        fuel_output.append(new_dict)
   
    return fuel_output

# Sorting by price
def by_price(item):
    return item['Price']

def  fuel_table_data(fuel, location, day):

    fuel_today = fuel_day(fuel, location, day)
    # fuel_tomorrow = fuel_day(PREMIUM_UNLEADED, NORTH_OF_RIVER, TOMORROW)
    all_fuel = fuel_today
    sorted_fuel_output = sorted(all_fuel, key=by_price)
    print(all_fuel)
    return sorted_fuel_output

def create_fuel_table(data):

    fuel_table_header = """
		<tr>
			<th> Price </th><th> Brand </th><th> Address </th><th> Location </th><th> Day </th>
		</th>"""

    fuel_data_row_string = ""

    for value in data:
        fuel_data_row_string += """
            <tr>
                <td>{Price} </td><td>{Brand} </td><td>{Address} </td><td>{Location} </td><td>{Day}</td>
            </tr>
        """.format(**value)
    fuel_html = "<table><tbody>" + fuel_table_header + fuel_data_row_string + "</tbody></table>"

    #print(fuel_html)
    return fuel_html

def render_form():
    location_select = ''
    select_head = '<select name="Location" id="Location">'
    select_box = ''
    select_end = '</select>'
    for v, k in regions.items():
        select_box += '<option value="{}">{}</option>'.format(k, v)
            
    location_select = select_head + select_box + select_end

    form_labels = '''
        
        <label>Day: </label>
        <select name="Day" id="day">
        <option value="Today">Today</option>
        <option value="Tomorrow">Tomorrow</option>
        <option value="Yesterday">Yesterday</option>
        </select>
        <br>
        <label>Fuel Type: </label>
        <select name="Fuel Type" id="fuel type">
        <option value="1">Unleaded Petrol</option>
        <option value="2">Premium Unleaded</option>
        <option value="4">Diesel</option>
        <option value="5">LPG</option>
        <option value="6">RON 98</option>
        <option value="10">E85</option>
        <option value="11">Diesel Brand</option>

        </select>

        '''

    submit_button = '<br><input type="submit" value="Submit">'

    rendered_form = '<form>' + 'Location: ' + location_select + '<br>'+ form_labels + submit_button + '</form>'

    return rendered_form


    # location select

    # return form_labels + 
    
# Test print of fuel dictionaries
# print(1, fuel_today, TODAY)
# print(fuel_tomorrow)

# remove /table></body></html render form in one function and table data in another



# def fuel_string_names():
#     if"""



# Printing output of sorted_fuel_output
# pprint(sorted_fuel_output, indent =4)






# fuel_output_table = fuel_table_data()

# data_for_fuel_table = fuel_table_data()
# fuel_data = fuel_table_data(PREMIUM_UNLEADED, NORTH_OF_RIVER, TODAY)
# print("fuel_data", fuel_data)
# print(render_form())
# list_fuel = create_fuel_table(fuel_data)

# print(list_fuel)


# print(os.getcwd())

# print(list_fuel)

# Printing output of fuel_data_row_string
# print(fuel_data_row_string)

# Formats the html data

# Printing output of fuel_html
# print(fuel_html)

# Create HTML file
# Opens and creates a file named fuel_report.html with write access.
#fuel_file = open('fuel_report.html', 'w')

# Writes the the data from fuel_data_html into the fuel_report.html file.
#fuel_file.write(list_fuel)

# Closes fuel_report.html.
# fuel_file.close()

# print("Run succesfully!")
# Get all regions as variables so they can be used by the function def fuel_day(which_day, which_fuel) Add the Region, Fuel type (needs to be added to function to be used) and day. Use a settings.py file (CONSTANCE?)

# Use Itertools to get all combinations of URLs

# Read up on list comprehension

# Read up on Python Context Manager
