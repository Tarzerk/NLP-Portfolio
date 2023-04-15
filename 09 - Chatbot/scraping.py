from bs4 import BeautifulSoup
import requests
import re

def get_build(name: str) -> str:
    """
    Takes the name of an Elden Ring class as input and returns the corresponding best build
    from https://www.denofgeek.com/games/elden-ring-best-builds-every-class-stats-pvp-pve/.

    Args:
    - name (str): The name of the Elden Ring class (case-insensitive).

    Returns:
    - str: A string containing the best build for the specified class. The string is formatted
      as follows:
      - The first line is the class name followed by a colon and a space.
      - The following lines contain the recommended stats for the class, with each line starting
        with a stat name followed by a colon and a space.

      If no build is found for the specified class, the function returns "Error: class not found".
    """
    
    url = "https://www.denofgeek.com/games/elden-ring-best-builds-every-class-stats-pvp-pve/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    builds = soup.find_all('h2')

    # Remove any h2 tags that don't start with "Elden Ring: Best "
    builds = [build for build in builds if build.text.startswith("Elden Ring: Best ")]
    
    name = re.sub(r'(?i)astrologer', 'astrolger', name)

    build = None
    for b in builds:
        if name.lower() in b.text.lower():
            build = b
            break
        
    if not build:
        return "Error: class not found"
    
    if build:
        build_text = ''
        for p in build.find_next_siblings('p'):
            strong = p.find('strong')
            if strong:
                build_text += p.get_text(separator='\n') + '\n'
            else:
                break
            
        build_text = str(build_text).strip()
        build_text = build_text.replace(": ", ":").replace(":\n", ": ").replace("\n:", ": ")
        
        # remove unnecessary info after stats
        lines = build_text.split("\n")
        ashes = False
        for i, line in enumerate(lines):
            if "Ashes of War" in line:
                lines = lines[:i+1]
                ashes = True
                break
        result = "\n".join(lines)
        result = re.sub(r"(Spells:.*)\n.*", r"\1", result) if not ashes else result # for confessor class
        return result
    else:
        print(f"No build found with name '{name}'")
    return ""