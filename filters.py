import pandas as pd

game_feed = pd.read_csv('game_feed.csv')
trends = pd.read_csv('trendsnlines.csv')

# Initialize the DataFrame with the specified columns
filtered_df = pd.DataFrame(columns=['player', 'o/u', 'stat', 'line', 'projection'])

# FILTER 1 - PLAYER HAS HIT LINE IN 55% OF THEIR LAST 20 GAMES

# Loop through the trends DataFrame
for index, row in trends.iterrows():
    name = row['name']
    points_hit_percentage = row['points_l20Rate']  # Percentage for hitting points line
    rebounds_hit_percentage = row['reb_l20Rate']  # Percentage for hitting rebounds line
    assists_hit_percentage = row['ast_l20Rate']   # Percentage for hitting assists line
    
    # Check if any of the hit percentages for points, rebounds, or assists is >= 55% or <= 45%
    if points_hit_percentage >= 55 or rebounds_hit_percentage >= 55 or assists_hit_percentage >= 55 or \
    points_hit_percentage <= 45 or rebounds_hit_percentage <= 45 or assists_hit_percentage <= 45:
        
        # Determine the stat that met the condition (points, rebounds, or assists)
        if points_hit_percentage >= 55:
            stat = 'points'
            line = row['points_line']
            projection = row['points_projection']
            o_u = 'over'
        elif rebounds_hit_percentage >= 55:
            stat = 'rebounds'
            line = row['reb_line']
            projection = row['rebounds_projection']
            o_u = 'over'
        elif assists_hit_percentage >= 55:
            stat = 'assists'
            line = row['ast_line']
            projection = row['assists_projection']
            o_u = 'over'
        elif points_hit_percentage <= 45:
            stat = 'points'
            line = row['points_line']
            projection = row['points_projection']
            o_u = 'under'
        elif rebounds_hit_percentage <= 45:
            stat = 'rebounds'
            line = row['reb_line']
            projection = row['rebounds_projection']
            o_u = 'under'
        elif assists_hit_percentage <= 45:
            stat = 'assists'
            line = row['ast_line']
            projection = row['assists_projection']
            o_u = 'under'
        
        # Create a new DataFrame for the current player data
        new_row = pd.DataFrame({
            'player': [name],
            'o/u': [o_u],  # This will be either 'over' or 'under'
            'stat': [stat],
            'line': [line],
            'projection': [projection]
        })
        
        # Concatenate the new row to filtered_df
        filtered_df = pd.concat([filtered_df, new_row], ignore_index=True)

# FILTER 2 - PLAYER HAS HIT LINE 60% L10

# Loop through the trends DataFrame
for index, row in trends.iterrows():
    name = row['name']
    points_hit_percentage_l10 = row['points_l10Rate']  # Percentage for hitting points line in last 10 games
    rebounds_hit_percentage_l10 = row['reb_l10Rate']  # Percentage for hitting rebounds line in last 10 games
    assists_hit_percentage_l10 = row['ast_l10Rate']   # Percentage for hitting assists line in last 10 games
    
    # Check if any of the hit percentages for points, rebounds, or assists is >= 60% or <= 40% in the last 10 games
    if points_hit_percentage_l10 >= 60 or rebounds_hit_percentage_l10 >= 60 or assists_hit_percentage_l10 >= 60 or \
    points_hit_percentage_l10 <= 40 or rebounds_hit_percentage_l10 <= 40 or assists_hit_percentage_l10 <= 40:
        
        # Determine the stat that met the condition (points, rebounds, or assists)
        if points_hit_percentage_l10 >= 60:
            stat = 'points'
            line = row['points_line']
            projection = row['points_projection']
            o_u = 'over'
        elif rebounds_hit_percentage_l10 >= 60:
            stat = 'rebounds'
            line = row['reb_line']
            projection = row['rebounds_projection']
            o_u = 'over'
        elif assists_hit_percentage_l10 >= 60:
            stat = 'assists'
            line = row['ast_line']
            projection = row['assists_projection']
            o_u = 'over'
        elif points_hit_percentage_l10 <= 40:
            stat = 'points'
            line = row['points_line']
            projection = row['points_projection']
            o_u = 'under'
        elif rebounds_hit_percentage_l10 <= 40:
            stat = 'rebounds'
            line = row['reb_line']
            projection = row['rebounds_projection']
            o_u = 'under'
        elif assists_hit_percentage_l10 <= 40:
            stat = 'assists'
            line = row['ast_line']
            projection = row['assists_projection']
            o_u = 'under'
        
        # Create a new DataFrame for the current player data
        new_row = pd.DataFrame({
            'player': [name],
            'o/u': [o_u],  # This will be either 'over' or 'under'
            'stat': [stat],
            'line': [line],
            'projection': [projection]
        })
        
        # Concatenate the new row to filtered_df
        filtered_df = pd.concat([filtered_df, new_row], ignore_index=True)

