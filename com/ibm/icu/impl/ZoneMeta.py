HOUR = "String  hourFormat""
GMT = "String  gmtFormat""
REGION_FORMAT = "String  regionFormat""
FALLBACK_FORMAT = "String  fallbackFormat""
ZONE_STRINGS = "String  zoneStrings""
FORWARD_SLASH = "String  /""
def getAvailableIDs():
'''public static synchronized String[] getAvailableIDs(final String country)
public static synchronized String[] getAvailableIDs()
public static synchronized String[] getAvailableIDs(final int offset)
'''
pass
def countEquivalentIDs():
'''public static synchronized int countEquivalentIDs(final String id)
'''
pass
def getEquivalentID():
'''public static synchronized String getEquivalentID(final String id, final int index)
'''
pass
def getCanonicalSystemID():
'''public static String getCanonicalSystemID(final String tzid)
'''
pass
def getCanonicalCountry():
'''public static String getCanonicalCountry(final String tzid)
'''
pass
def getSingleCountry():
'''public static String getSingleCountry(final String tzid)
'''
pass
def getLocationFormat():
'''public static String getLocationFormat(final String tzid, String city, final ULocale locale)
'''
pass
def getTZLocalizationInfo():
'''public static String getTZLocalizationInfo(final ULocale locale, final String format)
'''
pass
def openOlsonResource():
'''public static UResourceBundle openOlsonResource(UResourceBundle top, final String id)
'''
pass
def getSystemTimeZone():
'''public static TimeZone getSystemTimeZone(final String id)
'''
pass
def getGMT():
'''public static TimeZone getGMT()
'''
pass
def getCustomTimeZone():
'''public static TimeZone getCustomTimeZone(final String id)
public static TimeZone getCustomTimeZone(final int offset)
'''
pass
def getCustomID():
'''public static String getCustomID(final String id)
'''
pass
def getMetazoneID():
'''public static String getMetazoneID(final String olsonID, final long date)
'''
pass
def getZoneIdByMetazone():
'''public static String getZoneIdByMetazone(final String metazoneID, final String region)
'''
pass
