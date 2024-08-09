# Use an API call to get info about the most-starred Python projects on GitHub & visualise the results
import requests
import plotly.express as px

# Make an API call  - assign the API call url to "url" variable
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000" # query string

# Specify the API version to be used and what format the results should be returned in
headers = {"Accept": "application/vnd.github.v3+json"}
# User requests to make the call to the API
r = requests.get(url, headers=headers)
# Print info whether the call was successful - 200 means response was successful
print(f"Status code: {r.status_code}")

# Process the overall results
# Convert the reponse object to a Python dictionary
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repo info
repo_dicts = response_dict['items']
# create lists for the data in the bar chart - project name for each bar & stars for the bar height
repo_names, stars, hover_texts = [], [], [] 
# Loop through the repo dict and append project names and number of stars
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Build hover text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Visualise the data - create a bar chart
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

# Customise the chart
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

# Change the bars' colour to a darker blue with transparency
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()