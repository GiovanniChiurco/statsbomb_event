import pandas as pd

def add_name_players(metric_df: pd.DataFrame, players_df: pd.DataFrame):
    """Add the players names to metric dataframe

    Parameters
    ----------
    metric_df : pd.DataFrame
        player_id, metric
    players_df : pd.DataFrame
        player_id, player_name
    """
    return pd.merge(left=metric_df, right=players_df, on="player_id")

def check_column(partial_name: str, column_list: list[str]) -> None:
    for col in column_list:
        if partial_name in col:
            print(col)
