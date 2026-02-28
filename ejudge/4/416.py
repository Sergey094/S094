from datetime import datetime, timezone, timedelta

def parse_dt(s):
    dt_str, tz_str = s.rsplit(' ', 1)
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_str[3] == '+' else -1
    h, m = int(tz_str[4:6]), int(tz_str[7:9])
    tz = timezone(timedelta(hours=sign*h, minutes=sign*m))
    return dt.replace(tzinfo=tz)

start = parse_dt(input())
end = parse_dt(input())

duration = int((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds())
print(duration)