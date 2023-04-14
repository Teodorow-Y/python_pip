import csv 
import matplotlib.pyplot as plt
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    count = 0
    for row in reader: 
      iterable = zip(header, row)
      country_dict = { key: value for key, value in iterable}
      count += 1
      if count == 228:
        data.append(country_dict)
    return data
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  
values = data[0] 
value2 = values['1970 Population'],values['1980 Population'],values['1990 Population'],values['2000 Population'],values['2010 Population'],values['2015 Population'],values['2020 Population'],values['2022 Population']
#print(value2)


new_labels = data[0]
labels = list(new_labels.keys())

labels_p = [labels[12],labels[11], labels[10],labels[9], labels[8], labels[7], labels[6], labels[5]]
print(labels_p)
print(value2)

def generate_bar_chart(labels_p, value2):
 
  fig, ax = plt.subplots()
  ax.bar(labels_p, value2)
  plt.show()

if __name__ == '__main__':
  generate_bar_chart(labels_p, value2)