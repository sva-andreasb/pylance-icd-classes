def DateRange():
    '''public DateRange(final Range<Date> range)
    public DateRange(final Date start, final Date end)
    public DateRange()
    '''
def intersects():
    '''public boolean intersects(final Date clickdate)
    public boolean intersects(final Range<Date> date)
    '''
def before():
    '''public boolean before(final Date date)
    public boolean before(final Range<Date> date)
    '''
def after():
    '''public boolean after(final Date d)
    public boolean after(final Range<Date> date)
    '''
def normalize():
    '''public void normalize()
    public void normalize(final DateRange dates)
    '''
def ensureRange():
    '''public void ensureRange(final DateRange range)
    '''
def expandRange():
    '''public void expandRange(final int days)
    public void expandRange(final int days, final DateRange other)
    '''
def expandStart():
    '''public void expandStart(final int days)
    public void expandStart(final int days, final DateRange other)
    '''
def expandEnd():
    '''public void expandEnd(final int days)
    public void expandEnd(final int days, final DateRange other)
    '''
def getDurationInMillis():
    '''public long getDurationInMillis()
    '''
def asRange():
    '''public Range<Date> asRange()
    '''
def asDateRange():
    '''public static DateRange asDateRange(final Range<Date> range)
    '''
def compareTo():
    '''public int compareTo(final DateRange o)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def toString():
    '''public String toString()
    '''