# FILTER 3 - PLAYER HAS HIT LINE 60% L5

# Loop through the trends DataFrame
for index, row in trends.iterrows():
    name = row['name']
    points_hit_percentage_l5 = row['points_l5Rate']  # Percentage for hitting points line in last 5 games
    rebounds_hit_percentage_l5 = row['reb_l5Rate']  # Percentage for hitting rebounds line in last 5 games
    assists_hit_percentage_l5 = row['ast_l5Rate']   # Percentage for hitting assists line in last 5 games
    
    # Check if any of the hit percentages for points, rebounds, or assists is >= 60% or <= 40% in the last 5 games
    if points_hit_percentage_l5 >= 60 or rebounds_hit_percentage_l5 >= 60 or assists_hit_percentage_l5 >= 60 or \
    points_hit_percentage_l5 <= 40 or rebounds_hit_percentage_l5 <= 40 or assists_hit_percentage_l5 <= 40:
        
        # Determine the stat that met the condition (points, rebounds, or assists)
        if points_hit_percentage_l5 >= 60:
            stat = 'points'
            line = row['points_line']
            projection = row['points_projection']
            o_u = 'over'
        elif rebounds_hit_percentage_l5 >= 60:
            stat = 'rebounds'
            line = row['reb_line']
            projection = row['rebounds_projection']
            o_u = 'over'
        elif assists_hit_percentage_l5 >= 60:
            stat = 'assists'
            line = row['ast_line']
            projection = row['assists_projection']
            o_u = 'over'
        elif points_hit_percentage_l5 <= 40:
            stat = 'points'
            line = row['points_line']
            projection = row['points_projection']
            o_u = 'under'
        elif rebounds_hit_percentage_l5 <= 40:
            stat = 'rebounds'
            line = row['reb_line']
            projection = row['rebounds_projection']
            o_u = 'under'
        elif assists_hit_percentage_l5 <= 40:
            stat = 'assists'
            line = row['ast_line']
            projection = row['assists_projection']
            o_u = 'under'
        
        # Create a new DataFrame for the current player data
        new_row = pd.DataFrame({
            'player': [name],
            'o/u': [o_u],  # This will be either 'over' or 'under'
            'stat': [stat],
            'line': [line],
            'projection': [projection]
        })
        
        # Concatenate the new row to filtered_df
        filtered_df = pd.concat([filtered_df, new_row], ignore_index=True)

# Filter 4 - H2H Has Hit 50% Overall

# Loop through the trends DataFrame for head-to-head matchups
for index, row in trends.iterrows():
    name = row['name']
    points_h2h_rate = row.get('points_vsOpp', None)  # Points H2H percentage
    rebounds_h2h_rate = row.get('reb_vsOpp', None)  # Rebounds H2H percentage
    assists_h2h_rate = row.get('ast_vsOpp', None)   # Assists H2H percentage

    # Check if any stat's H2H hit percentage is >= 50%
    if points_h2h_rate is not None and points_h2h_rate >= 50:
        stat = 'points'
        line = row['points_line']
        projection = row['points_projection']
        o_u = 'over' if points_h2h_rate >= 50 else 'under'
        new_row = pd.DataFrame({
            'player': [name],
            'o/u': [o_u],
            'stat': [stat],
            'line': [line],
            'projection': [projection]
        })
        filtered_df = pd.concat([filtered_df, new_row], ignore_index=True)

    if rebounds_h2h_rate is not None and rebounds_h2h_rate >= 50:
        stat = 'rebounds'
        line = row['reb_line']
        projection = row['rebounds_projection']
        o_u = 'over' if rebounds_h2h_rate >= 50 else 'under'
        new_row = pd.DataFrame({
            'player': [name],
            'o/u': [o_u],
            'stat': [stat],
            'line': [line],
            'projection': [projection]
        })
        filtered_df = pd.concat([filtered_df, new_row], ignore_index=True)

    if assists_h2h_rate is not None and assists_h2h_rate >= 50:
        stat = 'assists'
        line = row['ast_line']
        projection = row['assists_projection']
        o_u = 'over' if assists_h2h_rate >= 50 else 'under'
        new_row = pd.DataFrame({
            'player': [name],
            'o/u': [o_u],
            'stat': [stat],
            'line': [line],
            'projection': [projection]
        })
        filtered_df = pd.concat([filtered_df, new_row], ignore_index=True)

