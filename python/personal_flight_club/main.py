# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


























# header = {
#     'Authorization': os.environ['Authorization']
# }
# apikey = os.environ['api_key']
#
# data_manager = DataManager()
# sheet_data = data_manager.get_data()
#
# if sheet_data[0]['iataCode'] == '':
#     fs = FlightSearch()
#     for row in sheet_data:
#         row['iataCode'] = fs.get_iata_code(row['city'])
#     data_manager.destination_data = sheet_data
#     data_manager.update_iata()
#
