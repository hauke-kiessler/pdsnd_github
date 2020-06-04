import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("We have the following data sets for you to choose from. Select the appropriate number for the city: \n\n      1 = Chicago\n      2 = New York City \n      3 = Washington\n\nPlease choose one city to analyze: ")

    #while llop to handle invalid inputs
    while True:
        if city == '1' or city == '01':
            print('All right, let\'s see what the situation is like in Chicago \n')
            break

        elif city == '2' or city == '02':
            print('All right, let\'s see what the situation is like in New York City \n')
            break

        elif city == '3' or city == '03':
            print('All right, let\'s see what the situation is like in Washington \n')
            break

        else:
            print('Upps, something went wrong: Are you sure you entered the right number?')
            city = input('Please try again: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ('What month would you like to analyze?\n1 = January    2 = February    3 = March    4 = April\n5 = May        6 = June        7 = all\n\nNote: Unfortunately, we only have data from January to June.\n\nPick a number from the list: ')
    #while llop to handle invalid inputs
    while True:
        if month in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06', '7', '07']:
            print('Great choice!\n')
            break

        else:
            print('Are you sure you punched in the right number?')
            month = input('Please try again: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week_choice = input('Do you also want to filter by a specific weekday (Monday, Tuesday,...)? Enter \'yes\' or \'no\': ')

    while True:
        if day_of_week_choice == 'yes' or day_of_week_choice == '\'yes\'':
            day = input ('Enter the weekday (Monday, Tuesday,...) here: ')
            day = day.lower()

            while True:
                if day not in WEEKDAYS:
                    print('I\'m sorry, did you make a mistake? Can\'t put the day in order?')
                    day = input('Please try again: ')
                    day = day.lower()


                else:
                    print('Awesome. Your input will be processed')
                    break

            break

        elif day_of_week_choice == 'no' or day_of_week_choice == '\'no\'':
                print ('Your input will be processed')
                day = 'all'
                break


        else:
            print('no valid input. ')
            day_of_week_choice = input('Try again: ')



    print('-'*40)
  #dictionaries for return:
    city_dict = {'1': 'chicago',
                 '2': 'new york city',
                 '3': 'washington'}
    if city in city_dict:
              city = city_dict[city]

    month_dict = {'1': 'january',
                  '2': 'february',
                  '3': 'march',
                  '4': 'april',
                  '5': 'may',
                  '6': 'june',
                  '7': 'all'}


    if month in month_dict:
              month = month_dict[month]
    day_dict = {'monday': '0',
                  'tuesday': '1',
                  'wednesday': '2',
                  'thursday': '3',
                  'friday': '4',
                  'saturday': '5',
                  'sunday': '6'}


    if day in day_dict:
              day = day_dict[day]

    return city, month, day



def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    #Add missing columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.dayofweek
    df ['Hours'] = df['Start Time'].dt.hour

    total_rides = len(df)
    filtered_rides = total_rides

    #Filter specifications
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day_of_Week'] == int(day)]

    print('Your data will be loaded...')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print('   Month:      ', MONTHS[(common_month) -1].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['Day_of_Week'].mode()[0]
    print('   Day:        ', WEEKDAYS[common_day_of_week].title())

    # TO DO: display the most common start hour
    common_hour = df['Hours'].mode()[0]
    print('   Start hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Start Station: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('End Station:   ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_trip = df['trip'].mode()[0]
    print('The most frequent trip is from', most_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:   ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average rental time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    # Washington has no gender information
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)

    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    # Washington has no birthday information
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        print('The youngest member is born in', earliest)
        most_recent = int(df['Birth Year'].max())
        print('The oldest member is born in', most_recent)
        most_common = int(df['Birth Year'].mode()[0])
        print('The most Users are born in', most_common)

    else:
        print("There is no birth year information in this city.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    """Specifies whether the user wants to see 5 lines of raw data"""


    count = 0

    while True:
        raw_input = input('Would you like to see the raw data? Enter \'yes\' or\' no\': ')

        if raw_input.lower() != 'yes' and raw_input.lower() != 'y':
            break

        else:
            print(df[count: count + 5])
            print('='*40)
            count = count + 5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
