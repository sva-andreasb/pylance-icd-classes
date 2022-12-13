def parse():
    '''    public static MutableInterval parse(final String s)
    '''
def MutableInterval():
    '''    public MutableInterval()
    public MutableInterval(final long n, final long n2)
    public MutableInterval(final long n, final long n2, final Chronology chronology)
    public MutableInterval(final ReadableInstant readableInstant, final ReadableInstant readableInstant2)
    public MutableInterval(final ReadableInstant readableInstant, final ReadableDuration readableDuration)
    public MutableInterval(final ReadableDuration readableDuration, final ReadableInstant readableInstant)
    public MutableInterval(final ReadableInstant readableInstant, final ReadablePeriod readablePeriod)
    public MutableInterval(final ReadablePeriod readablePeriod, final ReadableInstant readableInstant)
    public MutableInterval(final Object o)
    public MutableInterval(final Object o, final Chronology chronology)
    '''
def setInterval():
    '''    public void setInterval(final long n, final long n2)
    public void setInterval(final ReadableInterval readableInterval)
    public void setInterval(final ReadableInstant readableInstant, final ReadableInstant readableInstant2)
    '''
def setChronology():
    '''    public void setChronology(final Chronology chronology)
    '''
def setStartMillis():
    '''    public void setStartMillis(final long n)
    '''
def setStart():
    '''    public void setStart(final ReadableInstant readableInstant)
    '''
def setEndMillis():
    '''    public void setEndMillis(final long n)
    '''
def setEnd():
    '''    public void setEnd(final ReadableInstant readableInstant)
    '''
def setDurationAfterStart():
    '''    public void setDurationAfterStart(final long n)
    public void setDurationAfterStart(final ReadableDuration readableDuration)
    '''
def setDurationBeforeEnd():
    '''    public void setDurationBeforeEnd(final long n)
    public void setDurationBeforeEnd(final ReadableDuration readableDuration)
    '''
def setPeriodAfterStart():
    '''    public void setPeriodAfterStart(final ReadablePeriod readablePeriod)
    '''
def setPeriodBeforeEnd():
    '''    public void setPeriodBeforeEnd(final ReadablePeriod readablePeriod)
    '''
def copy():
    '''    public MutableInterval copy()
    '''
def clone():
    '''    public Object clone()
    '''
