def ():
    '''returns PRStream\n\n
    (final PRStream stream, final PdfDictionary newDic)\n
    (final PRStream stream, final PdfDictionary newDic, final PdfReader reader)\n
    (final PdfReader reader, final int offset)\n
    (final PdfReader reader, final byte[] conts)\n
    '''
def setData():
    '''returns None\n\n
    setData(final byte[] data)\n
    '''
def setLength():
    '''returns None\n\n
    setLength(final int length)\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getReader():
    '''returns PdfReader\n\n
    getReader()\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes()\n
    '''
def setObjNum():
    '''returns None\n\n
    setObjNum(final int objNum, final int objGen)\n
    '''
def toPdf():
    '''returns None\n\n
    toPdf(final PdfWriter writer, final OutputStream os)\n
    '''