# FILTER 5 - PLAYER HAS HIT LINE 65% OF GAMES AT SITE THIS SEASON

# Loop through the trends_df to process players and their site
for index, row in trends.iterrows():
    player_name = row['name']
    player_team = row['team']
    site = row['site']  # 'home' or 'away' from trends_df

    # Get projections

    points_proj = trends['points_projection']
    reb_proj = trends['rebounds_projection']
    ast_proj = trends['assists_projection']

    # Retrieve the lines for the player's stats
    points_line = row['points_line']
    rebounds_line = row['reb_line']
    assists_line = row['ast_line']

    # Filter the game_feed_df based on the player's team, site (home/away), and season
    filtered_by_site = game_feed[game_feed['site'] == site]
    filtered_by_season = filtered_by_site[filtered_by_site['season'] == 2025]
    player_games = filtered_by_season[filtered_by_season['name'] == player_name]

    # Filter out games where the points_line is 0
    player_games = player_games[player_games['points_line'] != 0]

    # Skip player if no games remain after filtering
    if len(player_games) == 0:
        continue

    # Initialize hit and under rates for the stats
    hit_rate = {'points': 0, 'rebounds': 0, 'assists': 0}
    under_rate = {'points': 0, 'rebounds': 0, 'assists': 0}

    # Loop through the player's games to calculate overs and unders for each stat
    for i, game in player_games.iterrows():
        # Compare points scored (game['points']) with points line
        points_scored = game.get('points', 0)
        points_diff = points_scored - points_line  # Difference between points scored and points line

        # Compare rebounds and assists with their respective lines
        reb_diff = game.get('rebounds', 0) - rebounds_line
        ast_diff = game.get('assists', 0) - assists_line

        # Count overs and unders for points
        if points_diff > 0:
            hit_rate['points'] += 1
        if points_diff < 0:
            under_rate['points'] += 1

        # Count overs and unders for rebounds
        if reb_diff > 0:
            hit_rate['rebounds'] += 1
        if reb_diff < 0:
            under_rate['rebounds'] += 1

        # Count overs and unders for assists
        if ast_diff > 0:
            hit_rate['assists'] += 1
        if ast_diff < 0:
            under_rate['assists'] += 1

    # Calculate hit rates for points, rebounds, assists (overs and unders)
    total_games = len(player_games)
    points_hit_rate = hit_rate['points'] / total_games
    reb_hit_rate = hit_rate['rebounds'] / total_games
    ast_hit_rate = hit_rate['assists'] / total_games

    points_under_rate = under_rate['points'] / total_games
    reb_under_rate = under_rate['rebounds'] / total_games
    ast_under_rate = under_rate['assists'] / total_games

    # Initialize the over/under values
    points_o_u = None
    rebounds_o_u = None
    assists_o_u = None

    # Points condition
    if points_hit_rate >= 0.65:
        points_o_u = 'over'
    elif points_under_rate >= 0.65:
        points_o_u = 'under'

    # Rebounds condition
    if reb_hit_rate >= 0.65:
        rebounds_o_u = 'over'
    elif reb_under_rate >= 0.65:
        rebounds_o_u = 'under'

    # Assists condition
    if ast_hit_rate >= 0.65:
        assists_o_u = 'over'
    elif ast_under_rate >= 0.65:
        assists_o_u = 'under'

    # Only add to filtered_df if any stat meets the 65% criteria
    if points_o_u or rebounds_o_u or assists_o_u:
        # We now check if the stat has a valid over/under and create temp_df only for that stat
        temp_df = pd.DataFrame()

        if points_o_u:  # If points hit rate meets the criteria
            temp_df = pd.concat([temp_df, pd.DataFrame([{
                'player': player_name,
                'o/u': points_o_u,
                'stat': 'points',
                'line': points_line,
            }])])

        if rebounds_o_u:  # If rebounds hit rate meets the criteria
            temp_df = pd.concat([temp_df, pd.DataFrame([{
                'player': player_name,
                'o/u': rebounds_o_u,
                'stat': 'rebounds',
                'line': rebounds_line,
            }])])

        if assists_o_u:  # If assists hit rate meets the criteria
            temp_df = pd.concat([temp_df, pd.DataFrame([{
                'player': player_name,
                'o/u': assists_o_u,
                'stat': 'assists',
                'line': assists_line,
            }])])

        # Concatenate the temp_df with the filtered_df
        if not temp_df.empty:
            filtered_df = pd.concat([filtered_df, temp_df], ignore_index=True)

