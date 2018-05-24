import matplotlib.pyplot as plot
import pandas

# load from the csv

df = pandas.read_csv('stats.csv')

# classic users/formats/contribs chart
bgcolor = 'whitesmoke'
linecolor = 'silver'
plot.rc('axes', facecolor=bgcolor)
plot.rc('lines', linewidth=3, color=linecolor, markersize=10)
plot.rc('savefig', facecolor=bgcolor)
plot.grid()
plot.tick_params('x', labelrotation=90)
plot.tick_params('both', color=linecolor, labelcolor='#202020')

# contribs
plot.plot('Year', 'Contributors', data=df, marker='o', color='royalblue')

# users
plot.plot('Year', 'Users (thousands)', data=df, marker='D', color='gold')

# formats
plot.plot('Year', 'Formats', data=df, marker='*', color='crimson')

plot.figlegend(loc='upper center', ncol=3)
plot.savefig('images/stats.png')

# TODO:
# - classic chart:
#   * make plots continuous
