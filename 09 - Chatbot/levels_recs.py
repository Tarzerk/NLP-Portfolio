from levels_data import data
import random

def get_areas_and_bosses(level: int) -> str:
    """
    Returns a formatted string containing the locations and bosses that match
    the given level.

    Args:
        level (int): The level to match against.

    Returns:
        str: A string containing the matched locations and bosses, or a
        message indicating that no matches were found.
    """
    matching_bosses = []
    matching_locations = []
    
    if 1 <= level < 20:
        return "At your level, continue exploring Limgrave. No bosses matched, continue leveling your stats up."
    if level > 150:
        return "At your level, you probably have explored most areas now as well as defeated most bosses. Consider starting NG+."
    
    for key in data.keys():
        start, end = key.split('-')
        if int(start) <= level <= int(end):
            matching_locations.append(data[key]['location'])
            bosses = data[key]['bosses']
            if isinstance(bosses, str):
                if key not in matching_bosses:
                    matching_bosses.append(bosses)
            else:
                for boss_key in bosses.keys():
                    boss_start, boss_end = boss_key.split('-')
                    if int(boss_start) <= level <= int(boss_end):
                        if bosses[boss_key] not in matching_bosses:
                            matching_bosses.append(bosses[boss_key])
    
    if matching_locations and matching_bosses:
        location_str = ", ".join(matching_locations)
        boss_str = ", ".join(matching_bosses)

        sent1 = (
            f"Since you are at level {level}, consider exploring these areas if you haven't already: {location_str}\n"
            f"You should fight these bosses as well: {boss_str}"
        )
        sent2 = (
            f"If you're currently at level {level}, I suggest exploring these areas if you haven't already: {location_str}\n"
            f"Additionally, you should consider fighting these bosses: {boss_str}."
        )
        sent3 = (
            f"At your current level ({level}), you may want to explore these areas if you haven't already: {location_str}\n"
            f"You may also want to fight these bosses: {boss_str}"
        )
        
        random_number = random.randint(1, 3)
    
        if random_number == 1:
            return sent1
        elif random_number == 2:
            return sent2
        return sent3
    
    return "No matches found."