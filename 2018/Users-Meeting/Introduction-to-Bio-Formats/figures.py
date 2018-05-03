import matplotlib.pyplot as plot
import pandas

# load from the csv

df = pandas.read_csv('stats.csv')

# classic users/formats/contribs chart
plot.rc('axes', facecolor='whitesmoke')
plot.rc('lines', linewidth=3, color='silver')
plot.rc('savefig', facecolor='whitesmoke')
plot.grid()

# contribs
plot.plot('Year', 'Contributors', data=df, marker='o', markersize=10, color='royalblue')

# users
plot.plot('Year', 'Users (thousands)', data=df, marker='o', markersize=10, color='gold')

# formats
plot.plot('Year', 'Formats', data=df, marker='o', markersize=10, color='crimson')

plot.figlegend(loc='lower center')
plot.savefig('stats.png')

# TODO:
# - classic chart:
#   * rotate X labels 90 degrees
#   * make plots continuous
#   * fill in remainder of .csv
#   * use different markers for each plot (in case colors aren't distinguishable)
#   * make legend horizontal instead of vertical
