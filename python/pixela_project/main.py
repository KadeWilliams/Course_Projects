import requests
from secrets import user_params, headers
import datetime

# to see the graph go here: https://pixe.la/v1/users/kaetha/graphs/graph1.html
#                           https://pixe.la/v1/users/kaetha/graphs/codinggraph.html

# today = datetime(year=2021, month=3, day=21)
today = datetime.datetime.now()

USERNAME = user_params['username']
TOKEN = user_params['token']
ID = 'graph1'
ID2 = 'codinggraph'
DATE = today.strftime("%Y%m%d")

pixela_endpoint = 'https://pixe.la/v1/users'
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# CREATE THE GRAPH
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# graph_config = {
#     'id': 'graph1',
#     'name':'Reading Graph',
#     'unit':'pages',
#     'type':'int',
#     'color':'kuro'
# }

# graph_config = {
#     'id': 'codinggraph',
#     'name': 'Coding Graph',
#     'unit': 'hours',
#     'type': 'float',
#     'color': 'shibafu'
# }

# CREATE NEW GRAPH

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# CREATE NEW VALUE IN THE GRAPH
# value_endpoint = f'{graph_endpoint}/{ID}'
#
# value_config = {
#     'date': DATE,
#     'quantity': input('How many pages did you read today? '),
# }
value_config = {
    'date': DATE,
    'quantity': input('How many hours did you study today? '),
}
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID2}"
response = requests.post(value_endpoint, json=value_config, headers=headers)
print(response.text)


# dates = []
# date = datetime.datetime(2021, 4, 23)
# for i in range(5):
#     date += datetime.timedelta(days=1)
#     dates.append(date)
#     # date = date.replace('00:00:00', '')
# date = [str(date).replace(' 00:00:00', '') for date in dates]
# date = [date.replace('-', '') for date in date]
#
# for val in date:
#     DATE = val
#     value_config = {
#         'date': DATE,
#         'quantity': '3',
#     }
#
#     value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID2}"
#     response = requests.post(value_endpoint, json=value_config, headers=headers)


# UPDATE THE GRAPH
# update_endpoint = f"{graph_endpoint}/{ID}/{DATE}"

# update_config = {
#     'quantity': '50'
# }
#
# response = requests.put(update_endpoint, json=update_config, headers=headers)
# print(response.text)

# DELETE A PIXEL
# delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}'
#
# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)
