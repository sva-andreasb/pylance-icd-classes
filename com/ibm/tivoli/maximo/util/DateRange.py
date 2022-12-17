def ():
    '''returns DateRange\n\n
    (final Range<Date> range)\n
    (final Date start, final Date end)\n
    ()\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final Date clickdate)\n
    intersects(final Range<Date> date)\n
    '''
def before():
    '''returns boolean\n\n
    before(final Date date)\n
    before(final Range<Date> date)\n
    '''
def after():
    '''returns boolean\n\n
    after(final Date d)\n
    after(final Range<Date> date)\n
    '''
def normalize():
    '''returns None\n\n
    normalize()\n
    normalize(final DateRange dates)\n
    '''
def ensureRange():
    '''returns None\n\n
    ensureRange(final DateRange range)\n
    '''
def expandRange():
    '''returns None\n\n
    expandRange(final int days)\n
    expandRange(final int days, final DateRange other)\n
    '''
def expandStart():
    '''returns None\n\n
    expandStart(final int days)\n
    expandStart(final int days, final DateRange other)\n
    '''
def expandEnd():
    '''returns None\n\n
    expandEnd(final int days)\n
    expandEnd(final int days, final DateRange other)\n
    '''
def getDurationInMillis():
    '''returns long\n\n
    getDurationInMillis()\n
    '''
def asRange():
    '''returns Range<Date>\n\n
    asRange()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final DateRange o)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
