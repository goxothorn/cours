import json, os, requests, configparser, time, math, pickle, hashlib, sys, getopt

class Tme_perso:


    def __init__(self):
        self.time2 = time.localtime()

        def timeLocal():

            def name_w_day(w_day):
                if w_day == 1:
                    name = "Mon"
                elif w_day == 2:
                    name = "Tue"
                elif w_day == 3:
                    name = "Wed"
                elif w_day == 4:
                    name = "Thu"
                elif w_day == 5:
                    name = "Fri"
                elif w_day == 6:
                    name = "Sat"
                elif w_day == 7:
                    name = "Sun"
                return name

            def date_yesterday(mth, day):
                if day != 1:
                    yday = day - 1
                elif day == 1 and (mth == 1 or mth == 2 or mth == 4 or mth == 6 or mth == 8 or mth == 9 or mth == 11):
                    yday = 31
                elif day == 1 and (mth == 5 or mth == 7 or mth == 10 or mth == 12):
                    yday = 30
                elif day == 1 and mth == 3:
                    yday = 28

                if day == 1 and mth !=1:
                    ymth = mth-1
                elif day == 1 and mth == 1:
                    ymth = 12
                else:
                    ymth = mth
                yesterday = {"y_month": ymth, "y_day": yday }
                return yesterday

            def minute(mn):
                if mn < 10:
                    name = "0{}".format(mn)
                else:
                    name = mn
                return name

            def dictTime (w_day, dy, mth, yer, hr, mn2, n_w_day, nameTime, yday, ymth):
                argtimeList= [w_day, dy, mth, yer, hr, mn2, n_w_day, nameTime, yday, ymth]
                argNameList= ["week_day", "day", "month", "year", "hour", "minute", "name_week_day", "Time_in_string", "day_yesterday", "month_yesterday"]
                dico = {}
                i=0
                for param in argtimeList:
                    dico["{}".format(argNameList[i])] = param
                    i+=1
                return dico

            tme = time.localtime()
            w_day = tme.tm_wday + 1
            dy = tme.tm_mday
            mth = tme.tm_mon
            yer = tme.tm_year
            hr = tme.tm_hour
            mn = tme.tm_min
            sc = tme.tm_sec
            n_w_day = name_w_day(w_day)
            mn2 = minute(mn)
            yesterday = date_yesterday(mth, dy)
            yday = yesterday["y_day"]
            ymth = yesterday ["y_month"]
            nameTime = "{}__{}_{}_{}__{}{}".format(n_w_day, dy, mth, yer, hr, mn2)
            dicoT = dictTime(w_day, dy, mth, yer, hr, mn2, n_w_day, nameTime, yday, ymth)
            return dicoT

        self.time = timeLocal()
        self.hour = self.time["hour"]
        self.day_n = self.time["day"]
        self.day_s = self.time ["name_week_day"]
        self.month = self.time["month"]
        self.year = self.time["year"]
        self.minute = self.time["minute"]
        self.time_name = self.time["Time_in_string"]
        self.yday = self.time["day_yesterday"]
        self.ymonth = self.time["month_yesterday"]


test = Tme_perso()

