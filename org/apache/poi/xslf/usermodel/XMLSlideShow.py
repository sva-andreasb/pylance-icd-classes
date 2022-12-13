def XMLSlideShow():
    '''public XMLSlideShow()
    public XMLSlideShow(final OPCPackage pkg)
    public XMLSlideShow(final InputStream is)
    '''
def getAllEmbedds():
    '''public List<PackagePart> getAllEmbedds()
    '''
def getPictureData():
    '''public List<XSLFPictureData> getPictureData()
    '''
def createSlide():
    '''public XSLFSlide createSlide(final XSLFSlideLayout layout)
    public XSLFSlide createSlide()
    '''
def getNotesSlide():
    '''public XSLFNotes getNotesSlide(final XSLFSlide slide)
    '''
def createNotesMaster():
    '''public void createNotesMaster()
    '''
def getNotesMaster():
    '''public XSLFNotesMaster getNotesMaster()
    '''
def getSlideMasters():
    '''public List<XSLFSlideMaster> getSlideMasters()
    '''
def getSlides():
    '''public List<XSLFSlide> getSlides()
    '''
def getCommentAuthors():
    '''public XSLFCommentAuthors getCommentAuthors()
    '''
def setSlideOrder():
    '''public void setSlideOrder(final XSLFSlide slide, final int newIndex)
    '''
def removeSlide():
    '''public XSLFSlide removeSlide(final int index)
    '''
def getPageSize():
    '''public Dimension getPageSize()
    '''
def setPageSize():
    '''public void setPageSize(final Dimension pgSize)
    '''
def getCTPresentation():
    '''public CTPresentation getCTPresentation()
    '''
def addPicture():
    '''public XSLFPictureData addPicture(final byte[] pictureData, final PictureData.PictureType format)
    public XSLFPictureData addPicture(final InputStream is, final PictureData.PictureType format)
    public XSLFPictureData addPicture(final File pict, final PictureData.PictureType format)
    '''
def findPictureData():
    '''public XSLFPictureData findPictureData(final byte[] pictureData)
    '''
def findLayout():
    '''public XSLFSlideLayout findLayout(final String name)
    '''
def getTableStyles():
    '''public XSLFTableStyles getTableStyles()
    '''
def createMasterSheet():
    '''public MasterSheet<XSLFShape, XSLFTextParagraph> createMasterSheet()
    '''
def getResources():
    '''public Resources getResources()
    '''
