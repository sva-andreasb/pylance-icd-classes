def ():
    '''returns XWPFHeaderFooter\n\n
    (final POIXMLDocumentPart parent, final PackagePart part)\n
    '''
def _getHdrFtr():
    '''returns CTHdrFtr\n\n
    _getHdrFtr()\n
    '''
def getBodyElements():
    '''returns List<IBodyElement>\n\n
    getBodyElements()\n
    '''
def getParagraphs():
    '''returns List<XWPFParagraph>\n\n
    getParagraphs()\n
    '''
def getTables():
    '''returns List<XWPFTable>\n\n
    getTables()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setHeaderFooter():
    '''returns None\n\n
    setHeaderFooter(final CTHdrFtr headerFooter)\n
    '''
def getTable():
    '''returns XWPFTable\n\n
    getTable(final CTTbl ctTable)\n
    '''
def getParagraph():
    '''returns XWPFParagraph\n\n
    getParagraph(final CTP p)\n
    '''
def getParagraphArray():
    '''returns XWPFParagraph\n\n
    getParagraphArray(final int pos)\n
    '''
def getListParagraph():
    '''returns List<XWPFParagraph>\n\n
    getListParagraph()\n
    '''
def getAllPictures():
    '''returns List<XWPFPictureData>\n\n
    getAllPictures()\n
    '''
def getAllPackagePictures():
    '''returns List<XWPFPictureData>\n\n
    getAllPackagePictures()\n
    '''
def addPictureData():
    '''returns String\n\n
    addPictureData(final byte[] pictureData, final int format)\n
    addPictureData(final InputStream is, final int format)\n
    '''
def getPictureDataByID():
    '''returns XWPFPictureData\n\n
    getPictureDataByID(final String blipID)\n
    '''
def createParagraph():
    '''returns XWPFParagraph\n\n
    createParagraph()\n
    '''
def createTable():
    '''returns XWPFTable\n\n
    createTable(final int rows, final int cols)\n
    '''
def removeParagraph():
    '''returns None\n\n
    removeParagraph(final XWPFParagraph paragraph)\n
    '''
def removeTable():
    '''returns None\n\n
    removeTable(final XWPFTable table)\n
    '''
def clearHeaderFooter():
    '''returns None\n\n
    clearHeaderFooter()\n
    '''
def insertNewParagraph():
    '''returns XWPFParagraph\n\n
    insertNewParagraph(final XmlCursor cursor)\n
    '''
def insertNewTbl():
    '''returns XWPFTable\n\n
    insertNewTbl(final XmlCursor cursor)\n
    '''
def getOwner():
    '''returns POIXMLDocumentPart\n\n
    getOwner()\n
    '''
def getTableArray():
    '''returns XWPFTable\n\n
    getTableArray(final int pos)\n
    '''
def insertTable():
    '''returns None\n\n
    insertTable(final int pos, final XWPFTable table)\n
    '''
def readHdrFtr():
    '''returns None\n\n
    readHdrFtr()\n
    '''
def getTableCell():
    '''returns XWPFTableCell\n\n
    getTableCell(final CTTc cell)\n
    '''
def getXWPFDocument():
    '''returns XWPFDocument\n\n
    getXWPFDocument()\n
    '''
def setXWPFDocument():
    '''returns None\n\n
    setXWPFDocument(final XWPFDocument doc)\n
    '''
def getPart():
    '''returns POIXMLDocumentPart\n\n
    getPart()\n
    '''