# Filter 6 - Player Season Average +-2 Points / +-1 Reb / +-1 Ast vs line

# Loop through the trends DataFrame to process each player's lines
for index, row in trends.iterrows():
    player_name = row['name']
    player_team = row['team']
    site = row['site']  # 'home' or 'away' from trends DataFrame

    # Retrieve the player's points, rebounds, and assists lines
    points_line = row['points_line']
    rebounds_line = row['reb_line']
    assists_line = row['ast_line']

    # Filter game_feed to get the player's games for the 2025 season
    player_games = game_feed[(game_feed['name'] == player_name) & (game_feed['season'] == 2025)]

    # Filter out games where the points line is 0 (you can also filter based on other conditions if necessary)
    player_games = player_games[player_games['points_line'] != 0]

    # Skip player if no games remain after filtering
    if len(player_games) == 0:
        continue

    # Calculate the average points, rebounds, and assists for this player in the 2025 season
    avg_points = player_games['points'].mean()
    avg_rebounds = player_games['rebounds'].mean()
    avg_assists = player_games['assists'].mean()

    # Initialize the over/under values
    points_o_u = None
    rebounds_o_u = None
    assists_o_u = None

    # Check if the averages meet the specified criteria and assign over or under accordingly
    if avg_points >= points_line + 2:  # Points over criteria
        points_o_u = 'over'
    elif avg_points <= points_line - 2:  # Points under criteria
        points_o_u = 'under'

    if avg_rebounds >= rebounds_line + 2:  # Rebounds over criteria
        rebounds_o_u = 'over'
    elif avg_rebounds <= rebounds_line - 2:  # Rebounds under criteria
        rebounds_o_u = 'under'

    if avg_assists >= assists_line + 1.5:  # Assists over criteria
        assists_o_u = 'over'
    elif avg_assists <= assists_line - 1.5:  # Assists under criteria
        assists_o_u = 'under'

    # Add to filtered_df only if the player meets any of the over/under criteria
    temp_df = []

    if points_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': points_o_u,
            'stat': 'points',
            'line': points_line,
        })

    if rebounds_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': rebounds_o_u,
            'stat': 'rebounds',
            'line': rebounds_line,
        })

    if assists_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': assists_o_u,
            'stat': 'assists',
            'line': assists_line,
        })

    # If the temp_df is not empty, concatenate it to filtered_df
    if temp_df:
        temp_df = pd.DataFrame(temp_df)
        filtered_df = pd.concat([filtered_df, temp_df], ignore_index=True)

# Filter 7 - Must have hit line 70% L10 of home/away

