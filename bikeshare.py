import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_input(inp, possible_inputs, message):
    """Ensure that the input is inside of the allowed ones"""
    while True:
        if inp in possible_inputs:
            return inp
        inp = input(message)

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
    input0 = input("Write the name of one of these cities to see its data: Chicago, New York, Washington\n")
    possible_input0 = ['Chicago', 'New York', 'Washington', 'chicago', 'new york', 'washington']
    m0 = "Please repeat your answer with one of the following options:  Chicago, New York, Washington\n"
    city = check_input(input0,possible_input0,m0).lower()
    
    input1 = input('Write one of the following filters: month, day, both, none \n')
    possible_input1 = ['month', 'day', 'both', 'none','Month', 'Day', 'Both', 'None']
    m1 = "Please repeat your answer with one of the following options:  month, day, both or none \n"
    input1 = check_input(input1,possible_input1,m1).lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    if input1.lower() == 'month' or input1.lower() == 'both':
        input2 = input("With which month of the year do you want to filter the data?\n")
        possible_input2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 
                           'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        m2 = "Please repeat your answer with the name of the month you have chosen\n"
        month = check_input(input2,possible_input2,m2).lower()
    else:
        month = 'all'
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if input1.lower() == 'day' or input1.lower() == 'both':
        possible_input3 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                           'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        input3 = input("With which day of the week do you want to filter the data? \n")
        m3 = "Please repeat your answer with the name of the day you have chosen\n"
        day = check_input(input3,possible_input3,m3)
    else:
        day = 'all'

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)+1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    print('shape',df.shape)
    print('mode',df['month'].mode())
    popular_month = months[df['month'].mode()[0]]
    print('The most frequent month is:', popular_month,'\n')
    
    # TO DO: display the most common day of week
    popular_day = days[df['day_of_week'].mode()[0]]
    print('The most frequent day is:', popular_day,'\n')
    
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['Start Hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = int(df['Start Hour'].mode())
    print('The most frequent hour is:', popular_hour,'\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most frequent start station is:', popular_start_station,'\n')
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most frequent end station is:', popular_end_station,'\n')

    # TO DO: display most frequent combination of start station and end station trip
    #Create a Serie with all the combinations
    combinations_list = [x for x in zip(df['Start Station'],df['End Station'])]
    combinations_Serie = pd.Series(combinations_list)
    # find the most common combination
    popular_combination_st = combinations_Serie.mode()[0]
    print('The most combination of start station and end station trip is:', popular_combination_st,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract the time of start and end to compute the time traveled
    Start_Time = df['Start Time'].dt.hour*3600+df['Start Time'].dt.minute*60+df['Start Time'].dt.second
    End_Time = df['End Time'].dt.hour*3600+df['End Time'].dt.minute*60+df['End Time'].dt.second
    df['Time traveled'] = End_Time - Start_Time
    #With Time traveled it is possible to compute the total travel time and mean
    print('The total travel time is:', df['Time traveled'].sum(), 'seconds')
    
    # TO DO: display mean travel time
    print('The mean travel time time is:', df['Time traveled'].mean(), 'seconds')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types is:\nSubscriber:', user_types[0], 'Customer:', user_types[1])

    # TO DO: Display counts of gender
    print('The counts of gender is:\nMale', df['Gender'].value_counts()[0],'Female:',df['Gender'].value_counts()[1])

    # TO DO: Display earliest, most recent, and most common year of birth
    print('The earliest year of birth is:', int(df['Birth Year'].min()))
    print('The most recent year of birth is:', int(df['Birth Year'].max()))
    print('The most common year of birth is:', int(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.shape[0]==0:
            restart = input('\nSorry, there is no data with these filters, would you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes' and restart.lower() != 'Yes':
                break
            continue
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data = input('\nWould you like to see a portion of raw data? Enter yes or no.\n')
        iteration = 0
        while raw_data.lower() == 'yes':
            aux = df.shape[0]-iteration*5
            if aux>=5:
                print(df[iteration*5:iteration*5+5])
            else:
                print(df[iteration*5:aux+iteration*5])
                break
            iteration += 1
            raw_data = input('\nWould you like to see aonother portion of raw data? Enter yes or no.\n')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
