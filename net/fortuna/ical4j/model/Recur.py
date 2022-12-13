SECONDLY = "String  \"SECONDLY\""
MINUTELY = "String  \"MINUTELY\""
HOURLY = "String  \"HOURLY\""
DAILY = "String  \"DAILY\""
WEEKLY = "String  \"WEEKLY\""
MONTHLY = "String  \"MONTHLY\""
YEARLY = "String  \"YEARLY\""
KEY_MAX_INCREMENT_COUNT = "String  \"net.fortuna.ical4j.recur.maxincrementcount\""
def Recur():
    '''public Recur(final String aValue)
    public Recur(final String frequency, final Date until)
    public Recur(final Frequency frequency, final Date until)
    public Recur(final String frequency, final int count)
    public Recur(final Frequency frequency, final int count)
    '''
def getDayList():
    '''public final WeekDayList getDayList()
    '''
def getHourList():
    '''public final NumberList getHourList()
    '''
def getMinuteList():
    '''public final NumberList getMinuteList()
    '''
def getMonthDayList():
    '''public final NumberList getMonthDayList()
    '''
def getMonthList():
    '''public final NumberList getMonthList()
    '''
def getSecondList():
    '''public final NumberList getSecondList()
    '''
def getSetPosList():
    '''public final NumberList getSetPosList()
    '''
def getWeekNoList():
    '''public final NumberList getWeekNoList()
    '''
def getYearDayList():
    '''public final NumberList getYearDayList()
    '''
def getCount():
    '''public final int getCount()
    '''
def getExperimentalValues():
    '''public final Map<String, String> getExperimentalValues()
    '''
def getFrequency():
    '''public final Frequency getFrequency()
    '''
def getInterval():
    '''public final int getInterval()
    '''
def getUntil():
    '''public final Date getUntil()
    '''
def setWeekStartDay():
    '''public final void setWeekStartDay(final WeekDay.Day weekStartDay)
    '''
def toString():
    '''public final String toString()
    '''
def getDates():
    '''public final DateList getDates(final Date periodStart, final Date periodEnd, final Value value)
    public final DateList getDates(final Date seed, final Period period, final Value value)
    public final DateList getDates(final Date seed, final Date periodStart, final Date periodEnd, final Value value)
    public final DateList getDates(final Date seed, final Date periodStart, final Date periodEnd, final Value value, final int maxCount)
    '''
def getNextDate():
    '''public final Date getNextDate(final Date seed, final Date startDate)
    '''
def setCount():
    '''public final void setCount(final int count)
    '''
def setFrequency():
    '''public final void setFrequency(final String frequency)
    '''
def setInterval():
    '''public final void setInterval(final int interval)
    '''
def setUntil():
    '''public final void setUntil(final Date until)
    '''
def frequency():
    '''public Builder frequency(final Frequency frequency)
    '''
def until():
    '''public Builder until(final Date until)
    '''
def count():
    '''public Builder count(final Integer count)
    '''
def interval():
    '''public Builder interval(final Integer interval)
    '''
def secondList():
    '''public Builder secondList(final NumberList secondList)
    '''
def minuteList():
    '''public Builder minuteList(final NumberList minuteList)
    '''
def hourList():
    '''public Builder hourList(final NumberList hourList)
    '''
def dayList():
    '''public Builder dayList(final WeekDayList dayList)
    '''
def monthDayList():
    '''public Builder monthDayList(final NumberList monthDayList)
    '''
def yearDayList():
    '''public Builder yearDayList(final NumberList yearDayList)
    '''
def weekNoList():
    '''public Builder weekNoList(final NumberList weekNoList)
    '''
def monthList():
    '''public Builder monthList(final NumberList monthList)
    '''
def setPosList():
    '''public Builder setPosList(final NumberList setPosList)
    '''
def weekStartDay():
    '''public Builder weekStartDay(final WeekDay.Day weekStartDay)
    '''
def build():
    '''public Recur build()
    '''
