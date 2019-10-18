##This program calculate the of water
#that would be spread accross the 48 contiguous U.S states


great_lake_volume = 22810.0 #Area and depth of the great lakes water
states_area = 8080464.3 #Area in km2

def calculate_depth(volume = great_lake_volume, area = states_area):

    depth = volume / area

    return round(depth , 5)

def getUserInput():

    try:
        volume_str = input('Type volume here (in km3): ')
        area_str = input('Type volume here (in km3): ')

        if (volume_str != '' and area_str != ''):
            volume = float(volume_str)
            area = float(area_str)

            return volume, area
        elif (volume_str == '' and area_str == ''):
            return '', ''

    except (ValueError, TypeError) as e:
        print(e)


def main():

    volume, area = getUserInput()

    if (volume == '' and area == ''):
        depth = calculate_depth()
    else:
        depth = calculate_depth(volume, area)


    print("Depth of all states with water spread evenly is: {:} km".format(depth))


if __name__ == '__main__':
    main()
