TIMEZONE_ICU = "int 0"
TIMEZONE_JDK = "int 1"
SHORT = "int 0"
LONG = "int 1"
SHORT_GENERIC = "int 2"
LONG_GENERIC = "int 3"
SHORT_GMT = "int 4"
LONG_GMT = "int 5"
SHORT_COMMONLY_USED = "int 6"
GENERIC_LOCATION = "int 7"
UNKNOWN_ZONE_ID = "String Etc/Unknown""
def TimeZone():
'''public TimeZone()
'''
pass
def getOffset():
'''public int getOffset(final long date)
public void getOffset(long date, final boolean local, final int[] offsets)
public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
'''
pass
def getID():
'''public String getID()
'''
pass
def setID():
'''public void setID(final String ID)
'''
pass
def getDisplayName():
'''public final String getDisplayName()
public final String getDisplayName(final Locale locale)
public final String getDisplayName(final ULocale locale)
public final String getDisplayName(final boolean daylight, final int style)
public String getDisplayName(final boolean daylight, final int style, final Locale locale)
public String getDisplayName(final boolean daylight, final int style, final ULocale locale)
'''
pass
def getDSTSavings():
'''public int getDSTSavings()
'''
pass
def observesDaylightTime():
'''public boolean observesDaylightTime()
'''
pass
def getTimeZone():
'''public static TimeZone getTimeZone(final String ID)
public static TimeZone getTimeZone(final String ID, final int type)
'''
pass
def getFrozenTimeZone():
'''public static TimeZone getFrozenTimeZone(final String ID)
'''
pass
def setDefaultTimeZoneType():
'''public static synchronized void setDefaultTimeZoneType(final int type)
'''
pass
def getDefaultTimeZoneType():
'''public static int getDefaultTimeZoneType()
'''
pass
def getAvailableIDs():
'''public static Set<String> getAvailableIDs(final SystemTimeZoneType zoneType, final String region, final Integer rawOffset)
public static String[] getAvailableIDs(final int rawOffset)
public static String[] getAvailableIDs(final String country)
public static String[] getAvailableIDs()
'''
pass
def countEquivalentIDs():
'''public static int countEquivalentIDs(final String id)
'''
pass
def getEquivalentID():
'''public static String getEquivalentID(final String id, final int index)
'''
pass
def getDefault():
'''public static TimeZone getDefault()
'''
pass
def setDefault():
'''public static synchronized void setDefault(final TimeZone tz)
'''
pass
def setICUDefault():
'''public static synchronized void setICUDefault(final TimeZone tz)
'''
pass
def hasSameRules():
'''public boolean hasSameRules(final TimeZone other)
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def getTZDataVersion():
'''public static String getTZDataVersion()
'''
pass
def getCanonicalID():
'''public static String getCanonicalID(final String id)
public static String getCanonicalID(final String id, final boolean[] isSystemID)
'''
pass
def getRegion():
'''public static String getRegion(final String id)
'''
pass
def getWindowsID():
'''public static String getWindowsID(String id)
'''
pass
def getIDForWindowsID():
'''public static String getIDForWindowsID(final String winid, final String region)
'''
pass
def isFrozen():
'''public boolean isFrozen()
public boolean isFrozen()
'''
pass
def freeze():
'''public TimeZone freeze()
public TimeZone freeze()
'''
pass
def cloneAsThawed():
'''public TimeZone cloneAsThawed()
public TimeZone cloneAsThawed()
'''
pass
def setRawOffset():
'''public void setRawOffset(final int offsetMillis)
'''
pass
def getRawOffset():
'''public int getRawOffset()
'''
pass
def useDaylightTime():
'''public boolean useDaylightTime()
'''
pass
def inDaylightTime():
'''public boolean inDaylightTime(final Date date)
'''
pass
