data = {
    '1-40': {
        'location': 'Limgrave',
        'bosses': {
            '20-40': 'Margit, the Fell Omen',
            '35-40': 'Flying Dragon Agheel'
        }
    },
    '20-30': {
        'location': 'Weeping Peninsula',
        'bosses': 'Leonine Misbegotten'
    },
    '40-70': {
        'location': 'Liurnia of the Lakes',
        'bosses': {
            '30-70': 'Red Wolf of Radagon',
            '50-70': 'Magma Wyrm Makar',
            '70-80': 'Godskin Noble',
            '70-100': 'Glintstone Dragon Adula'
        }
    },
    '50-60': {
        'location': 'Ainsel River',
        'bosses': 'Dragonkin Soldier of Nokstella'
    },
    '60-70': {
        'location': 'Caelid',
        'bosses': {
            '60-70': 'Commander O\'Neil',
            '60-70': 'Magma Wyrm',
            '65-70': 'Cemetery Shade',
            '65-70': 'Decaying Ekzykes',
            '65-70': 'Crucible Knight & Misbegotten Warrior'
        }
    },
    '60-80': {
        'location': 'Atlas Plateau',
        'bosses': {
            '60-80': 'Erdtree Burial Watchdog',
            '70-80': 'Godefroy The Grafted',
            '75-80': 'Godskin Apostle',
            '100-120': 'Ancient Dragon Lansseax',
        }
    },
    '70-100': {
        'location': 'Leyndell The Royal Capital',
        'bosses': {
            '60-100': 'Godfrey First Elden Lord',
            '70-100': 'Mohg the Omen'
        }
    },
    '90-100': {
        'location': 'Dragonbarrow',
        'bosses': {
            '50-100': 'Flying Dragon Greyoll',
            '90-100': 'Godskin Apostle'
        }
    },
    '80-120': {
        'location': 'Mountaintops of the Giants',
        'bosses': {
            '80-120': 'Commander Niall',
            '90-120': 'Borealis the Freezing Fog',
            '100-120': 'Godskin Apostle and Godskin Noble (Spiritcaller Snail)'
        }
    },
    '120-150': {
        'location': 'Miquella\'s Haligtree',
        'bosses': {
            '120-150': 'Loretta Knight of the Haligtree',
            '130-150': 'Malenia Blade of Miquella'
        }
    }
}


def get_areas_and_bosses(level: int) -> str:
    matching_bosses = []
    matching_locations = []

    if 1 <= level < 20:
        return "Location: Limgrave\nNo bosses matched"

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
        result_str = f"Locations: {location_str}\nBosses: {boss_str}"
        print(result_str)
    else:
        return "No matches found."

    return result_str