def ():
    '''returns AbstractFileSet\n\n
    ()\n
    '''
def setRefid():
    '''returns None\n\n
    setRefid(final Reference r)\n
    '''
def getDir():
    '''returns File\n\n
    getDir()\n
    '''
def setMaxLevelsOfSymlinks():
    '''returns None\n\n
    setMaxLevelsOfSymlinks(final int max)\n
    '''
def getMaxLevelsOfSymlinks():
    '''returns int\n\n
    getMaxLevelsOfSymlinks()\n
    '''
def setErrorOnMissingDir():
    '''returns None\n\n
    setErrorOnMissingDir(final boolean errorOnMissingDir)\n
    '''
def getDirectoryScanner():
    '''returns DirectoryScanner\n\n
    getDirectoryScanner()\n
    getDirectoryScanner(final Project p)\n
    '''
def setupDirectoryScanner():
    '''returns None\n\n
    setupDirectoryScanner(final FileScanner ds)\n
    '''
def addSelector():
    '''returns None\n\n
    addSelector(final SelectSelector selector)\n
    '''
def addAnd():
    '''returns None\n\n
    addAnd(final AndSelector selector)\n
    '''
def addOr():
    '''returns None\n\n
    addOr(final OrSelector selector)\n
    '''
def addNot():
    '''returns None\n\n
    addNot(final NotSelector selector)\n
    '''
def addNone():
    '''returns None\n\n
    addNone(final NoneSelector selector)\n
    '''
def addMajority():
    '''returns None\n\n
    addMajority(final MajoritySelector selector)\n
    '''
def addDate():
    '''returns None\n\n
    addDate(final DateSelector selector)\n
    '''
def addSize():
    '''returns None\n\n
    addSize(final SizeSelector selector)\n
    '''
def addDifferent():
    '''returns None\n\n
    addDifferent(final DifferentSelector selector)\n
    '''
def addFilename():
    '''returns None\n\n
    addFilename(final FilenameSelector selector)\n
    '''
def addType():
    '''returns None\n\n
    addType(final TypeSelector selector)\n
    '''
def addCustom():
    '''returns None\n\n
    addCustom(final ExtendSelector selector)\n
    '''
def addContains():
    '''returns None\n\n
    addContains(final ContainsSelector selector)\n
    '''
def addPresent():
    '''returns None\n\n
    addPresent(final PresentSelector selector)\n
    '''
def addDepth():
    '''returns None\n\n
    addDepth(final DepthSelector selector)\n
    '''
def addDepend():
    '''returns None\n\n
    addDepend(final DependSelector selector)\n
    '''
def addContainsRegexp():
    '''returns None\n\n
    addContainsRegexp(final ContainsRegexpSelector selector)\n
    '''
def addModified():
    '''returns None\n\n
    addModified(final ModifiedSelector selector)\n
    '''
def addReadable():
    '''returns None\n\n
    addReadable(final ReadableSelector r)\n
    '''
def addWritable():
    '''returns None\n\n
    addWritable(final WritableSelector w)\n
    '''
def add():
    '''returns None\n\n
    add(final FileSelector selector)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def mergeIncludes():
    '''returns String[]\n\n
    mergeIncludes(final Project p)\n
    '''
def mergeExcludes():
    '''returns String[]\n\n
    mergeExcludes(final Project p)\n
    '''