# Loop through the trends DataFrame to process each player's lines
for index, row in trends.iterrows():
    player_name = row['name']
    player_team = row['team']
    site = row['site']  # 'home' or 'away' from trends DataFrame

    # Retrieve the player's points, rebounds, and assists lines
    points_line = row['points_line']
    rebounds_line = row['reb_line']
    assists_line = row['ast_line']

    # Filter game_feed to get the player's games (no season filter, only player and most recent games)
    player_games = game_feed[(game_feed['name'] == player_name) & (game_feed['site'] == site)]

    # Sort by 'start_time' to get the most recent games first
    player_games = player_games.sort_values(by='start_time', ascending=False)

    # Get the last 10 games (most recent)
    last_10_games = player_games.head(10)

    # Skip player if less than 10 games remain after filtering
    if len(last_10_games) < 10:
        continue

    # Initialize hit and under rates for the stats
    hit_rate = {'points': 0, 'rebounds': 0, 'assists': 0}
    under_rate = {'points': 0, 'rebounds': 0, 'assists': 0}

    # Loop through the last 10 games to calculate overs and unders for each stat
    for i, game in last_10_games.iterrows():
        # Compare points scored (game['points']) with points line
        points_scored = game.get('points', 0)
        points_diff = points_scored - points_line  # Difference between points scored and points line

        # Compare rebounds and assists with their respective lines
        reb_scored = game.get('rebounds', 0)
        reb_diff = reb_scored - rebounds_line
        ast_scored = game.get('assists', 0)
        ast_diff = ast_scored - assists_line

        # Count overs and unders for points
        if points_diff > 0:
            hit_rate['points'] += 1
        if points_diff < 0:
            under_rate['points'] += 1

        # Count overs and unders for rebounds
        if reb_diff > 0:
            hit_rate['rebounds'] += 1
        if reb_diff < 0:
            under_rate['rebounds'] += 1

        # Count overs and unders for assists
        if ast_diff > 0:
            hit_rate['assists'] += 1
        if ast_diff < 0:
            under_rate['assists'] += 1

    # Calculate hit rates for points, rebounds, assists (overs and unders) for the last 10 games
    total_games = len(last_10_games)
    points_hit_rate = hit_rate['points'] / total_games
    reb_hit_rate = hit_rate['rebounds'] / total_games
    ast_hit_rate = hit_rate['assists'] / total_games

    points_under_rate = under_rate['points'] / total_games
    reb_under_rate = under_rate['rebounds'] / total_games
    ast_under_rate = under_rate['assists'] / total_games

    # Initialize the over/under values
    points_o_u = None
    rebounds_o_u = None
    assists_o_u = None

    # Points condition (70% hit rate)
    if points_hit_rate >= 0.7:
        points_o_u = 'over'
    elif points_under_rate >= 0.7:
        points_o_u = 'under'

    # Rebounds condition (70% hit rate)
    if reb_hit_rate >= 0.7:
        rebounds_o_u = 'over'
    elif reb_under_rate >= 0.7:
        rebounds_o_u = 'under'

    # Assists condition (70% hit rate)
    if ast_hit_rate >= 0.7:
        assists_o_u = 'over'
    elif ast_under_rate >= 0.7:
        assists_o_u = 'under'

    # Now handle each stat based on their individual conditions
    # Only add the stat to filtered_df if it meets the 70% criteria
    temp_df = []

    if points_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': points_o_u,
            'stat': 'points',
            'line': points_line,
        })

    if rebounds_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': rebounds_o_u,
            'stat': 'rebounds',
            'line': rebounds_line,
        })

    if assists_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': assists_o_u,
            'stat': 'assists',
            'line': assists_line,
        })

    # If temp_df is not empty, concatenate it to filtered_df
    if temp_df:
        filtered_df = pd.concat([filtered_df, pd.DataFrame(temp_df)], ignore_index=True)


# Filter 8 - L5 Average must be 2pts/2reb/1.5/ast differential from line

