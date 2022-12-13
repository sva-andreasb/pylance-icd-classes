INCLUSIVE_START = "int  1"
INCLUSIVE_END = "int  2"
def DateRange():
    '''public DateRange(final Date start, final Date end)
    '''
def getRangeStart():
    '''public Date getRangeStart()
    '''
def getRangeEnd():
    '''public Date getRangeEnd()
    '''
def includes():
    '''public final boolean includes(final Date date)
    public final boolean includes(final Date date, final int inclusiveMask)
    '''
def before():
    '''public final boolean before(final DateRange range)
    '''
def after():
    '''public final boolean after(final DateRange range)
    '''
def intersects():
    '''public final boolean intersects(final DateRange range)
    '''
def adjacent():
    '''public final boolean adjacent(final DateRange range)
    '''
def contains():
    '''public final boolean contains(final DateRange range)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
