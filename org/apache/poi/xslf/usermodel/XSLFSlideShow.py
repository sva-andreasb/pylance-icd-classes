def ():
    '''returns XSLFSlideShow\n\n
    (final OPCPackage container)\n
    (final String file)\n
    '''
def getPresentation():
    '''returns CTPresentation\n\n
    getPresentation()\n
    '''
def getSlideReferences():
    '''returns CTSlideIdList\n\n
    getSlideReferences()\n
    '''
def getSlideMasterReferences():
    '''returns CTSlideMasterIdList\n\n
    getSlideMasterReferences()\n
    '''
def getSlideMasterPart():
    '''returns PackagePart\n\n
    getSlideMasterPart(final CTSlideMasterIdListEntry master)\n
    '''
def getSlideMaster():
    '''returns CTSlideMaster\n\n
    getSlideMaster(final CTSlideMasterIdListEntry master)\n
    '''
def getSlidePart():
    '''returns PackagePart\n\n
    getSlidePart(final CTSlideIdListEntry slide)\n
    '''
def getSlide():
    '''returns CTSlide\n\n
    getSlide(final CTSlideIdListEntry slide)\n
    '''
def getNodesPart():
    '''returns PackagePart\n\n
    getNodesPart(final CTSlideIdListEntry parentSlide)\n
    '''
def getNotes():
    '''returns CTNotesSlide\n\n
    getNotes(final CTSlideIdListEntry slide)\n
    '''
def getSlideComments():
    '''returns CTCommentList\n\n
    getSlideComments(final CTSlideIdListEntry slide)\n
    '''
def getAllEmbedds():
    '''returns List<PackagePart>\n\n
    getAllEmbedds()\n
    '''
