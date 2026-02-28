from datetime import datetime, timezone, timedelta

def parse_datetime(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    tz = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=tz)

dt1 = parse_datetime(input())
dt2 = parse_datetime(input())

diff_seconds = abs((dt1 - dt2).total_seconds())
days = int(diff_seconds // 86400)
print(days)