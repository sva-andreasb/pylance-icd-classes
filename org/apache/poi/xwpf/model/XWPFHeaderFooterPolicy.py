def ():
    '''returns XWPFHeaderFooterPolicy\n\n
    (final XWPFDocument doc)\n
    (final XWPFDocument doc, CTSectPr sectPr)\n
    '''
def createHeader():
    '''returns XWPFHeader\n\n
    createHeader(final STHdrFtr.Enum type)\n
    createHeader(final STHdrFtr.Enum type, final XWPFParagraph[] pars)\n
    '''
def createFooter():
    '''returns XWPFFooter\n\n
    createFooter(final STHdrFtr.Enum type)\n
    createFooter(final STHdrFtr.Enum type, final XWPFParagraph[] pars)\n
    '''
def getFirstPageHeader():
    '''returns XWPFHeader\n\n
    getFirstPageHeader()\n
    '''
def getFirstPageFooter():
    '''returns XWPFFooter\n\n
    getFirstPageFooter()\n
    '''
def getOddPageHeader():
    '''returns XWPFHeader\n\n
    getOddPageHeader()\n
    '''
def getOddPageFooter():
    '''returns XWPFFooter\n\n
    getOddPageFooter()\n
    '''
def getEvenPageHeader():
    '''returns XWPFHeader\n\n
    getEvenPageHeader()\n
    '''
def getEvenPageFooter():
    '''returns XWPFFooter\n\n
    getEvenPageFooter()\n
    '''
def getDefaultHeader():
    '''returns XWPFHeader\n\n
    getDefaultHeader()\n
    '''
def getDefaultFooter():
    '''returns XWPFFooter\n\n
    getDefaultFooter()\n
    '''
def getHeader():
    '''returns XWPFHeader\n\n
    getHeader(final int pageNumber)\n
    getHeader(final STHdrFtr.Enum type)\n
    '''
def getFooter():
    '''returns XWPFFooter\n\n
    getFooter(final int pageNumber)\n
    getFooter(final STHdrFtr.Enum type)\n
    '''
def createWatermark():
    '''returns None\n\n
    createWatermark(final String text)\n
    '''
