import json
import datetime
from pprint import pprint 
import os
from jinja2 import Template

# Get number of current week in the year
week_number = datetime.datetime.now().isocalendar()[1]

# Load results.json
with open('data/results.json', 'r') as f:
    results = json.load(f)
    # Copy the file to history/{week_number}/results.json
    directory = f'history/{week_number}'
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f'{directory}/results.json', 'w') as h:
        json.dump(results, h, indent=4)
    
    # Save current datetime to history/{week_number}/access.txt
    with open(f'{directory}/access.txt', 'w') as h:
        h.write(str(datetime.datetime.now()))

results = results['data']
results_json = json.dumps(results, indent=4)
"""
Results is a list of dictionaries. Each dictionary contains the following
{'athlete_firstname': 'Michał',
           'athlete_id': 107086618,
           'athlete_lastname': 'K.',
           'athlete_member_type': None,
           'athlete_picture_url': '/assets/avatar/athlete/medium.png',
           'distance': 0.0,
           'elev_gain': 0.0,
           'moving_time': 17226,
           'num_activities': 3,
           'rank': 1}
"""

# Define the scoreboard template from template.html
with open('template.html', 'r') as f:
    template = Template(f.read())

# Render the template with the results data
html = template.render(results=results, results_json=results_json)

# Save the rendered HTML to results.html
with open('data/results.html', 'w') as f:
    f.write(html)


print(week_number)