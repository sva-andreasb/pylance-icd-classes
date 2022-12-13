def DateRange():
'''public DateRange(final Range<Date> range)
public DateRange(final Date start, final Date end)
public DateRange()
'''
pass
def intersects():
'''public boolean intersects(final Date clickdate)
public boolean intersects(final Range<Date> date)
'''
pass
def before():
'''public boolean before(final Date date)
public boolean before(final Range<Date> date)
'''
pass
def after():
'''public boolean after(final Date d)
public boolean after(final Range<Date> date)
'''
pass
def normalize():
'''public void normalize()
public void normalize(final DateRange dates)
'''
pass
def ensureRange():
'''public void ensureRange(final DateRange range)
'''
pass
def expandRange():
'''public void expandRange(final int days)
public void expandRange(final int days, final DateRange other)
'''
pass
def expandStart():
'''public void expandStart(final int days)
public void expandStart(final int days, final DateRange other)
'''
pass
def expandEnd():
'''public void expandEnd(final int days)
public void expandEnd(final int days, final DateRange other)
'''
pass
def getDurationInMillis():
'''public long getDurationInMillis()
'''
pass
def asRange():
'''public Range<Date> asRange()
'''
pass
def asDateRange():
'''public static DateRange asDateRange(final Range<Date> range)
'''
pass
def compareTo():
'''public int compareTo(final DateRange o)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def toString():
'''public String toString()
'''
pass
