import pandas as pd

# Defining the data as a dictionary
# Apparently in event data there is the position Center Forward that is not present in the documentation
data = {
    "Position Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    "Position Abbreviation": ["GK", "RB", "RCB", "CB", "LCB", "LB", "RWB", "LWB", "RDM", "CDM", "LDM", "RM", "RCM", "CM", "LCM", "LM", "RW", "RAM", "CAM", "LAM", "LW", "RCF", "ST", "LCF", "SS", "CF"],
    "Position Name": [
        "Goalkeeper", "Right Back", "Right Center Back", "Center Back", "Left Center Back", "Left Back", 
        "Right Wing Back", "Left Wing Back", "Right Defensive Midfield", "Center Defensive Midfield", 
        "Left Defensive Midfield", "Right Midfield", "Right Center Midfield", "Center Midfield", 
        "Left Center Midfield", "Left Midfield", "Right Wing", "Right Attacking Midfield", 
        "Center Attacking Midfield", "Left Attacking Midfield", "Left Wing", "Right Center Forward", 
        "Striker", "Left Center Forward", "Secondary Striker", "Center Forward"
    ]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Adding a new column 'Position Category' based on conditions
def categorize_position(position_name):
    if "Midfield" in position_name:
        return "Midfielder"
    elif "Back" in position_name:
        return "Defender"
    elif "Goalkeeper" in position_name:
        return "Goalkeeper"
    else:
        return "Attacker"

df['Position Category'] = df['Position Name'].apply(categorize_position)

# Saving to CSV
df.to_csv("./data/expanded_positions.csv", index=False)
