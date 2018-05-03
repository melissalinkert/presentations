import matplotlib.pyplot as plot
import pandas

# load from the csv

df = pandas.read_csv('stats.csv')

# classic users/formats/contribs chart
plot.rc('axes', facecolor='whitesmoke')
plot.rc('lines', linewidth=3, color='silver', markersize=10)
plot.rc('savefig', facecolor='whitesmoke')
plot.grid()
plot.tick_params('x', labelrotation=90)
plot.tick_params('both', color='silver', labelcolor='#202020')

# contribs
plot.plot('Year', 'Contributors', data=df, marker='o', color='royalblue')

# users
plot.plot('Year', 'Users (thousands)', data=df, marker='o', color='gold')

# formats
plot.plot('Year', 'Formats', data=df, marker='o', color='crimson')

plot.figlegend(loc='upper center', ncol=3)
plot.savefig('stats.png')

# TODO:
# - classic chart:
#   * make plots continuous
#   * fill in remainder of .csv
#   * use different markers for each plot (in case colors aren't distinguishable)
