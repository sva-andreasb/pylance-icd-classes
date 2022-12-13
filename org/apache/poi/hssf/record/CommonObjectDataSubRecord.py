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
def CommonObjectDataSubRecord():
    '''public CommonObjectDataSubRecord()
    public CommonObjectDataSubRecord(final LittleEndianInput in, final int size)
    '''
def toString():
    '''public String toString()
    '''
def serialize():
    '''public void serialize(final LittleEndianOutput out)
    '''
def getSid():
    '''public short getSid()
    '''
def clone():
    '''public CommonObjectDataSubRecord clone()
    '''
def getObjectType():
    '''public short getObjectType()
    '''
def setObjectType():
    '''public void setObjectType(final short field_1_objectType)
    '''
def getObjectId():
    '''public int getObjectId()
    '''
def setObjectId():
    '''public void setObjectId(final int field_2_objectId)
    '''
def getOption():
    '''public short getOption()
    '''
def setOption():
    '''public void setOption(final short field_3_option)
    '''
def getReserved1():
    '''public int getReserved1()
    '''
def setReserved1():
    '''public void setReserved1(final int field_4_reserved1)
    '''
def getReserved2():
    '''public int getReserved2()
    '''
def setReserved2():
    '''public void setReserved2(final int field_5_reserved2)
    '''
def getReserved3():
    '''public int getReserved3()
    '''
def setReserved3():
    '''public void setReserved3(final int field_6_reserved3)
    '''
def setLocked():
    '''public void setLocked(final boolean value)
    '''
def isLocked():
    '''public boolean isLocked()
    '''
def setPrintable():
    '''public void setPrintable(final boolean value)
    '''
def isPrintable():
    '''public boolean isPrintable()
    '''
def setAutofill():
    '''public void setAutofill(final boolean value)
    '''
def isAutofill():
    '''public boolean isAutofill()
    '''
def setAutoline():
    '''public void setAutoline(final boolean value)
    '''
def isAutoline():
    '''public boolean isAutoline()
    '''
