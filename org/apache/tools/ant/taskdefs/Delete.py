def ():
    '''returns Delete\n\n
    ()\n
    '''
def setFile():
    '''returns None\n\n
    setFile(final File file)\n
    '''
def setDir():
    '''returns None\n\n
    setDir(final File dir)\n
    '''
def setVerbose():
    '''returns None\n\n
    setVerbose(final boolean verbose)\n
    '''
def setQuiet():
    '''returns None\n\n
    setQuiet(final boolean quiet)\n
    '''
def setFailOnError():
    '''returns None\n\n
    setFailOnError(final boolean failonerror)\n
    '''
def setDeleteOnExit():
    '''returns None\n\n
    setDeleteOnExit(final boolean deleteOnExit)\n
    '''
def setIncludeEmptyDirs():
    '''returns None\n\n
    setIncludeEmptyDirs(final boolean includeEmpty)\n
    '''
def addFileset():
    '''returns None\n\n
    addFileset(final FileSet set)\n
    '''
def add():
    '''returns None\n\n
    add(final ResourceCollection rc)\n
    add(final FileSelector selector)\n
    '''
def createPatternSet():
    '''returns PatternSet\n\n
    createPatternSet()\n
    '''
def setIncludes():
    '''returns None\n\n
    setIncludes(final String includes)\n
    '''
def setExcludes():
    '''returns None\n\n
    setExcludes(final String excludes)\n
    '''
def setDefaultexcludes():
    '''returns None\n\n
    setDefaultexcludes(final boolean useDefaultExcludes)\n
    '''
def setIncludesfile():
    '''returns None\n\n
    setIncludesfile(final File includesfile)\n
    '''
def setExcludesfile():
    '''returns None\n\n
    setExcludesfile(final File excludesfile)\n
    '''
def setCaseSensitive():
    '''returns None\n\n
    setCaseSensitive(final boolean isCaseSensitive)\n
    '''
def setFollowSymlinks():
    '''returns None\n\n
    setFollowSymlinks(final boolean followSymlinks)\n
    '''
def setRemoveNotFollowedSymlinks():
    '''returns None\n\n
    setRemoveNotFollowedSymlinks(final boolean b)\n
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
def addFilename():
    '''returns None\n\n
    addFilename(final FilenameSelector selector)\n
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
def execute():
    '''returns None\n\n
    execute()\n
    '''
def isFilesystemOnly():
    '''returns boolean\n\n
    isFilesystemOnly()\n
    isFilesystemOnly()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    size()\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    iterator()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object foo, final Object bar)\n
    '''
