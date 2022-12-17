def ():
    '''returns TIFFLZWDecoder\n\n
    (final int w, final int predictor, final int samplesPerPixel)\n
    '''
def decode():
    '''returns byte[]\n\n
    decode(final byte[] data, final byte[] uncompData, final int h)\n
    '''
def initializeStringTable():
    '''returns None\n\n
    initializeStringTable()\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final byte[] string)\n
    '''
def addStringToTable():
    '''returns None\n\n
    addStringToTable(final byte[] oldString, final byte newString)\n
    addStringToTable(final byte[] string)\n
    '''
def composeString():
    '''returns byte[]\n\n
    composeString(final byte[] oldString, final byte newString)\n
    '''
def getNextCode():
    '''returns int\n\n
    getNextCode()\n
    '''
