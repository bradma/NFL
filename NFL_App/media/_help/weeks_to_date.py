import datetime
import requests

#from Select.models import game_week

def assign_weeks():
    weeks = (
        (datetime.date(2015, 9, 10), 1),    #Week 1
        (datetime.date(2015, 9, 17), 2),    #Week 2
                (datetime.date(2015, 9, 24), 3),        #Week 3
                (datetime.date(2015, 10, 1), 4),        #Week 4
                (datetime.date(2015, 10, 8), 5),        #Week 5
                (datetime.date(2015, 10, 15), 6),       #Week 6
                (datetime.date(2015, 10, 22), 7),       #Week 7
                (datetime.date(2015, 10, 29), 8),       #Week 8
                (datetime.date(2015, 11, 5), 9),        #Week 9
                (datetime.date(2015, 11, 12), 10),      #Week 10
                (datetime.date(2015, 11, 19), 11),      #Week 11
                (datetime.date(2015, 11, 26), 12),      #Week 12
                (datetime.date(2015, 12, 3), 13),       #Week 13
                (datetime.date(2015, 12, 10), 14),      #Week 14
                (datetime.date(2015, 12, 17), 15),      #Week 15
                (datetime.date(2015, 12, 24), 16),      #Week 16
                (datetime.date(2016, 1, 2), 17),      #Week 17
                (datetime.date(2016, 1, 5), 18),      #Week 18
                (datetime.date(2016, 1, 14), 19),       #Week 19
                (datetime.date(2016, 1, 21), 20),       #Week 20)
    )
    available_weeks = [x[1] for x in weeks if x[0] <= datetime.date.today()]
    return available_weeks

def get_json():
    get_my_fib = requests.get('http://www.nfl.com/liveupdate/scores/scores.json?random=1434223490000')
    return get_my_fib.json()
