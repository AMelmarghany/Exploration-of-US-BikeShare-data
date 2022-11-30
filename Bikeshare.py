import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a city to calculate the data for it\n(Washington, New york city or Chicago) ?\n').lower()
        if city not in CITY_DATA:
            print('Invalid input! Try Again')
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please Enter a month\nJanuary, Febraury... to June or all\n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in months:
            print('Invalid Input! Try Again')
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day\n').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and day not in days:
            print('Invalid input! Try Again')
        else:
            break


    print('-'*40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month is: {}' .format(df['month'].mode()[0]))

    # display the most common day of week
    print('Most common day of week is: {}' .format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('Most common start hour: {}' .format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common used start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most common used end station is: {}' .format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    frequent_trip = df['Start Station'] + " ==> " + df['End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip: \n', frequent_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average travel time is: ', mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('Uers Types:\n', user_types)

    # Display counts of gender
    try:
        print("Gender :\n", df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
        print('The earliest birth year is: ', int(df['Birth Year'].min()))
        print('The most recent birth is: ', int(df['Birth Year'].max()))
        print('The most common year of birth is: ', int(df['Birth Year'].mode()[0]))
    except:
        print('Sorry, No data available for Washington.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    data_row = 0
    while True:
        display_raw_data = input('Would you like to view more raw data? yes or no? ').lower()
        if display_raw_data == 'yes':
            print(df.iloc[data_row : data_row + 5])
            data_row += 5
        elif display_raw_data == 'no':
            break
        else:
            print('Invalid input! Try again.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
