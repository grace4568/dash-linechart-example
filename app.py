import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "GDP Growth in 2000s"
mytitle = "GDP Trends for the 3 Major Countries <USA, China, Germany>"
x_values = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']
y1_values = [8.492, 8.34, 9.131, 10.036, 10.111, 11.396, 12.719, 9.654, 9.4, 10.636]
y2_values = [4.127, 0.998, 1.742, 2.861, 3.799, 3.513, 3.7, 3.261, 1.082, -2.537, 2.564]
y3_values = [2.962, 1.695, 0, -0.71, 1.17 , 0.707, 3.7, 3.261, 1.082, -5.619, 4.08]
color1 = '#9B59B6  '
color2 = '#1ABC9C  '
color3 = '#D35400  '
name1 = 'China'
name2 = 'USA'
name3 = 'Germany'
tabtitle = 'GDP'
sourceurl = 'https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?end=2010&locations=CN-US-DE&start=2000'
githublink = 'https://github.com/grace456/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
