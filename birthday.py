from datetime import datetime, timedelta

users = [
    {'name': 'Bill', 'birthday': '13.11.1975'},
    {'name': 'Jill', 'birthday': '13.11.1990'},
    {'name': 'Kim', 'birthday': '17.11.2000'},
    {'name': 'Jan', 'birthday': '17.06.1989'},
    {'name': 'Tom', 'birthday': '12.11.1991'},
    {'name': 'Bob', 'birthday': '12.12.1996'}
    ]

def get_birthdays_per_week():

    days = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
        }

    #time zone next week
    current_datetime = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
    next_year = datetime(year=datetime.now().year+1, month=datetime.now().month, day=datetime.now().day)
    datetime_plus_one_week = current_datetime + timedelta(weeks=1)
    datetime_weekday = datetime_plus_one_week.weekday()
    current_datetime_weekday = current_datetime.weekday()
    datetime_start = current_datetime - timedelta(days=current_datetime_weekday) + timedelta(days=5)
    datetime_Monday = datetime_plus_one_week - timedelta(days=datetime_weekday)
    datetime_end = datetime_Monday + timedelta(days=4)
    
    #search persons who have a birthday in the next week and list them by day on which they have a birthday
    for user in users:
        name = user['name']
        birthday_str = user['birthday']
        birthday_date = datetime.strptime(birthday_str, '%d.%m.%Y')
        this_year_birthday = birthday_date.replace(year=current_datetime.year)
        next_year_birthday = birthday_date.replace(year=next_year.year)
        if this_year_birthday <= current_datetime:
            next_birthday = next_year_birthday
        else:
            next_birthday = this_year_birthday
        if next_birthday >= datetime_start and next_birthday <= datetime_end:
            if next_birthday.weekday() == 0 or next_birthday.weekday() == 5 or next_birthday.weekday() == 6:
                days['Monday'].append(name)
            elif next_birthday.weekday() == 1:
                days['Tuesday'].append(name)
            elif next_birthday.weekday() == 2:
                days['Wednesday'].append(name)
            elif next_birthday.weekday() == 3:
                days['Thursday'].append(name)
            elif next_birthday.weekday() == 4:
                days['Friday'].append(name)

    #format for displaying persons having a birthday
    birthdays_next_week = ''     
    for day, names in days.items():
        if names:
            birthdays_next_week += f"{day}: {', '.join(names)}\n"

    #checking if someone has a birthday
    if birthdays_next_week == '':
        return print('There are no birthdays next week.')
    else:
        return print(birthdays_next_week)

if __name__ == "__main__":
    get_birthdays_per_week()