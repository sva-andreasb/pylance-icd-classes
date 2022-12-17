def ():
    '''returns Interval\n\n
    (final long n, final long n2)\n
    (final long n, final long n2, final DateTimeZone dateTimeZone)\n
    (final long n, final long n2, final Chronology chronology)\n
    (final ReadableInstant readableInstant, final ReadableInstant readableInstant2)\n
    (final ReadableInstant readableInstant, final ReadableDuration readableDuration)\n
    (final ReadableDuration readableDuration, final ReadableInstant readableInstant)\n
    (final ReadableInstant readableInstant, final ReadablePeriod readablePeriod)\n
    (final ReadablePeriod readablePeriod, final ReadableInstant readableInstant)\n
    (final Object o)\n
    (final Object o, final Chronology chronology)\n
    '''
def toInterval():
    '''returns Interval\n\n
    toInterval()\n
    '''
def overlap():
    '''returns Interval\n\n
    overlap(ReadableInterval readableInterval)\n
    '''
def gap():
    '''returns Interval\n\n
    gap(ReadableInterval readableInterval)\n
    '''
def abuts():
    '''returns boolean\n\n
    abuts(final ReadableInterval readableInterval)\n
    '''
def withChronology():
    '''returns Interval\n\n
    withChronology(final Chronology chronology)\n
    '''
def withStartMillis():
    '''returns Interval\n\n
    withStartMillis(final long n)\n
    '''
def withStart():
    '''returns Interval\n\n
    withStart(final ReadableInstant readableInstant)\n
    '''
def withEndMillis():
    '''returns Interval\n\n
    withEndMillis(final long n)\n
    '''
def withEnd():
    '''returns Interval\n\n
    withEnd(final ReadableInstant readableInstant)\n
    '''
def withDurationAfterStart():
    '''returns Interval\n\n
    withDurationAfterStart(final ReadableDuration readableDuration)\n
    '''
def withDurationBeforeEnd():
    '''returns Interval\n\n
    withDurationBeforeEnd(final ReadableDuration readableDuration)\n
    '''
def withPeriodAfterStart():
    '''returns Interval\n\n
    withPeriodAfterStart(final ReadablePeriod readablePeriod)\n
    '''
def withPeriodBeforeEnd():
    '''returns Interval\n\n
    withPeriodBeforeEnd(final ReadablePeriod readablePeriod)\n
    '''
