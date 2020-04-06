import datetime, pytz
d1 = datetime.datetime.now()
d3 = datetime.datetime.now().day
sourceTimezone = pytz.timezone('US/Hawaii')
z = int(input("days away: "))
x = int(input("Hour(24h): "))
y = int(input("Minutes(60): "))
d2 = d1.replace(day=(d3)+(z),hour=(x),minute=(y),second=0,microsecond=0)
hawaii = sourceTimezone.localize(d2)
pacific = pytz.timezone ('America/Los_Angeles')
mountain = pytz.timezone ('America/Denver')
central = pytz.timezone ('America/Chicago')
eastern = pytz.timezone ('America/New_York')
london = pytz.timezone ('Europe/London')
centralEurope = pytz.timezone ('Europe/Paris')
tokyo = pytz.timezone ('Asia/Tokyo')
sydney = pytz.timezone ('Australia/Sydney')
nextPacific = hawaii.astimezone(pacific)
nextMountain = hawaii.astimezone(mountain)
nextCentral = hawaii.astimezone(central)
nextEastern = hawaii.astimezone(eastern)
nextLondon = hawaii.astimezone(london)
nextCentralEurope = hawaii.astimezone(centralEurope)
nextTokyo = hawaii.astimezone(tokyo)
nextSydney = hawaii.astimezone(sydney)
print (
    f"{'Pacific:':<15} {nextPacific.strftime('%D %I:%M:%S %p'):>20}",
    #f"\n{'Mountain:':<15} {nextMountain.strftime('%D %I:%M:%S %p'):>20}",
    #f"\n{'Central:':<15} {nextCentral.strftime('%D %I:%M:%S %p'):>20}",
    f"\n{'Eastern:':<15} {nextEastern.strftime('%D %I:%M:%S %p'):>20}",
    f"\n{'London:':<15} {nextLondon.strftime('%D %I:%M:%S %p'):>20}",
    f"\n{'CentralEurope:':<15} {nextCentralEurope.strftime('%D %I:%M:%S %p'):>20}",
    f"\n{'Tokyo:':<15} {nextTokyo.strftime('%D %I:%M:%S %p'):>20}",
    f"\n{'Sydney:':<15} {nextSydney.strftime('%D %I:%M:%S %p'):>20}",
    )
input('Press ENTER to exit')
