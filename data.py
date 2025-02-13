import requests
import json
import pandas as pd
from datetime import datetime
import pytz

pd.set_option('display.max_rows', 500)

    # Define the API endpoint for prop trends
    url = "https://api.props.cash/nba/prop-trends"

    # Add your API key to the request headers
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjF0dUkybDZSQjBjWlF2MHM1M28yNSJ9.eyJzdWJzY3JpcHRpb24iOiJwcm8iLCJpc3MiOiJodHRwczovL3Byb3BzLWhlbHBlci51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQxMTE5MDQxMjk1NzYyNDk5MjUiLCJhdWQiOlsiaHR0cHM6Ly9wcm9wcy1kb3QtY2FzaC9hcGkiLCJodHRwczovL3Byb3BzLWhlbHBlci51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzM4NTQwMDE2LCJleHAiOjE3NDExMzIwMTYsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJrSTc2UFlrOUEzZzd5VXR5aFkzQWhLbXI5b3ZpSEF6dyJ9.KuzTtQeFfiMFNdRLM9f-8d4bWFNJcH2k7eITn07gqwCNfM6n8wKLh0eqenIDZY9eZaTk4aZhwki-E_aQMR7VnnoLDoQcVo06il8p7SKUM6CTlevFQItVRbMgu_aUUOSN7TBKHZG2gM0jW7IPY2FKYLqqRptKrxS8dj8tXRJn6NI7LfIkjGXtdmIjAJ0bu2T-ng8VqOH5CpF8OLHaifOXwXMJs8zBTtQ5czzADsLwuONhBeaMIL7fjj304EN3BUFXeNty-efAFhr3d7EU4001zea1xzyZ4LRWO5wgIMRIN8_SOq3OdrOkkAZ06rVWs_KWsODB0Yl1nzG4I7FG-4vnUw'
    }

    # Define the API endpoint for the schedule
    schedule_url = "https://api.props.cash/nba/schedule"

    # Projections URL

    projections_url = "https://api.props.cash/nba/projections"

    # Make a GET request to the API with the headers to fetch player prop trends
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

    # Initialize an empty list to store player data for the DataFrame
    data_rows = []

    # Initialize the EST timezone
    est = pytz.timezone('US/Eastern')

    # Loop through the player data to extract player information for the DataFrame
    for player in data:
        name = player.get('name')
        team = player.get('team')
        player_id = player.get('id')  # Get the player ID
        points = player.get('points', {})
        rebounds = player.get('rebounds', {})
        assists = player.get('assists', {})

        row = {
            'id': player_id,  # Add the player ID to the row
            'name': name,
            'team': team,
            'points_line': points.get('line'),
            'points_l20Rate': points.get('l20Rate'),
            'points_l10Rate': points.get('l10Rate'),
            'points_l5Rate': points.get('l5Rate'),
            'points_vsOpp': points.get('vsOpp'),
            'points_vsOppGames': points.get('vsOppGames'),
            'reb_line': rebounds.get('line'),
            'reb_l20Rate': rebounds.get('l20Rate'),
            'reb_l10Rate': rebounds.get('l10Rate'),
            'reb_l5Rate': rebounds.get('l5Rate'),
            'reb_vsOpp': rebounds.get('vsOpp'),
            'reb_vsOppGames': rebounds.get('vsOppGames'),
            'ast_line': assists.get('line'),
            'ast_l20Rate': assists.get('l20Rate'),
            'ast_l10Rate': assists.get('l10Rate'),
            'ast_l5Rate': assists.get('l5Rate'),
            'ast_vsOpp': assists.get('vsOpp'),
            'ast_vsOppGames': assists.get('vsOppGames')
        }

        # Add player URL
        row['player_url'] = f"https://api.props.cash/nba/player-feed?playerId={player_id}&int=0"
        data_rows.append(row)

    # Create the DataFrame for player statistics
    points_df = pd.DataFrame(data_rows)

    # Make a GET request to the API with the headers to fetch the schedule
    schedule_response = requests.get(schedule_url, headers=headers)

    # Check if the request was successful (status code 200)
    if schedule_response.status_code == 200:
        # Parse the JSON data from the response
        schedule_data = schedule_response.json()

    site_data = []  

    # Loop through the rows of points_df
    for index, row in points_df.iterrows():
        player_team = row['team']
        site = 'unknown'  # Default value for site
        
        # Loop through each game in the schedule to determine if the player is home or away
        for game in schedule_data:
            if game['home'] == player_team:
                site = 'home'  # Player is playing at home
                break
            elif game['away'] == player_team:
                site = 'away'  # Player is playing away
                break
        
        site_data.append(site)

    # Add the new 'site' column to points_df
    points_df['site'] = site_data

    # Get Projecion Data

    # Make a GET request to the API with the headers to fetch the projections data
    projections_response = requests.get(projections_url, headers=headers)

    # Check if the request was successful (status code 200)
    if projections_response.status_code == 200:
        # Parse the JSON data from the response
        projections_data = projections_response.json()

    # Initialize an empty list to store the projections data
    projections_list = []

    # Loop through each player in points_df and match them to the projections data
    for index, row in points_df.iterrows():
        player_name = row['name']  # Get player's name
        player_team = row['team']  # Get player's team abbreviation
        
        # Search for matching player in projections_data
        player_found = False
        for player in projections_data:
            if player['name'] == player_name and player['team'] == player_team:
                points_projection = player['projections'].get('points')
                rebounds_projection = player['projections'].get('rebounds')
                assists_projection = player['projections'].get('assists')
                
                projections_list.append({
                    'name': player_name,
                    'points_projection': points_projection,
                    'rebounds_projection': rebounds_projection,
                    'assists_projection': assists_projection
                })
                player_found = True
                break  # Stop the loop once the player is found

        # If player is not found, append None values
        if not player_found:
            projections_list.append({
                'name': player_name,
                'points_projection': None,
                'rebounds_projection': None,
                'assists_projection': None
            })

    # Convert the projections data into a DataFrame
    projections_df = pd.DataFrame(projections_list)

    # Merge the projections data into the original points_df
    points_df = pd.merge(points_df, projections_df, on='name', how='left')

    # Fetch each player's stats by going through each player URL in the DataFrame
    player_feed_data = []

    # Loop through each player in points_df and fetch their data from the player URL
    for index, row in points_df.iterrows():
        player_url = row['player_url']
        
        # Make a GET request to the player URL
        print(f"Fetching data for player: {row['name']}")
        player_response = requests.get(player_url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if player_response.status_code == 200:
            # Parse the JSON data for the player
            player_data = player_response.json()
            
            # Extract gamelogs and loop through them to extract 'startTime', 'pts', 'reb', and 'ast'
            gamelogs = player_data.get('gamelogs', [])
            if not gamelogs:
                print(f"No gamelogs found for player: {row['name']}")
            
            for game in gamelogs:
                start_time = game.get('game', {}).get('startTime')
                points = float(game.get('stats', {}).get('offense', {}).get('pts', 0))
                rebounds = float(game.get('stats', {}).get('rebounds', {}).get('reb', 0))
                assists = float(game.get('stats', {}).get('offense', {}).get('ast', 0))
                points_line = float(game.get('lines', {}).get('points',{}).get('line', 0))
                reb_line = float(game.get('lines', {}).get('rebounds',{}).get('line', 0))
                ast_line = float(game.get('lines', {}).get('assists',{}).get('line', 0))
                
                # Deduce the NBA season year from start time
                if start_time:
                    start_datetime = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
                    start_datetime = pytz.utc.localize(start_datetime)  # Localize to UTC timezone
                    start_datetime_est = start_datetime.astimezone(est)  # Convert to EST
                    season_year = start_datetime_est.year if start_datetime_est.month < 10 else start_datetime_est.year + 1
                    start_time_est = start_datetime_est.strftime('%Y-%m-%dT%H:%M:%S')  # Format the time in EST
                else:
                    season_year = None
                    start_time_est = None

                # Determine if the player was home or away based on the team abbreviation
                team_abbreviation = game.get('team', {}).get('abbreviation')
                if team_abbreviation == game.get('game', {}).get('awayTeamAbbreviation'):
                    site = 'away'
                elif team_abbreviation == game.get('game', {}).get('homeTeamAbbreviation'):
                    site = 'home'
                else:
                    site = 'unknown'

                # Append the data to the list
                player_feed_data.append({
                    'name': row['name'],
                    'id': row['id'],
                    'start_time': start_time_est,
                    'site': site,
                    'season': season_year,
                    'points': points,
                    'rebounds': rebounds,
                    'assists': assists,
                    'points_line': points_line,
                    'reb_line': reb_line,
                    'ast_line': ast_line, 
                    'points_diff': points - points_line,
                    'reb_diff': rebounds - reb_line,
                    'ast_diff': assists - ast_line
                })
        else:
            print(f"Failed to fetch data for player {row['name']}")
            player_feed_data.append({
                'name': row['name'],
                'id': row['id'],
                'start_time': 'Request failed',
                'pts': 'Request failed',
                'rebounds': 'Request failed',
                'assists': 'Request failed',
                'season': 'Request failed',
                'site': 'Request failed'
            })

    # Create a new DataFrame with the game data
    game_data_df = pd.DataFrame(player_feed_data)

    # Display the final DataFrame with game details

    game_data_df.to_csv('game_feed.csv')
    points_df.to_csv('trendsnlines.csv')

    print(game_data_df)
    print(points_df)
