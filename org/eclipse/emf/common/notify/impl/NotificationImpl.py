PRIMITIVE_TYPE_OBJECT = "int  -1"
PRIMITIVE_TYPE_BOOLEAN = "int  0"
PRIMITIVE_TYPE_BYTE = "int  1"
PRIMITIVE_TYPE_CHAR = "int  2"
PRIMITIVE_TYPE_DOUBLE = "int  3"
PRIMITIVE_TYPE_FLOAT = "int  4"
PRIMITIVE_TYPE_INT = "int  5"
PRIMITIVE_TYPE_LONG = "int  6"
PRIMITIVE_TYPE_SHORT = "int  7"
def ():
    '''returns NotificationImpl\n\n
    (final int eventType, final Object oldValue, final Object newValue)\n
    (final int eventType, final Object oldValue, final Object newValue, final boolean isSetChange)\n
    (final int eventType, final Object oldValue, final Object newValue, final int position)\n
    (final int eventType, final Object oldValue, final Object newValue, final int position, final boolean wasSet)\n
    (final int eventType, final boolean oldBooleanValue, final boolean newBooleanValue, final boolean isSetChange)\n
    (final int eventType, final boolean oldBooleanValue, final boolean newBooleanValue)\n
    (final int eventType, final byte oldByteValue, final byte newByteValue, final boolean isSetChange)\n
    (final int eventType, final byte oldByteValue, final byte newByteValue)\n
    (final int eventType, final char oldCharValue, final char newCharValue, final boolean isSetChange)\n
    (final int eventType, final char oldCharValue, final char newCharValue)\n
    (final int eventType, final double oldDoubleValue, final double newDoubleValue, final boolean isSetChange)\n
    (final int eventType, final double oldDoubleValue, final double newDoubleValue)\n
    (final int eventType, final float oldFloatValue, final float newFloatValue, final boolean isSetChange)\n
    (final int eventType, final float oldFloatValue, final float newFloatValue)\n
    (final int eventType, final int oldIntValue, final int newIntValue, final boolean isSetChange)\n
    (final int eventType, final int oldIntValue, final int newIntValue)\n
    (final int eventType, final long oldLongValue, final long newLongValue, final boolean isSetChange)\n
    (final int eventType, final long oldLongValue, final long newLongValue)\n
    (final int eventType, final short oldShortValue, final short newShortValue, final boolean isSetChange)\n
    (final int eventType, final short oldShortValue, final short newShortValue)\n
    '''
def getNotifier():
    '''returns Object\n\n
    getNotifier()\n
    '''
def getEventType():
    '''returns int\n\n
    getEventType()\n
    '''
def getFeature():
    '''returns Object\n\n
    getFeature()\n
    '''
def getFeatureID():
    '''returns int\n\n
    getFeatureID(final Class expectedClass)\n
    '''
def getOldValue():
    '''returns Object\n\n
    getOldValue()\n
    '''
def getNewValue():
    '''returns Object\n\n
    getNewValue()\n
    '''
def isTouch():
    '''returns boolean\n\n
    isTouch()\n
    '''
def isReset():
    '''returns boolean\n\n
    isReset()\n
    '''
def wasSet():
    '''returns boolean\n\n
    wasSet()\n
    '''
def getPosition():
    '''returns int\n\n
    getPosition()\n
    '''
def merge():
    '''returns boolean\n\n
    merge(final Notification notification)\n
    '''
def getOldBooleanValue():
    '''returns boolean\n\n
    getOldBooleanValue()\n
    '''
def getNewBooleanValue():
    '''returns boolean\n\n
    getNewBooleanValue()\n
    '''
def getOldByteValue():
    '''returns byte\n\n
    getOldByteValue()\n
    '''
def getNewByteValue():
    '''returns byte\n\n
    getNewByteValue()\n
    '''
def getOldCharValue():
    '''returns char\n\n
    getOldCharValue()\n
    '''
def getNewCharValue():
    '''returns char\n\n
    getNewCharValue()\n
    '''
def getOldDoubleValue():
    '''returns double\n\n
    getOldDoubleValue()\n
    '''
def getNewDoubleValue():
    '''returns double\n\n
    getNewDoubleValue()\n
    '''
def getOldFloatValue():
    '''returns float\n\n
    getOldFloatValue()\n
    '''
def getNewFloatValue():
    '''returns float\n\n
    getNewFloatValue()\n
    '''
def getOldIntValue():
    '''returns int\n\n
    getOldIntValue()\n
    '''
def getNewIntValue():
    '''returns int\n\n
    getNewIntValue()\n
    '''
def getOldLongValue():
    '''returns long\n\n
    getOldLongValue()\n
    '''
def getNewLongValue():
    '''returns long\n\n
    getNewLongValue()\n
    '''
def getOldShortValue():
    '''returns short\n\n
    getOldShortValue()\n
    '''
def getNewShortValue():
    '''returns short\n\n
    getNewShortValue()\n
    '''
def getOldStringValue():
    '''returns String\n\n
    getOldStringValue()\n
    '''
def getNewStringValue():
    '''returns String\n\n
    getNewStringValue()\n
    '''
def add():
    '''returns boolean\n\n
    add(final Notification newNotification)\n
    '''
def dispatch():
    '''returns None\n\n
    dispatch()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
