# Refer to this module's readme

'''
def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))



def create_report(spacecraft):
    return f"""
======== REPORT ========

Name: {spacecraft.get("name", "Unkown")}
Distance: {spacecraft.get("distance", "Unknown")}AU

========================
"""

main()
'''

distances ={
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,

}

def convert(au):
    return au * 149597870700


def main():
    '''
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU form Earth")
    '''
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


main()