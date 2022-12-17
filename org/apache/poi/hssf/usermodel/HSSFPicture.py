PICTURE_TYPE_EMF = "int  2"
PICTURE_TYPE_WMF = "int  3"
PICTURE_TYPE_PICT = "int  4"
PICTURE_TYPE_JPEG = "int  5"
PICTURE_TYPE_PNG = "int  6"
PICTURE_TYPE_DIB = "int  7"
def ():
    '''returns HSSFPicture\n\n
    (final EscherContainerRecord spContainer, final ObjRecord objRecord)\n
    (final HSSFShape parent, final HSSFAnchor anchor)\n
    '''
def getPictureIndex():
    '''returns int\n\n
    getPictureIndex()\n
    '''
def setPictureIndex():
    '''returns None\n\n
    setPictureIndex(final int pictureIndex)\n
    '''
def resize():
    '''returns None\n\n
    resize()\n
    resize(final double scale)\n
    resize(final double scaleX, final double scaleY)\n
    '''
def getPreferredSize():
    '''returns HSSFClientAnchor\n\n
    getPreferredSize()\n
    getPreferredSize(final double scale)\n
    getPreferredSize(final double scaleX, final double scaleY)\n
    '''
def getImageDimension():
    '''returns Dimension\n\n
    getImageDimension()\n
    '''
def getPictureData():
    '''returns HSSFPictureData\n\n
    getPictureData()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def setFileName():
    '''returns None\n\n
    setFileName(final String data)\n
    '''
def setShapeType():
    '''returns None\n\n
    setShapeType(final int shapeType)\n
    '''
def getClientAnchor():
    '''returns HSSFClientAnchor\n\n
    getClientAnchor()\n
    '''
def getSheet():
    '''returns HSSFSheet\n\n
    getSheet()\n
    '''
