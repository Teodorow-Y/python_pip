def get_population():
  keys = ['Col', 'Bol']
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result 
