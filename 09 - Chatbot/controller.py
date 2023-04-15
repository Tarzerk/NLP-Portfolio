from flask import Flask, request
import requests
import random
from scraping import get_build
from levels_recs import get_areas_and_bosses

app = Flask(__name__)


@app.route('/areas-and-bosses', methods=['GET'])
def get_level_recs():
    """
    Returns a string with areas and bosses recommended for a given level.
    
    Args:
        level (int): The level of the character. Must be between 1 and 150.
    Returns:
        str: A string with areas and bosses recommended for the given level.
             Returns an error message if the level parameter is missing, or 
             if it is not a valid integer or outside the valid range.
    """
    level = request.args.get('level')
    if level is not None:
        try:
            level_int = int(level)
            if 1 <= level_int <= 200:
                result_str = get_areas_and_bosses(level_int)
                return result_str
            else:
                return "Error: level must be between 1 and 200."
        except ValueError:
            return "Error: level must be a valid integer."
    else:
        return "Error: level parameter is missing."


@app.route('/builds', methods=['GET'])
def get_build_advice():
    """
    Returns a string with build advice for a given class name.
    
    Args:
        name (str): The name of the class.
    Returns:
        str: A string with build advice for the given class name.
    """
    name = request.args.get('name')
    str = get_build(name)
    return str


@app.route('/builds/stats', methods=['GET'])
def get_build_stats():
    """
    Returns a string with recommended stats to upgrade for a given class name.
    
    Args:
        name (str): The name of the class.  
    Returns:
        str: A string with recommended stats to upgrade for the given class name.
    """
    name = request.args.get('name')
    build = get_build(name)
    primary_stats = build.split("\n")[0].replace("Primary Stats: ", "")
    secondary_stats = build.split("\n")[1].replace("Secondary Stats: ", "")
    stats_list = primary_stats.split(", ") + secondary_stats.split(", ")
    stats_str = ", ".join(stats_list[:-1]) + ", and " + stats_list[-1]
    
    sentence1 = f"Based on your class, I recommend upgrading the following stats: {stats_str}"
    sentence2 = f"Considering your class, the stats you should upgrade are: {stats_str} " 
    sentence3 = f"Given your character class, it is recommended that you upgrade your stats of {stats_str}"
    random_number = random.randint(1, 3)
    
    if random_number == 1:
        return sentence1
    elif random_number == 2:
        return sentence2

    return sentence3


@app.route('/builds/weapons', methods=['GET'])
def get_build_weapon():
    """
    Returns a string with recommended weapons to upgrade for a given class name.
    
    Args:
        name (str): The name of the class.
    Returns:
        str: A string with recommended weapons to upgrade for the given class name.
    """
    name = request.args.get('name')
    build = get_build(name)
    weapons = build.split("\n")[2].replace("Weapon: ", "")
    weapons_list = weapons.split(", ")
    weapons_str = ", ".join(weapons_list[:-1]) + ", and " + weapons_list[-1]
    
    sentence1 = "Considering your class, the weapons you should upgrade are " + weapons_str
    sentence2 = "Based on your class, the recommended weapons to use are: " + weapons_str
    sentence3 = "To optimize your build for your class, it is recommended that you upgrade the following weapons: " + weapons_str
    
    random_number = random.randint(1, 3)
    
    if random_number == 1:
        return sentence1
    elif random_number == 2:
        return sentence2

    return sentence3


