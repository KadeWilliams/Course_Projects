class DataManager:
    pass

























    # # This class is responsible for talking to the Google Sheet.
    # def __init__(self):
    #     self.destination_data = {}
    #
    # def get_data(self):
    #     self.header = {
    #         'Authorization': os.environ['Authorization']
    #     }
    #     response = requests.get(endpoint, headers=self.header)
    #     data = response.json()
    #     self.destination_data = data['prices']
    #     return self.destination_data
    #
    # def update_iata(self):
    #     for city in self.destination_data:
    #         body = {
    #             'price': {
    #                 'iataCode': city['iataCode']
    #             }
    #         }
    #         response = requests.put(f"{endpoint}/{city['id']}", json=body, headers=self.header)
