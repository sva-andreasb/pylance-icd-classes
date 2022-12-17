def ():
    '''returns XWPFDocument\n\n
    (final OPCPackage pkg)\n
    (final InputStream is)\n
    ()\n
    '''
def getDocument():
    '''returns CTDocument1\n\n
    getDocument()\n
    '''
def getBodyElements():
    '''returns List<IBodyElement>\n\n
    getBodyElements()\n
    '''
def getBodyElementsIterator():
    '''returns Iterator<IBodyElement>\n\n
    getBodyElementsIterator()\n
    '''
def getParagraphs():
    '''returns List<XWPFParagraph>\n\n
    getParagraphs()\n
    '''
def getTables():
    '''returns List<XWPFTable>\n\n
    getTables()\n
    '''
def getTableArray():
    '''returns XWPFTable\n\n
    getTableArray(final int pos)\n
    '''
def getFooterList():
    '''returns List<XWPFFooter>\n\n
    getFooterList()\n
    '''
def getFooterArray():
    '''returns XWPFFooter\n\n
    getFooterArray(final int pos)\n
    '''
def getHeaderList():
    '''returns List<XWPFHeader>\n\n
    getHeaderList()\n
    '''
def getHeaderArray():
    '''returns XWPFHeader\n\n
    getHeaderArray(final int pos)\n
    '''
def getTblStyle():
    '''returns String\n\n
    getTblStyle(final XWPFTable table)\n
    '''
def getHyperlinkByID():
    '''returns XWPFHyperlink\n\n
    getHyperlinkByID(final String id)\n
    '''
def getFootnoteByID():
    '''returns XWPFFootnote\n\n
    getFootnoteByID(final int id)\n
    '''
def getEndnoteByID():
    '''returns XWPFFootnote\n\n
    getEndnoteByID(final int id)\n
    '''
def getFootnotes():
    '''returns List<XWPFFootnote>\n\n
    getFootnotes()\n
    '''
def getHyperlinks():
    '''returns XWPFHyperlink[]\n\n
    getHyperlinks()\n
    '''
def getCommentByID():
    '''returns XWPFComment\n\n
    getCommentByID(final String id)\n
    '''
def getComments():
    '''returns XWPFComment[]\n\n
    getComments()\n
    '''
def getPartById():
    '''returns PackagePart\n\n
    getPartById(final String id)\n
    '''
def getHeaderFooterPolicy():
    '''returns XWPFHeaderFooterPolicy\n\n
    getHeaderFooterPolicy()\n
    '''
def createHeaderFooterPolicy():
    '''returns XWPFHeaderFooterPolicy\n\n
    createHeaderFooterPolicy()\n
    '''
def createHeader():
    '''returns XWPFHeader\n\n
    createHeader(final HeaderFooterType type)\n
    '''
def createFooter():
    '''returns XWPFFooter\n\n
    createFooter(final HeaderFooterType type)\n
    '''
def getStyle():
    '''returns CTStyles\n\n
    getStyle()\n
    '''
def getAllEmbedds():
    '''returns List<PackagePart>\n\n
    getAllEmbedds()\n
    '''
def getParagraphPos():
    '''returns int\n\n
    getParagraphPos(final int pos)\n
    '''
def getTablePos():
    '''returns int\n\n
    getTablePos(final int pos)\n
    '''
def insertNewParagraph():
    '''returns XWPFParagraph\n\n
    insertNewParagraph(final XmlCursor cursor)\n
    '''
def insertNewTbl():
    '''returns XWPFTable\n\n
    insertNewTbl(final XmlCursor cursor)\n
    '''
def getPosOfParagraph():
    '''returns int\n\n
    getPosOfParagraph(final XWPFParagraph p)\n
    '''
def getPosOfTable():
    '''returns int\n\n
    getPosOfTable(final XWPFTable t)\n
    '''
def createParagraph():
    '''returns XWPFParagraph\n\n
    createParagraph()\n
    '''
def createNumbering():
    '''returns XWPFNumbering\n\n
    createNumbering()\n
    '''
def createStyles():
    '''returns XWPFStyles\n\n
    createStyles()\n
    '''
def createFootnotes():
    '''returns XWPFFootnotes\n\n
    createFootnotes()\n
    '''
def addFootnote():
    '''returns XWPFFootnote\n\n
    addFootnote(final CTFtnEdn note)\n
    '''
def addEndnote():
    '''returns XWPFFootnote\n\n
    addEndnote(final CTFtnEdn note)\n
    '''
def removeBodyElement():
    '''returns boolean\n\n
    removeBodyElement(final int pos)\n
    '''
