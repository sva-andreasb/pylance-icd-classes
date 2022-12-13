def readFrom():
'''public static DateTimeZone readFrom(final InputStream in, final String s)
public static DateTimeZone readFrom(final DataInput dataInput, final String s)
'''
pass
def DateTimeZoneBuilder():
'''public DateTimeZoneBuilder()
'''
pass
def addCutover():
'''public DateTimeZoneBuilder addCutover(final int n, final char c, final int n2, final int n3, final int n4, final boolean b, final int n5)
'''
pass
def setStandardOffset():
'''public DateTimeZoneBuilder setStandardOffset(final int standardOffset)
public void setStandardOffset(final int iStandardOffset)
'''
pass
def setFixedSavings():
'''public DateTimeZoneBuilder setFixedSavings(final String s, final int n)
public void setFixedSavings(final String iInitialNameKey, final int iInitialSaveMillis)
'''
pass
def addRecurringSavings():
'''public DateTimeZoneBuilder addRecurringSavings(final String s, final int n, final int n2, final int n3, final char c, final int n4, final int n5, final int n6, final boolean b, final int n7)
'''
pass
def toDateTimeZone():
'''public DateTimeZone toDateTimeZone(final String s, final boolean b)
'''
pass
def writeTo():
'''public void writeTo(final String s, final OutputStream out)
public void writeTo(final String s, final DataOutput dataOutput)
public void writeTo(final DataOutput dataOutput)
public void writeTo(final DataOutput dataOutput)
public void writeTo(final DataOutput dataOutput)
public void writeTo(final DataOutput dataOutput)
'''
pass
def setInstant():
'''public long setInstant(final int n, final int n2, final int n3)
'''
pass
def next():
'''public long next(long n, final int n2, final int n3)
public long next(final long n, final int n2, final int n3)
public long next(final long n, final int n2, final int n3)
'''
pass
def previous():
'''public long previous(long n, final int n2, final int n3)
public long previous(final long n, final int n2, final int n3)
'''
pass
def equals():
'''public boolean equals(final Object o)
public boolean equals(final Object o)
public boolean equals(final Object o)
public boolean equals(final Object o)
'''
pass
def getOfYear():
'''public OfYear getOfYear()
public OfYear getOfYear()
'''
pass
def getNameKey():
'''public String getNameKey()
public String getNameKey()
public String getNameKey()
public String getNameKey(final long n)
public String getNameKey(final long key)
'''
pass
def getSaveMillis():
'''public int getSaveMillis()
public int getSaveMillis()
public int getSaveMillis()
'''
pass
def getFromYear():
'''public int getFromYear()
'''
pass
def getToYear():
'''public int getToYear()
'''
pass
def getMillis():
'''public long getMillis()
'''
pass
def getWallOffset():
'''public int getWallOffset()
'''
pass
def getStandardOffset():
'''public int getStandardOffset()
public int getStandardOffset()
public int getStandardOffset(final long n)
public int getStandardOffset(final long key)
'''
pass
def isTransitionFrom():
'''public boolean isTransitionFrom(final Transition transition)
'''
pass
def addRule():
'''public void addRule(final Rule rule)
'''
pass
def setUpperLimit():
'''public void setUpperLimit(final int iUpperYear, final OfYear iUpperOfYear)
'''
pass
def firstTransition():
'''public Transition firstTransition(final long n)
'''
pass
def nextTransition():
'''public Transition nextTransition(final long n, final int n2)
public long nextTransition(final long n)
public long nextTransition(long key)
'''
pass
def getUpperLimit():
'''public long getUpperLimit(final int n)
'''
pass
def buildTailZone():
'''public DSTZone buildTailZone(final String s)
'''
pass
def getOffset():
'''public int getOffset(final long n)
public int getOffset(final long key)
'''
pass
def isFixed():
'''public boolean isFixed()
public boolean isFixed()
'''
pass
def previousTransition():
'''public long previousTransition(long n)
public long previousTransition(final long key)
'''
pass
def isCachable():
'''public boolean isCachable()
'''
pass
