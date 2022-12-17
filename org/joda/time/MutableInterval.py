def ():
    '''returns MutableInterval\n\n
    ()\n
    (final long n, final long n2)\n
    (final long n, final long n2, final Chronology chronology)\n
    (final ReadableInstant readableInstant, final ReadableInstant readableInstant2)\n
    (final ReadableInstant readableInstant, final ReadableDuration readableDuration)\n
    (final ReadableDuration readableDuration, final ReadableInstant readableInstant)\n
    (final ReadableInstant readableInstant, final ReadablePeriod readablePeriod)\n
    (final ReadablePeriod readablePeriod, final ReadableInstant readableInstant)\n
    (final Object o)\n
    (final Object o, final Chronology chronology)\n
    '''
def setInterval():
    '''returns None\n\n
    setInterval(final long n, final long n2)\n
    setInterval(final ReadableInterval readableInterval)\n
    setInterval(final ReadableInstant readableInstant, final ReadableInstant readableInstant2)\n
    '''
def setChronology():
    '''returns None\n\n
    setChronology(final Chronology chronology)\n
    '''
def setStartMillis():
    '''returns None\n\n
    setStartMillis(final long n)\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final ReadableInstant readableInstant)\n
    '''
def setEndMillis():
    '''returns None\n\n
    setEndMillis(final long n)\n
    '''
def setEnd():
    '''returns None\n\n
    setEnd(final ReadableInstant readableInstant)\n
    '''
def setDurationAfterStart():
    '''returns None\n\n
    setDurationAfterStart(final long n)\n
    setDurationAfterStart(final ReadableDuration readableDuration)\n
    '''
def setDurationBeforeEnd():
    '''returns None\n\n
    setDurationBeforeEnd(final long n)\n
    setDurationBeforeEnd(final ReadableDuration readableDuration)\n
    '''
def setPeriodAfterStart():
    '''returns None\n\n
    setPeriodAfterStart(final ReadablePeriod readablePeriod)\n
    '''
def setPeriodBeforeEnd():
    '''returns None\n\n
    setPeriodBeforeEnd(final ReadablePeriod readablePeriod)\n
    '''
def copy():
    '''returns MutableInterval\n\n
    copy()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