@app.route('/bosses', methods=['GET'])
def get_bosses():
    """
    Returns information about a given boss, including their location, drops, and a brief description.

    Parameters:
        name (str): The name of the boss to look up.
    Returns:
        str: A string containing information about the boss. If the boss is not found, an error message is returned. 
    Raises:
        Exception: If the boss name is not found in the Elden Ring API.
    """
    name = request.args.get('name')
    
    if name.lower() == 'margit':
        return "Margit, the Fell Omen is found in Stormhill when players attempt to approach Stormveil Castle. He is one of the earliest bosses and drops 12,000 runes."
    
    if name.lower() == 'morgott':
        return "Morgott, The Omen King, also known as Morgott the Grace Given, is a Demigod Boss in Elden Ring. Morgott is the true identity of Margit, the Fell Omen, and the self-proclaimed \"Last of All Kings\". Although he and his twin brother Mohg were imprisoned deep in the Subterranean Shunning-Grounds for being born as Omen royalty, Morgott still loved the Golden Order and defended the capital when his fellow demigods invaded during the Shattering. This is not an optional boss as players must defeat him to advance in Elden Ring."
    
    try:
        response = requests.get(f'https://eldenring.fanapis.com/api/bosses?name={name}')
        json_data = response.json()
        
        boss_data = json_data['data'][0]

        description = boss_data['description']
        drops = ', '.join(boss_data['drops'])
        location = boss_data['location']
        name = boss_data['name']
        
        sentence1 = f"The boss full name is {name}. They are located at {location}. The drops include {drops}. {description}"
        sentence2 = f"The boss's full name is {name}. They can be found in {location}. They drop {drops}. Here's a brief description: {description}"
        sentence3 = f"{name} is a boss located in {location}. They drop {drops}. {description}"
        random_number = random.randint(1, 3)
        
        if random_number == 1:
            return sentence1
        elif random_number == 2:
            return sentence2

        return sentence3
    
    except Exception as e:
        return f"Unexpected error: {name} not found"


@app.route('/items', methods=['GET'])
def get_items():
    """
    Retrieve information about an item by its name.

    Args:
        name (str): The name of the item to retrieve information about.

    Returns:
        str: A sentence containing the name of the item, its description, and its effect.

    Raises:
        Exception: If the item name is not found in the Elden Ring API.
    """
    name = request.args.get('name')
    try:
        response = requests.get(f'https://eldenring.fanapis.com/api/items?name={name}')
        json_data = response.json()
        
        boss_data = json_data['data'][0]

        description = boss_data['description']
        effect = boss_data['effect']
        name = boss_data['name']
        
        sentence = name + ": " + description + " " + effect
        return sentence
    
    except Exception as e:
        return f"Unexpected error: {name} not found"



@app.route('/classes', methods=['GET'])
def get_classes():
    """
    Retrieves information about an Elden Ring character class.

    Parameters:
        name (str): The name of the character class to look up.
    Returns:
        A string containing the name, description, and starting stats of the character class. If the name is not found, an 
        error message is returned instead.
    """
    name = request.args.get('name')
    try:
        response = requests.get(f'https://eldenring.fanapis.com/api/classes?name={name}')
        json_data = response.json()
        
        class_data = json_data['data'][0]

        name = class_data['name']
        description = class_data['description'][0].lower() + class_data['description'][1:]
        stats = class_data['stats']
        
        sentence = f"The {name} class is {description}. The starting stats are: "
        for key, value in stats.items():
            sentence += f'{key}: {value}, '
        sentence = sentence[:-2]
        print(sentence)
        
        return sentence
    except Exception as e:
        return f"Unexpected error: {name} not found"


@app.route('/compare-classes', methods=['GET'])
def compare_classes():
    """
    Retrieves information about an Elden Ring character class.

    Parameters:
        name (str): The name of the character class to look up.
    Returns:
        A string containing the name, description, and starting stats of the character class. If the name is not found, an 
        error message is returned instead.
    """
    name1 = request.args.get('class1')
    name2 = request.args.get('class2')

    try:
        # call APIs
        response1 = requests.get(f'https://eldenring.fanapis.com/api/classes?name={name1}')
        json_data1 = response1.json()
        class_data1 = json_data1['data'][0]

        
        response2 = requests.get(f'https://eldenring.fanapis.com/api/classes?name={name2}')
        json_data2 = response2.json()
        class_data2 = json_data2['data'][0]

        # parsing data
        name1 = class_data1['name']
        description1 = class_data1['description']
        stats1 = ', '.join([f"{k}: {v}" for k, v in class_data1['stats'].items()])

        name2 = class_data2['name']
        description2 = class_data2['description']
        stats2 = ', '.join([f"{k}: {v}" for k, v in class_data2['stats'].items()])

        # combining responses
        response = f"Comparison between {name1} and {name2}: \n\n"
        response += f"{name1} class description: {description1} \n"
        response += f"{name2} class description: {description2} \n\n"
        response += f"{name1} starting stats: {stats1} \n"
        response += f"{name2} starting stats: {stats2} \n"

        return response
    except Exception as e:
        return f"Unexpected error: {name1} or {name2} not found"


if __name__ == '__main__':
    app.run(debug=True)