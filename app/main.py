import utils_1
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Type Country => ')
  print(country)
  name = country
  print(country)
  result = utils_1.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils_1.get_population(country)
    charts.generate_bar_chart(name, labels, values)
    print(country)
   
  
 # data =[
 #  {
 #     'Country': 'Colombia',
  #    'Population': 300
   # },
    #{
     # 'Country': 'Bolivia',
      #'Population': 500
    #}
  #]
  #country = input('Type Country => ')
  #result = utils.population_by_country(data, country)
  #print(result)

if __name__ == '__main__':
  run()
  