def setParagraph():
    '''returns None\n\n
    setParagraph(final XWPFParagraph paragraph, final int pos)\n
    '''
def getLastParagraph():
    '''returns XWPFParagraph\n\n
    getLastParagraph()\n
    '''
def createTable():
    '''returns XWPFTable\n\n
    createTable()\n
    createTable(final int rows, final int cols)\n
    '''
def createTOC():
    '''returns None\n\n
    createTOC()\n
    '''
def setTable():
    '''returns None\n\n
    setTable(final int pos, final XWPFTable table)\n
    '''
def isEnforcedProtection():
    '''returns boolean\n\n
    isEnforcedProtection()\n
    '''
def isEnforcedReadonlyProtection():
    '''returns boolean\n\n
    isEnforcedReadonlyProtection()\n
    '''
def isEnforcedFillingFormsProtection():
    '''returns boolean\n\n
    isEnforcedFillingFormsProtection()\n
    '''
def isEnforcedCommentsProtection():
    '''returns boolean\n\n
    isEnforcedCommentsProtection()\n
    '''
def isEnforcedTrackedChangesProtection():
    '''returns boolean\n\n
    isEnforcedTrackedChangesProtection()\n
    '''
def isEnforcedUpdateFields():
    '''returns boolean\n\n
    isEnforcedUpdateFields()\n
    '''
def enforceReadonlyProtection():
    '''returns None\n\n
    enforceReadonlyProtection()\n
    enforceReadonlyProtection(final String password, final HashAlgorithm hashAlgo)\n
    '''
def enforceFillingFormsProtection():
    '''returns None\n\n
    enforceFillingFormsProtection()\n
    enforceFillingFormsProtection(final String password, final HashAlgorithm hashAlgo)\n
    '''
def enforceCommentsProtection():
    '''returns None\n\n
    enforceCommentsProtection()\n
    enforceCommentsProtection(final String password, final HashAlgorithm hashAlgo)\n
    '''
def enforceTrackedChangesProtection():
    '''returns None\n\n
    enforceTrackedChangesProtection()\n
    enforceTrackedChangesProtection(final String password, final HashAlgorithm hashAlgo)\n
    '''
def validateProtectionPassword():
    '''returns boolean\n\n
    validateProtectionPassword(final String password)\n
    '''
def removeProtectionEnforcement():
    '''returns None\n\n
    removeProtectionEnforcement()\n
    '''
def enforceUpdateFields():
    '''returns None\n\n
    enforceUpdateFields()\n
    '''
def isTrackRevisions():
    '''returns boolean\n\n
    isTrackRevisions()\n
    '''
def setTrackRevisions():
    '''returns None\n\n
    setTrackRevisions(final boolean enable)\n
    '''
def getZoomPercent():
    '''returns long\n\n
    getZoomPercent()\n
    '''
def setZoomPercent():
    '''returns None\n\n
    setZoomPercent(final long zoomPercent)\n
    '''
def insertTable():
    '''returns None\n\n
    insertTable(final int pos, final XWPFTable table)\n
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
def getNextPicNameNumber():
    '''returns int\n\n
    getNextPicNameNumber(final int format)\n
    '''
def getPictureDataByID():
    '''returns XWPFPictureData\n\n
    getPictureDataByID(final String blipID)\n
    '''
def getNumbering():
    '''returns XWPFNumbering\n\n
    getNumbering()\n
    '''
def getStyles():
    '''returns XWPFStyles\n\n
    getStyles()\n
    '''
def getParagraph():
    '''returns XWPFParagraph\n\n
    getParagraph(final CTP p)\n
    '''
def getTable():
    '''returns XWPFTable\n\n
    getTable(final CTTbl ctTbl)\n
    '''
def getTablesIterator():
    '''returns Iterator<XWPFTable>\n\n
    getTablesIterator()\n
    '''
def getParagraphsIterator():
    '''returns Iterator<XWPFParagraph>\n\n
    getParagraphsIterator()\n
    '''
def getParagraphArray():
    '''returns XWPFParagraph\n\n
    getParagraphArray(final int pos)\n
    '''
def getPart():
    '''returns POIXMLDocumentPart\n\n
    getPart()\n
    '''
def getPartType():
    '''returns BodyType\n\n
    getPartType()\n
    '''
def getTableCell():
    '''returns XWPFTableCell\n\n
    getTableCell(final CTTc cell)\n
    '''
def getXWPFDocument():
    '''returns XWPFDocument\n\n
    getXWPFDocument()\n
    '''
