import matplotlib.pyplot as plot
import numpy as np
import pandas

def setup_plot(xaxis):
    bgcolor = 'whitesmoke'
    linecolor = 'silver'
    plot.rc('axes', facecolor=bgcolor)
    plot.rc('lines', linewidth=3, color=linecolor, markersize=10)
    plot.rc('savefig', facecolor=bgcolor)
    plot.grid()
    plot.tick_params('x', labelrotation=90)
    plot.tick_params('both', color=linecolor, labelcolor='#202020')
    # make sure every year is shown on the X axis
    plot.xticks(np.arange(min(xaxis), max(xaxis)+1, 1.0))


# load from the csv

df = pandas.read_csv('stats.csv', comment='#')
df = df.interpolate(limit_area='inside', limit_direction='backward')

# classic users/formats/contribs chart

setup_plot(df['Year'])

# contribs
plot.plot('Year', 'Contributors', data=df, marker='o', color='royalblue')

# users - expected to be sparse
plot.plot('Year', 'Users (thousands)', data=df, marker='D', color='gold')

# formats
plot.plot('Year', 'Formats', data=df, marker='*', color='crimson')

plot.figlegend(loc='upper center', ncol=3)
plot.savefig('images/stats.png')

# reset figure and generate releases over time

plot.close()
setup_plot(df['Year'])
plot.plot('Year', 'Releases', data=df, marker='o', color='crimson')
plot.figlegend(loc='upper center')
plot.savefig('images/releases.png')
