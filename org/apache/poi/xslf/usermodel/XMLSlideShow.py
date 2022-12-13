def XMLSlideShow():
'''public XMLSlideShow()
public XMLSlideShow(final OPCPackage pkg)
public XMLSlideShow(final InputStream is)
'''
pass
def getAllEmbedds():
'''public List<PackagePart> getAllEmbedds()
'''
pass
def getPictureData():
'''public List<XSLFPictureData> getPictureData()
'''
pass
def createSlide():
'''public XSLFSlide createSlide(final XSLFSlideLayout layout)
public XSLFSlide createSlide()
'''
pass
def getNotesSlide():
'''public XSLFNotes getNotesSlide(final XSLFSlide slide)
'''
pass
def createNotesMaster():
'''public void createNotesMaster()
'''
pass
def getNotesMaster():
'''public XSLFNotesMaster getNotesMaster()
'''
pass
def getSlideMasters():
'''public List<XSLFSlideMaster> getSlideMasters()
'''
pass
def getSlides():
'''public List<XSLFSlide> getSlides()
'''
pass
def getCommentAuthors():
'''public XSLFCommentAuthors getCommentAuthors()
'''
pass
def setSlideOrder():
'''public void setSlideOrder(final XSLFSlide slide, final int newIndex)
'''
pass
def removeSlide():
'''public XSLFSlide removeSlide(final int index)
'''
pass
def getPageSize():
'''public Dimension getPageSize()
'''
pass
def setPageSize():
'''public void setPageSize(final Dimension pgSize)
'''
pass
def getCTPresentation():
'''public CTPresentation getCTPresentation()
'''
pass
def addPicture():
'''public XSLFPictureData addPicture(final byte[] pictureData, final PictureData.PictureType format)
public XSLFPictureData addPicture(final InputStream is, final PictureData.PictureType format)
public XSLFPictureData addPicture(final File pict, final PictureData.PictureType format)
'''
pass
def findPictureData():
'''public XSLFPictureData findPictureData(final byte[] pictureData)
'''
pass
def findLayout():
'''public XSLFSlideLayout findLayout(final String name)
'''
pass
def getTableStyles():
'''public XSLFTableStyles getTableStyles()
'''
pass
def createMasterSheet():
'''public MasterSheet<XSLFShape, XSLFTextParagraph> createMasterSheet()
'''
pass
def getResources():
'''public Resources getResources()
'''
pass
