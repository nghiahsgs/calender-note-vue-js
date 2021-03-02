import datetime
def nb_day_in_a_month(month,year):
      leap = 0
      if year% 400 == 0:
         leap = 1
      elif year % 100 == 0:
         leap = 0
      elif year% 4 == 0:
         leap = 1
      if month==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if month in list:
         return 31
      return 30

def gen_date_in_month(month,year):
    nb_days = nb_day_in_a_month(month,year)
    dayt_start = datetime.date(year, month, 1).weekday()+1
    

    L = []
    date_start = 1
    

    dayt = dayt_start-1
    date = date_start-1
    for day in range(0,nb_days):
        dayt += 1
        if dayt>6:
            dayt =0
        
        date += 1
        L.append({
            'dayt':dayt,
            'date':date,
            'events':[]
        })

    return L

if __name__=="__main__":
    month = 3
    year = 2021
    L = gen_date_in_month(month,year)
    print(L)