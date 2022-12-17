sid = "short  21"
OBJECT_TYPE_GROUP = "short  0"
OBJECT_TYPE_LINE = "short  1"
OBJECT_TYPE_RECTANGLE = "short  2"
OBJECT_TYPE_OVAL = "short  3"
OBJECT_TYPE_ARC = "short  4"
OBJECT_TYPE_CHART = "short  5"
OBJECT_TYPE_TEXT = "short  6"
OBJECT_TYPE_BUTTON = "short  7"
OBJECT_TYPE_PICTURE = "short  8"
OBJECT_TYPE_POLYGON = "short  9"
OBJECT_TYPE_RESERVED1 = "short  10"
OBJECT_TYPE_CHECKBOX = "short  11"
OBJECT_TYPE_OPTION_BUTTON = "short  12"
OBJECT_TYPE_EDIT_BOX = "short  13"
OBJECT_TYPE_LABEL = "short  14"
OBJECT_TYPE_DIALOG_BOX = "short  15"
OBJECT_TYPE_SPINNER = "short  16"
OBJECT_TYPE_SCROLL_BAR = "short  17"
OBJECT_TYPE_LIST_BOX = "short  18"
OBJECT_TYPE_GROUP_BOX = "short  19"
OBJECT_TYPE_COMBO_BOX = "short  20"
OBJECT_TYPE_RESERVED2 = "short  21"
OBJECT_TYPE_RESERVED3 = "short  22"
OBJECT_TYPE_RESERVED4 = "short  23"
OBJECT_TYPE_RESERVED5 = "short  24"
OBJECT_TYPE_COMMENT = "short  25"
OBJECT_TYPE_RESERVED6 = "short  26"
OBJECT_TYPE_RESERVED7 = "short  27"
OBJECT_TYPE_RESERVED8 = "short  28"
OBJECT_TYPE_RESERVED9 = "short  29"
OBJECT_TYPE_MICROSOFT_OFFICE_DRAWING = "short  30"
def ():
    '''returns CommonObjectDataSubRecord\n\n
    ()\n
    (final LittleEndianInput in, final int size)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def clone():
    '''returns CommonObjectDataSubRecord\n\n
    clone()\n
    '''
def getObjectType():
    '''returns short\n\n
    getObjectType()\n
    '''
def setObjectType():
    '''returns None\n\n
    setObjectType(final short field_1_objectType)\n
    '''
def getObjectId():
    '''returns int\n\n
    getObjectId()\n
    '''
def setObjectId():
    '''returns None\n\n
    setObjectId(final int field_2_objectId)\n
    '''
def getOption():
    '''returns short\n\n
    getOption()\n
    '''
def setOption():
    '''returns None\n\n
    setOption(final short field_3_option)\n
    '''
def getReserved1():
    '''returns int\n\n
    getReserved1()\n
    '''
def setReserved1():
    '''returns None\n\n
    setReserved1(final int field_4_reserved1)\n
    '''
def getReserved2():
    '''returns int\n\n
    getReserved2()\n
    '''
def setReserved2():
    '''returns None\n\n
    setReserved2(final int field_5_reserved2)\n
    '''
def getReserved3():
    '''returns int\n\n
    getReserved3()\n
    '''
def setReserved3():
    '''returns None\n\n
    setReserved3(final int field_6_reserved3)\n
    '''
def setLocked():
    '''returns None\n\n
    setLocked(final boolean value)\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked()\n
    '''
def setPrintable():
    '''returns None\n\n
    setPrintable(final boolean value)\n
    '''
def isPrintable():
    '''returns boolean\n\n
    isPrintable()\n
    '''
def setAutofill():
    '''returns None\n\n
    setAutofill(final boolean value)\n
    '''
def isAutofill():
    '''returns boolean\n\n
    isAutofill()\n
    '''
def setAutoline():
    '''returns None\n\n
    setAutoline(final boolean value)\n
    '''
def isAutoline():
    '''returns boolean\n\n
    isAutoline()\n
    '''
