from django.shortcuts import render
import datetime, pytz
# Create your views here.
def index(request):
    startDate = datetime.date(2020, 9, 27).isocalendar()[1]
    startDate2 = datetime.date(2021, 2, 21).isocalendar()[1]
    tz = pytz.timezone('Europe/Bucharest')
    now = datetime.datetime.now(tz)
    year, week, day = now.isocalendar()
    if year == 2020:
        uniWeek = week-startDate
    elif year == 2021 and week >=8:
        uniWeek = week - startDate2
    else:
        if week <= 2:
            uniWeek = 12 + week
        else:
            uniWeek = "exam session"
    return render(request, "fom/index.html", {
        "newyear": uniWeek})