# Loop through the trends DataFrame to process each player's lines
for index, row in trends.iterrows():
    player_name = row['name']
    player_team = row['team']
    site = row['site']  # 'home' or 'away' from trends DataFrame

    # Retrieve the player's points, rebounds, and assists lines
    points_line = row['points_line']
    rebounds_line = row['reb_line']
    assists_line = row['ast_line']

    # Filter game_feed to get the player's games (no season filter, only player and most recent games)
    player_games = game_feed[game_feed['name'] == player_name]

    # Sort by 'start_time' to get the most recent games first
    player_games = player_games.sort_values(by='start_time', ascending=False)

    # Get the last 5 games (most recent)
    last_5_games = player_games.head(5)

    # Skip player if less than 5 games remain after filtering
    if len(last_5_games) < 5:
        continue

    # Calculate the L5 averages for each stat (points, rebounds, assists)
    points_avg = last_5_games['points'].mean()
    rebounds_avg = last_5_games['rebounds'].mean()
    assists_avg = last_5_games['assists'].mean()

    # Initialize the over/under values for each stat
    points_o_u = None
    rebounds_o_u = None
    assists_o_u = None

    # Points condition (±2 points from the line)
    if abs(points_avg - points_line) >= 2:
        points_o_u = 'over' if points_avg > points_line else 'under'

    # Rebounds condition (±2 rebounds from the line)
    if abs(rebounds_avg - rebounds_line) >= 2:
        rebounds_o_u = 'over' if rebounds_avg > rebounds_line else 'under'

    # Assists condition (±1.5 assists from the line)
    if abs(assists_avg - assists_line) >= 1.5:
        assists_o_u = 'over' if assists_avg > assists_line else 'under'

    # Now handle each stat based on their individual conditions
    # Only add the stat to filtered_df if it meets the criteria
    temp_df = []

    if points_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': points_o_u,
            'stat': 'points',
            'line': points_line,
        })

    if rebounds_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': rebounds_o_u,
            'stat': 'rebounds',
            'line': rebounds_line,
        })

    if assists_o_u:
        temp_df.append({
            'player': player_name,
            'o/u': assists_o_u,
            'stat': 'assists',
            'line': assists_line,
        })

    # If temp_df is not empty, concatenate it to filtered_df
    if temp_df:
        filtered_df = pd.concat([filtered_df, pd.DataFrame(temp_df)], ignore_index=True)

# Lists to hold the rows for players hitting 8, 7, and 6 filters
csv_rows_8 = []
csv_rows_7 = []
csv_rows_6 = []

# Group by 'player', 'o/u', and 'line' to get the count of rows for each combination
grouped = filtered_df.groupby(['player', 'o/u', 'line', 'stat']).size().reset_index(name='count')

# Filter for rows with exactly 8, 7, or 6 occurrences
for count in [8, 7, 6]:
    filtered_rows = grouped[grouped['count'] == count]

    # If there are rows that meet the condition, process them
    if not filtered_rows.empty:
        # Keep track of players we've already added to CSV
        added_players = set()

        # Now process the original rows from filtered_df that match the condition
        for _, row in filtered_rows.iterrows():
            player = row['player']
            o_u = row['o/u']
            line = row['line']
            
            # Filter the original filtered_df for the rows matching the player, o/u, and line
            matching_rows = filtered_df[(filtered_df['player'] == player) & 
                                        (filtered_df['o/u'] == o_u) & 
                                        (filtered_df['line'] == line) & 
                                        (filtered_df['stat'] == row['stat'])]
            
            # If the player is not in the added_players set, add them
            if player not in added_players:
                added_players.add(player)
                
                # Clean up the format: select only the necessary columns
                selected_columns = matching_rows[['player', 'o/u', 'stat', 'line', 'projection']]
                
                # Append the row as a dictionary to the correct list
                if count == 8:
                    csv_rows_8.append(selected_columns.iloc[0].to_dict())  # Add as dictionary to keep columns
                elif count == 7:
                    csv_rows_7.append(selected_columns.iloc[0].to_dict())  # Add as dictionary to keep columns
                elif count == 6:
                    csv_rows_6.append(selected_columns.iloc[0].to_dict())  # Add as dictionary to keep columns

# Convert lists to DataFrames
df_8_filters = pd.DataFrame(csv_rows_8)
df_7_filters = pd.DataFrame(csv_rows_7)
df_6_filters = pd.DataFrame(csv_rows_6)

# Save to CSV with formatted headers
df_8_filters.to_csv('8_Filters.csv', index=False)
df_7_filters.to_csv('7_Filters.csv', index=False)
df_6_filters.to_csv('6_Filters.csv', index=False)

print('All Plays Added to CSVs')
