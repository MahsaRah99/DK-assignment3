#!/usr/bin/python3
# HW3_Q4_HAPPY BIRTHDAY
"""
seconds_since_bd function: calcules the seconds since a special date
hbd_beforehand function  : counts days and minutes tii a special date
Shamsi_bday function     : converts gregorian birthdate to Jalali birthdate
"""
import jdatetime
import datetime as dtm

def seconds_since_bd(b_date:str, b_time:str)-> str:
    """
    Args:
        b_date (str): input birth date
        b_time (str): input birth time

    Returns:
        str: a message that tells totall 
        seconds past from your birth till right now.
    """
    try:
        day, mon, year = map(int,b_date.split('/'))
        hr, min, sec  = map(int,b_time.split(':')) 
        birth_dt = dtm.datetime(year,mon,day,hr,min,sec) 
        
    except ValueError:
        return "you've entered an invalid date or time"
    
    right_now  = dtm.datetime.now()
    
    if birth_dt > right_now:
        return "you can't be from future! :)"
    
    diff = (right_now - birth_dt).total_seconds()
    return f"{int(diff)} seconds have passed since you were born!"

def hbd_beforehand(b_date:str,b_time:str)->str:
    """
    Args:
        b_date (str): input birth date
        b_time (str): input birth time

    Returns:
        str: a message that tells how 
        many days and minutes has left untill
        your next birthday.
    """

    now  = dtm.datetime.now()
    try:
        day, mon, year = map(int,b_date.split('/')) 
        hr, min, sec  = map(int,b_time.split(':')) 
        date1 = dtm.datetime(now.year, mon, day, hr, min, sec)
        date2 = dtm.datetime(now.year+1, mon, day, hr, min, sec)
        
    except ValueError:
        return "you've entered an invalid date or time"
    
    if date1 > now:
        d = (date1 - now).days
        m = ((date1 - now).seconds//60)
        return f"{d} days and {m} minutes till your next birthay!"
    else:
        d2 = (date2 - now).days
        m2 = ((date2 - now).seconds//60)
        return f"{d2} days and {m2} minutes till your next birthay!"


def Shamsi_bday(b_date:str)-> jdatetime.date:
    """
    Args:
        b_date (str): your gregorian birth date

    Returns:
        jdatetime.date: your Shamsi birth date
    """
    try:
        d, m, y = map(int,b_date.split('/'))
        jalali = jdatetime.date.fromgregorian(day=d, month=m, year=y)
    except ValueError:
        return "you've entered an invalid birthdate"
    except IndexError:
        return "months should be:[1,12] and days should be: [1,31]"
    
    jd,jm,jy = jalali.day,jalali.month,jalali.year
    then = jdatetime.datetime(jy,jm,jd)
    if  then > jdatetime.datetime.now():
        return "you can't be from future! :)"
    
    return jalali


def main():  
    bd_date = input("Enter your birth date (DD/MM/YYYY) : ")
    bd_time = input("Enter your birth time (hh:mm:ss) : ")
    print(seconds_since_bd(bd_date,bd_time))
    print(hbd_beforehand(bd_date,bd_time))
    print(Shamsi_bday(bd_date))
    
    
    
if __name__ == "__main__":
    main()
