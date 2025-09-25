import dash
from dash import html, dcc

# Create a dash application
app = dash.Dash(__name__)

# define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1('My Dashboard'),
    dcc.Graph(
        id='My-Graph',
        figure={
            'data':[
                {'x':[1,2,3,4], 'y':[4,1,2,8], 'type': 'bar', 'name':'Bar chart'},
                {'x':[1,2,3,4], 'y':[2,4,5,8], 'type': 'line', 'name':'Line chart'}
            ],
            'layout': {
                'title':'Dash Data Visualization'
            }
        }
    )
]) 

# run the application
if __name__ == '__main__':
    app.run(debug=True)


# Navigation:
# Open Terminal
# Navigate to project folder via Terminal Commands
#   DIR: 
#   cd: Change directory
#   ls: list
#   pwd: Print Working Directory
#   mkdir: Make New Directory
#   rmdir: Remove empty directory
#   rm: remove non empty directory must be ran with -r and -f flags
#   mv: move directory orignal folder + ~ + destination folder
#   cp: copy directory original directory + ~ + destination folder
#   cat: concatenate - reads data from a specified file and prints the output
#   less: prints file logs
#   find: finds files or file types
# Run File
# copy socket address socket address = IP Address + Port Number