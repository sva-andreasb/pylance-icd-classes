def ():
    '''returns XMLSlideShow\n\n
    ()\n
    (final OPCPackage pkg)\n
    (final InputStream is)\n
    '''
def getAllEmbedds():
    '''returns List<PackagePart>\n\n
    getAllEmbedds()\n
    '''
def getPictureData():
    '''returns List<XSLFPictureData>\n\n
    getPictureData()\n
    '''
def createSlide():
    '''returns XSLFSlide\n\n
    createSlide(final XSLFSlideLayout layout)\n
    createSlide()\n
    '''
def getNotesSlide():
    '''returns XSLFNotes\n\n
    getNotesSlide(final XSLFSlide slide)\n
    '''
def createNotesMaster():
    '''returns None\n\n
    createNotesMaster()\n
    '''
def getNotesMaster():
    '''returns XSLFNotesMaster\n\n
    getNotesMaster()\n
    '''
def getSlideMasters():
    '''returns List<XSLFSlideMaster>\n\n
    getSlideMasters()\n
    '''
def getSlides():
    '''returns List<XSLFSlide>\n\n
    getSlides()\n
    '''
def getCommentAuthors():
    '''returns XSLFCommentAuthors\n\n
    getCommentAuthors()\n
    '''
def setSlideOrder():
    '''returns None\n\n
    setSlideOrder(final XSLFSlide slide, final int newIndex)\n
    '''
def removeSlide():
    '''returns XSLFSlide\n\n
    removeSlide(final int index)\n
    '''
def getPageSize():
    '''returns Dimension\n\n
    getPageSize()\n
    '''
def setPageSize():
    '''returns None\n\n
    setPageSize(final Dimension pgSize)\n
    '''
def getCTPresentation():
    '''returns CTPresentation\n\n
    getCTPresentation()\n
    '''
def addPicture():
    '''returns XSLFPictureData\n\n
    addPicture(final byte[] pictureData, final PictureData.PictureType format)\n
    addPicture(final InputStream is, final PictureData.PictureType format)\n
    addPicture(final File pict, final PictureData.PictureType format)\n
    '''
def findPictureData():
    '''returns XSLFPictureData\n\n
    findPictureData(final byte[] pictureData)\n
    '''
def findLayout():
    '''returns XSLFSlideLayout\n\n
    findLayout(final String name)\n
    '''
def getTableStyles():
    '''returns XSLFTableStyles\n\n
    getTableStyles()\n
    '''
def getResources():
    '''returns Resources\n\n
    getResources()\n
    '''
