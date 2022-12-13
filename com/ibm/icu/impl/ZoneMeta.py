HOUR = "String  \"hourFormat\""
GMT = "String  \"gmtFormat\""
REGION_FORMAT = "String  \"regionFormat\""
FALLBACK_FORMAT = "String  \"fallbackFormat\""
ZONE_STRINGS = "String  \"zoneStrings\""
FORWARD_SLASH = "String  \"/\""
def getAvailableIDs():
    '''public static synchronized String[] getAvailableIDs(final String country)
    public static synchronized String[] getAvailableIDs()
    public static synchronized String[] getAvailableIDs(final int offset)
    '''
def countEquivalentIDs():
    '''public static synchronized int countEquivalentIDs(final String id)
    '''
def getEquivalentID():
    '''public static synchronized String getEquivalentID(final String id, final int index)
    '''
def getCanonicalSystemID():
    '''public static String getCanonicalSystemID(final String tzid)
    '''
def getCanonicalCountry():
    '''public static String getCanonicalCountry(final String tzid)
    '''
def getSingleCountry():
    '''public static String getSingleCountry(final String tzid)
    '''
def getLocationFormat():
    '''public static String getLocationFormat(final String tzid, String city, final ULocale locale)
    '''
def getTZLocalizationInfo():
    '''public static String getTZLocalizationInfo(final ULocale locale, final String format)
    '''
def openOlsonResource():
    '''public static UResourceBundle openOlsonResource(UResourceBundle top, final String id)
    '''
def getSystemTimeZone():
    '''public static TimeZone getSystemTimeZone(final String id)
    '''
def getGMT():
    '''public static TimeZone getGMT()
    '''
def getCustomTimeZone():
    '''public static TimeZone getCustomTimeZone(final String id)
    public static TimeZone getCustomTimeZone(final int offset)
    '''
def getCustomID():
    '''public static String getCustomID(final String id)
    '''
def getMetazoneID():
    '''public static String getMetazoneID(final String olsonID, final long date)
    '''
def getZoneIdByMetazone():
    '''public static String getZoneIdByMetazone(final String metazoneID, final String region)
    '''
