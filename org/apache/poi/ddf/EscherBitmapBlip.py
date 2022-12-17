RECORD_ID_JPEG = "short  -4067"
RECORD_ID_PNG = "short  -4066"
RECORD_ID_DIB = "short  -4065"
def ():
    '''returns EscherBitmapBlip\n\n
    ()\n
    '''
def fillFields():
    '''returns int\n\n
    fillFields(final byte[] data, final int offset, final EscherRecordFactory recordFactory)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data, final EscherSerializationListener listener)\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def getUID():
    '''returns byte[]\n\n
    getUID()\n
    '''
def setUID():
    '''returns None\n\n
    setUID(final byte[] field_1_UID)\n
    '''
def getMarker():
    '''returns byte\n\n
    getMarker()\n
    '''
def setMarker():
    '''returns None\n\n
    setMarker(final byte field_2_marker)\n
    '''
