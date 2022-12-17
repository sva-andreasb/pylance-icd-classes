WARN = "String  \"warn\""
FAIL = "String  \"fail\""
TRUNCATE = "String  \"truncate\""
GNU = "String  \"gnu\""
OMIT = "String  \"omit\""
def ():
    '''returns TarCompressionMethod\n\n
    ()\n
    (final FileSet fileset)\n
    ()\n
    ()\n
    ()\n
    '''
def createTarFileSet():
    '''returns TarFileSet\n\n
    createTarFileSet()\n
    '''
def add():
    '''returns None\n\n
    add(final ResourceCollection res)\n
    '''
def setTarfile():
    '''returns None\n\n
    setTarfile(final File tarFile)\n
    '''
def setDestFile():
    '''returns None\n\n
    setDestFile(final File destFile)\n
    '''
def setBasedir():
    '''returns None\n\n
    setBasedir(final File baseDir)\n
    '''
def setLongfile():
    '''returns None\n\n
    setLongfile(final String mode)\n
    setLongfile(final TarLongFileMode mode)\n
    '''
def setCompression():
    '''returns None\n\n
    setCompression(final TarCompressionMethod mode)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def getFiles():
    '''returns String[]\n\n
    getFiles(final Project p)\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final String octalString)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def setPreserveLeadingSlashes():
    '''returns None\n\n
    setPreserveLeadingSlashes(final boolean b)\n
    '''
def getPreserveLeadingSlashes():
    '''returns boolean\n\n
    getPreserveLeadingSlashes()\n
    '''
def getValues():
    '''returns String[]\n\n
    getValues()\n
    getValues()\n
    '''
def isTruncateMode():
    '''returns boolean\n\n
    isTruncateMode()\n
    '''
def isWarnMode():
    '''returns boolean\n\n
    isWarnMode()\n
    '''
def isGnuMode():
    '''returns boolean\n\n
    isGnuMode()\n
    '''
def isFailMode():
    '''returns boolean\n\n
    isFailMode()\n
    '''
def isOmitMode():
    '''returns boolean\n\n
    isOmitMode()\n
    '''
