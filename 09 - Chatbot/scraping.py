from bs4 import BeautifulSoup
import requests
import re


def get_build(name: str) -> str:
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
        for i, line in enumerate(lines):
            if "Ashes of War" in line:
                lines = lines[:i + 1]
                break
        result = "\n".join(lines)
        return result
    else:
        print(f"No build found with name '{name}'")
    return ""


def main():
    # testing
    txt = get_build("bandit")
    print(txt)


def find_dragon_smithing_stones(name: str) -> str:
    url = "https://www.gamesradar.com/elden-ring-ancient-dragon-smithing-stones-somber/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    id = ""

    if "somber" in name.lower():
        id = "section-somber-ancient-dragon-smithing-stones-locations"
    else:
        id = "section-ancient-dragon-smithing-stones-locations"

    h3_tag = soup.find('h3', {'class': 'article-body__section', 'id': id})

    # find all the ol tags until there is a h2 tag
    ol_tags = []
    next_tag = h3_tag.find_next_sibling()
    while next_tag and next_tag.name != 'h2':
        if next_tag.name == 'ol':
            ol_tags.append(next_tag)
        next_tag = next_tag.find_next_sibling()

    # print the li tags within each ol tag
    li_strings = []
    for ol in ol_tags:
        for li in ol.find_all('li'):
            li_strings.append(f"- {li.text.strip()}\n\n")

    # print the li strings
    print(''.join(li_strings))

    return ''.join(li_strings)


if __name__ == '__main__':
    main()