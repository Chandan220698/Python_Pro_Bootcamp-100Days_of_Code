# @Author: Chandan Kumar: https://github.com/Chandan220698/
# Nesting

# List and dict nested in main dictionary
# Example:

'''
{
    key1: [list],
    key2: {dict}
}
'''

# Nesting list in dictionary
travel_log = {
    "France": ["Paris, Lille, Dijon"],      # Value for this key is list
    "Germany": ["Berlin, Hamburg"]
}
# list nested inside dictionary which iteself nested in a dictionary
travel_log2 = {
    "France": {"cities_visited": ["Paris, Lille, Dijon"], "total_visits": 12},      # Value for this key is list
    "Germany": {"cities_visited": ["Berlin, Hamburg"], "total_visits": 10}
}

# Nesting dictionaries in list
travel_log3 = [
    {
        "country": "France",
        "cities_visited": ["Paris, Lille, Dijon"],
        "total_visits": 12
    },
    {
        "Germany":"Germany",
        "cities_visited": ["Berlin, Hamburg"],
        "total_visits": 5
    }
]