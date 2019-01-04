import json, os, requests, configparser, time, math, pickle, hashlib, sys, getopt
from time_perso import Tme_perso

url = "https://api.appnexus.com/"  # Pour test, URL non test= https://api.appnexus.com
url_auth = "{}{}".format(url, "auth")
userUrl = "{}{}".format(url, "user")
ReportURL = "{}{}".format(url, "report")
ReportCheckStatusURL = "{}{}".format(ReportURL, "?id=")
ReportDL_URL = "{}{}".format(ReportURL, "-download?id=")


##Check l'ordre pour auth ok et pas ok ici il semble que cela ne soit pas bon, sinon la fonction tourne
def CheckAuth(userUrl):
    tt = requests.get(userUrl)
    resp = json.loads(tt.content)
    if resp['response'].get('statut', False) == 'OK':
        print("authentification=OK")

    else:
        print("No authentification")
        return True


def Credidential():  ###Fonctionne, maintenant le système que j'utilise est moins flexible qu'un système avec
    username = input("User name")
    username = "{}".format(username)
    password = input("Password")
    password = "{}".format(password)
    Login = {
        "auth": {
            "username": username,
            "password": password
        }
    }
    return Login

def Credidential_2():  ###Fonctionne, maintenant le système que j'utilise est moins flexible qu'un système avec
    username =
    password =
    Login = {
        "auth": {
            "username": username,
            "password": password
        }
    }
    return Login

def CreateReport():
    ReportBackBone = {
        "report": {
            "report_type": "network_analytics",
            "report_interval": "last_48_hours",
            "columns": ["day", "imps", "clicks", "hour"],
            "filters": [{"geo_country": "BE"}],
            "orders": [{"order_by": "day", "direction": "ASC"}, {"order_by": "imps", "direction": "DESC"}],
            "format": "csv"
        }
    }
    return ReportBackBone


def C_Report_B_Deal_metric():
    tme = Tme_perso()
    today = tme.day_n
    month_today = tme.month
    yesterday = tme.yday
    month_yesterday = tme.ymonth
    ReportBackbone2 = {
        "report": {
            "report_type": "buyer_deal_metrics_report",
            "columns": [
                "day",
                "hour",
                "seller_member_name",
                "imps_matched",
                "deal_name",
                "deal_id",
                "start_date",
                "end_date",
                "bids",
                "imps_won",
                "reject_count",
            ],
            "filters": [{"deal_id": "521495"}],
            "start_date" : "2018-{}-{} 00:00:00".format(month_yesterday, yesterday),
            "end_date" : "2018-{}-{} 23:00:00".format(month_today, today),
            "orders": [{"order_by": "day", "direction": "ASC"}],
            "format": "csv"
        }
    }
    return ReportBackbone2


def ReportCheck(ReportCheckStatusURL, Report_ID, CookiesCo):
    ReportStatusID_URL = "{}{}".format(ReportCheckStatusURL, Report_ID)
    ReportCheckrequest = requests.get(ReportStatusID_URL, cookies=CookiesCo)
    ReportCheckrequest = json.loads(ReportCheckrequest.content)
    ReportCheckrequest = ReportCheckrequest["response"].get("execution_status")
    print(ReportCheckrequest)
    return ReportCheckrequest


#def ReportDownload(ReportDL_URL, Report_ID, CookiesCo):
#    ReportDLURL = "{}{}".format(ReportDL_URL, Report_ID)
#    Report_DL = requests.get(ReportDLURL, cookies=CookiesCo)
#    return Report_DL


def ReportDownload2(ReportDL_URL, Report_ID, CookiesCo):
    ReportDLURL = "{}{}".format(ReportDL_URL, Report_ID)

    retry = 0
    print("waiting for report generation")

    Report_DL = ""

    while retry < 10:
        report_ready = ReportCheck(ReportCheckStatusURL, Report_ID, CookiesCo)
        if report_ready == "ready":
            Report_DL = requests.get(ReportDLURL, cookies=CookiesCo)
            break
        else:
            time.sleep(5)
            retry += 1

    return Report_DL


def name_time ():
    tme = Tme_perso()
    nameTime = tme.time_name
    return nameTime

def name_w_day (w_day):
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

def date_day():
    tme = time.localtime()
    day ="{}".format(tme.tm_mday)
    return day

def date_yesterday():
    tme = time.localtime()
    day = tme.tm_mday
    mth = tme.tm_mon
    if day !=1:
        yday = day-1
    elif day == 1 and (mth == 1 or mth == 2 or mth == 4 or mth == 6 or mth == 8 or mth == 9 or mth == 11):
        yday = 31
    elif day == 1 and (mth == 5 or mth == 7 or mth == 10 or mth == 12):
        yday = 30
    elif day ==1 and mth == 3:
        yday = 28
    yday = "{}".format(yday)
    return yday

def heure_01 ():
    tme = time.localtime()
    hr = tme.tm_hour
    return hr


def SaveReport(DLReport):
    ReportName = \
        input("chose name for your report")
    Content = DLReport.content
    Report_Data = open("{}.csv".format(ReportName), "wb")
    Report_Data.write(Content)
    Report_Data.close()
    return Report_Data


def SaveReport_2(DLReport):
    ReportName = name_time()
    Content = DLReport.content
    Report_Data = open("{}.csv".format(ReportName), "wb")
    Report_Data.write(Content)
    Report_Data.close()
    return Report_Data

def boucleMain ():
    Logpayload = Credidential()
    Authrequest = requests.post(url_auth, data=json.dumps(Logpayload))
    CookiesCo = Authrequest.cookies
    ReportRequestPayload = C_Report_B_Deal_metric()
    Reportrequest = requests.post(ReportURL, cookies=CookiesCo, data=json.dumps(ReportRequestPayload))
    ContentReportRequest = json.loads(Reportrequest.content)
    Report_ID = ContentReportRequest["response"].get("report_id")
    DL1 = ReportDownload2(ReportDL_URL, Report_ID, CookiesCo)
    status = SaveReport_2(DL1)
    return status

tmeDebut = heure_01()
param_boucle_test = 0
main = boucleMain()
print (main)
tmeNow = heure_01()

while param_boucle_test<3:
    if tmeNow!= tmeDebut:
        main = boucleMain()
        print(main)
        print ("new report available for hour {}".format(tmeNow))
        param_boucle_test +=1
        tmeDebut = heure_01()
        tmeNow = heure_01()
    else:
        print ("waiting for 5 min")
        time.sleep(300)
        print("retry")
        tmeNow = heure_01()