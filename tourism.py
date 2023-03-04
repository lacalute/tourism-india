# import neccessary libraries
import csv
import matplotlib.pyplot as plt
import numpy as np

# open the csv file
with open('tourism.csv') as f:
    reader = csv.reader(f)
    x = list(reader)
    # create a variable with titles
    titles = x[0]
    # delete titles
    x.pop(0)

# collect the data as:
# [{'state': *name_of_state, 'data': *data}]
a = 0
q = []
states = []
while a < len(x):
    # collect list of states
    if x[a][0] not in states:
        states.append(x[a][0])
    # collect Total data of all states and turn it in list "q"
    if x[a][0] == "Total":
        q.append(dict({'state': x[a-1][0], 'data': x[a]}))
        a = a + 1
    else:
        a = a + 1
# remove Total from the list of states
states.remove('Total')

# the main func, which collect data and after visualize them
def collect_data(cn):
    # arrays with data
    # indian - list with number of indian tourists
    # foreign - list with number of foreign tourists
    indian = []
    foreign = []
    # the loop, which collect data
    for collect in q:
        if collect['state'] == cn:
            indian.append(int(collect['data'][2]))
            indian.append(int(collect['data'][4]))
            foreign.append(int(collect['data'][3]))
            foreign.append(int(collect['data'][5]))   

    # the func, which make the plot with data
    def plot():
        year = ['2020', '2021']
        x = np.arange(0, len(year))
        plt.style.use('ggplot')
        plt.title(cn)
        plt.suptitle('Number of tourists')
        plt.bar(x+0.00,indian, width=0.25, label='Indian')
        plt.bar(x+0.25,foreign,  width=0.25, label='Foreign')
        plt.xticks(x+0.125, year)
        plt.legend()
        plt.show()
    plot()

# the while loop, which start program
status = True
print(states)
while status:
    try:
        ask_state = str(input('Type the state -> '))
        if ask_state in states:
            collect_data(ask_state)
            status = False
        else:
            print('That state is not in list of states. Type another state')
    except ValueError:
        print('Error, type again')
    
# The program by Lacalute !!!