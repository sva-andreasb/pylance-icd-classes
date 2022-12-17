SUBSCRIPTION_BOTH = "String  \"both\""
SUBSCRIPTION_TO = "String  \"to\""
SUBSCRIPTION_FROM = "String  \"from\""
SUBSCRIPTION_NONE = "String  \"none\""
def ():
    '''returns PrivacyItem\n\n
    (final boolean allow, final long order)\n
    (final Type type, final String value, final boolean allow, final long order)\n
    (final Type type, final CharSequence value, final boolean allow, final long order)\n
    '''
def isAllow():
    '''returns boolean\n\n
    isAllow()\n
    '''
def isFilterIQ():
    '''returns boolean\n\n
    isFilterIQ()\n
    '''
def setFilterIQ():
    '''returns None\n\n
    setFilterIQ(final boolean filterIQ)\n
    '''
def isFilterMessage():
    '''returns boolean\n\n
    isFilterMessage()\n
    '''
def setFilterMessage():
    '''returns None\n\n
    setFilterMessage(final boolean filterMessage)\n
    '''
def isFilterPresenceIn():
    '''returns boolean\n\n
    isFilterPresenceIn()\n
    '''
def setFilterPresenceIn():
    '''returns None\n\n
    setFilterPresenceIn(final boolean filterPresenceIn)\n
    '''
def isFilterPresenceOut():
    '''returns boolean\n\n
    isFilterPresenceOut()\n
    '''
def setFilterPresenceOut():
    '''returns None\n\n
    setFilterPresenceOut(final boolean filterPresenceOut)\n
    '''
def getOrder():
    '''returns long\n\n
    getOrder()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def isFilterEverything():
    '''returns boolean\n\n
    isFilterEverything()\n
    '''
def toXML():
    '''returns String\n\n
    toXML()\n
    '''
