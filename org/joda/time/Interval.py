def parse():
    '''public static Interval parse(final String s)
    '''
def Interval():
    '''public Interval(final long n, final long n2)
    public Interval(final long n, final long n2, final DateTimeZone dateTimeZone)
    public Interval(final long n, final long n2, final Chronology chronology)
    public Interval(final ReadableInstant readableInstant, final ReadableInstant readableInstant2)
    public Interval(final ReadableInstant readableInstant, final ReadableDuration readableDuration)
    public Interval(final ReadableDuration readableDuration, final ReadableInstant readableInstant)
    public Interval(final ReadableInstant readableInstant, final ReadablePeriod readablePeriod)
    public Interval(final ReadablePeriod readablePeriod, final ReadableInstant readableInstant)
    public Interval(final Object o)
    public Interval(final Object o, final Chronology chronology)
    '''
def toInterval():
    '''public Interval toInterval()
    '''
def overlap():
    '''public Interval overlap(ReadableInterval readableInterval)
    '''
def gap():
    '''public Interval gap(ReadableInterval readableInterval)
    '''
def abuts():
    '''public boolean abuts(final ReadableInterval readableInterval)
    '''
def withChronology():
    '''public Interval withChronology(final Chronology chronology)
    '''
def withStartMillis():
    '''public Interval withStartMillis(final long n)
    '''
def withStart():
    '''public Interval withStart(final ReadableInstant readableInstant)
    '''
def withEndMillis():
    '''public Interval withEndMillis(final long n)
    '''
def withEnd():
    '''public Interval withEnd(final ReadableInstant readableInstant)
    '''
def withDurationAfterStart():
    '''public Interval withDurationAfterStart(final ReadableDuration readableDuration)
    '''
def withDurationBeforeEnd():
    '''public Interval withDurationBeforeEnd(final ReadableDuration readableDuration)
    '''
def withPeriodAfterStart():
    '''public Interval withPeriodAfterStart(final ReadablePeriod readablePeriod)
    '''
def withPeriodBeforeEnd():
    '''public Interval withPeriodBeforeEnd(final ReadablePeriod readablePeriod)
    '''
