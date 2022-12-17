def ():
    '''returns ZoneStringFormat\n\n
    (final String[][] zoneStrings)\n
    '''
def getZoneStrings():
    '''returns String[][]\n\n
    getZoneStrings()\n
    '''
def getSpecificLongString():
    '''returns String\n\n
    getSpecificLongString(final Calendar cal)\n
    '''
def getSpecificShortString():
    '''returns String\n\n
    getSpecificShortString(final Calendar cal, final boolean commonlyUsedOnly)\n
    '''
def getGenericLongString():
    '''returns String\n\n
    getGenericLongString(final Calendar cal)\n
    '''
def getGenericShortString():
    '''returns String\n\n
    getGenericShortString(final Calendar cal, final boolean commonlyUsedOnly)\n
    '''
def getGenericLocationString():
    '''returns String\n\n
    getGenericLocationString(final Calendar cal)\n
    '''
def findSpecificLong():
    '''returns ZoneStringInfo\n\n
    findSpecificLong(final String text, final int start)\n
    '''
def findSpecificShort():
    '''returns ZoneStringInfo\n\n
    findSpecificShort(final String text, final int start)\n
    '''
def findGenericLong():
    '''returns ZoneStringInfo\n\n
    findGenericLong(final String text, final int start)\n
    '''
def findGenericShort():
    '''returns ZoneStringInfo\n\n
    findGenericShort(final String text, final int start)\n
    '''
def findGenericLocation():
    '''returns ZoneStringInfo\n\n
    findGenericLocation(final String text, final int start)\n
    '''
def getLongStandard():
    '''returns String\n\n
    getLongStandard(final String tzid, final long date)\n
    '''
def getLongDaylight():
    '''returns String\n\n
    getLongDaylight(final String tzid, final long date)\n
    '''
def getLongGenericNonLocation():
    '''returns String\n\n
    getLongGenericNonLocation(final String tzid, final long date)\n
    '''
def getLongGenericPartialLocation():
    '''returns String\n\n
    getLongGenericPartialLocation(final String tzid, final long date)\n
    '''
def getShortStandard():
    '''returns String\n\n
    getShortStandard(final String tzid, final long date, final boolean commonlyUsedOnly)\n
    '''
def getShortDaylight():
    '''returns String\n\n
    getShortDaylight(final String tzid, final long date, final boolean commonlyUsedOnly)\n
    '''
def getShortGenericNonLocation():
    '''returns String\n\n
    getShortGenericNonLocation(final String tzid, final long date, final boolean commonlyUsedOnly)\n
    '''
def getShortGenericPartialLocation():
    '''returns String\n\n
    getShortGenericPartialLocation(final String tzid, final long date, final boolean commonlyUsedOnly)\n
    '''
def getGenericLocation():
    '''returns String\n\n
    getGenericLocation(final String tzid)\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def getString():
    '''returns String\n\n
    getString()\n
    '''
def isStandard():
    '''returns boolean\n\n
    isStandard()\n
    '''
def isDaylight():
    '''returns boolean\n\n
    isDaylight()\n
    '''
def isGeneric():
    '''returns boolean\n\n
    isGeneric()\n
    '''
def handlePrefixMatch():
    '''returns boolean\n\n
    handlePrefixMatch(final int matchLength, final Iterator<ZoneStringInfo> values)\n
    '''
