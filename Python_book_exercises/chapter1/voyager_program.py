
#get user input

current_speed = 38_241 #miles/hour
current_distance = 16_637_000_000 #miles

def get_user_input():

    try:
        number_of_days_str = input('Enter number of days since 9/25/09')
        number_of_days_int = int(number_of_days_str)

        return  number_of_days_int
    except (TypeError, ValueError) as e:
        print(e)
        return None


#convert days to hours
def convert_days_to_hours(days_int):
    days_hours = days_int * 24

    return days_hours

def calculate_distance_in_miles(time_in_hours):

    distance_in_miles = time_in_hours * current_speed
    return distance_in_miles + current_distance

def calculate_distance_in_km(time_in_hours):

    distance_in_km = calculate_distance_in_miles(time_in_hours) * 1.609344
    return distance_in_km

def calculate_astronomical_ditance(time_in_hours):
    #
    distance_in_au = ((calculate_distance_in_miles(time_in_hours) + current_distance) / 92955807.267433)
    return distance_in_au

def calculate_radio_trip(time_in_hours):

    #convert distance to meters

    distance_in_radio_seconds = (calculate_distance_in_miles(time_in_hours)+current_distance) / 1609.34
    distance_in_radio_hours = distance_in_radio_seconds / 3600

    return distance_in_radio_hours

def main():
    #get input from user
    days = get_user_input()

    #convert days to hours
    days_in_hours = convert_days_to_hours(days)

    distance_in_miles = calculate_distance_in_miles(days_in_hours)
    distance_in_km = calculate_distance_in_km(days_in_hours)
    distance_in_au = calculate_astronomical_ditance(days_in_hours)

    radio_time_in_hours = calculate_radio_trip(days_in_hours)

    print("Distance in miles is")




















