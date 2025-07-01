# Assessing Midfielders' Goal Creation and Positioning Abilities

In this repository, I demonstrate how to extract metrics from seasonal event data to assess midfielders' abilities to create goal-scoring chances for teammates and position themselves in dangerous areas around the opposition goal.

## Data Exploration

The main notebook is [`data_exploration.ipynb`](statsbomb_event/data_exploration.ipynb), in which, after performing some simple queries to practice with the open StatsBomb event data, I defined methods to retrieve aggregated metrics for assessing the midfielder abilities I chose to analyze.

To assess the *Final Pass* capability, which is defined as the ability to create goal-scoring opportunities for teammates through passing, I chose to extract metrics such as the number of assists, Expected Goals (xG) assisted, key passes, and progressive passes.

For the *Box Positioning* capability, which refers to the ability to move into goal-scoring positions in valuable pitch locations through clever positioning in and around the opponent's penalty area at the right time, I examined receptions into the penalty box and in Zone 14. Zone 14 is the area located in the middle of the pitch immediately outside the penalty area and appears crucial for goal scoring (Taylor et al., 2002). This metric indicates how well players position themselves near the opposition goal to receive passes. The number of xG serves as an indicator of a player's ability to position themselves well for shots—the higher the xG, the better their ability to find good goal-scoring positions.

Finally, I normalized all metrics and averaged them to create a single metric that shows the overall abilities of each midfielder.

## Data Extraction

The [`data_extraction.ipynb`](statsbomb_event/data_extraction.ipynb) notebook downloads the [open StatsBomb event data](https://github.com/statsbomb/open-data) from all matches of the 2015/2016 Premier League season into the `data` directory (which is not included to keep the repository lightweight). I used the [`statsbombpy`](https://github.com/statsbomb/statsbombpy) package to communicate directly with the StatsBomb API.

## Determining Players' Positions

I further grouped the StatsBomb players' positions into four categories (Goalkeeper, Defender, Midfielder, Attacker) in [`position_definition.py`](statsbomb_event/position_definition.py) to extract metrics specifically for midfielders.

During a season, and even within a single match, a player can be classified with different positions. To uniquely assign each player's position, I calculate in [`player_positions`](statsbomb_event/player_positions.ipynb) how many times they are reported in each of the above categories over the season and select the most frequent one. In case of a tie, I retain all categories with the maximum frequency.