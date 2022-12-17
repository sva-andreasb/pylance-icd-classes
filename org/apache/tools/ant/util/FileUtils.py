FAT_FILE_TIMESTAMP_GRANULARITY = "long  2000L"
UNIX_FILE_TIMESTAMP_GRANULARITY = "long  1000L"
NTFS_FILE_TIMESTAMP_GRANULARITY = "long  1L"
def getFileURL():
    '''returns URL\n\n
    getFileURL(final File file)\n
    '''
def copyFile():
    '''returns None\n\n
    copyFile(final String sourceFile, final String destFile)\n
    copyFile(final String sourceFile, final String destFile, final FilterSetCollection filters)\n
    copyFile(final String sourceFile, final String destFile, final FilterSetCollection filters, final boolean overwrite)\n
    copyFile(final String sourceFile, final String destFile, final FilterSetCollection filters, final boolean overwrite, final boolean preserveLastModified)\n
    copyFile(final String sourceFile, final String destFile, final FilterSetCollection filters, final boolean overwrite, final boolean preserveLastModified, final String encoding)\n
    copyFile(final String sourceFile, final String destFile, final FilterSetCollection filters, final Vector filterChains, final boolean overwrite, final boolean preserveLastModified, final String encoding, final Project project)\n
    copyFile(final String sourceFile, final String destFile, final FilterSetCollection filters, final Vector filterChains, final boolean overwrite, final boolean preserveLastModified, final String inputEncoding, final String outputEncoding, final Project project)\n
    copyFile(final File sourceFile, final File destFile)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters, final boolean overwrite)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters, final boolean overwrite, final boolean preserveLastModified)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters, final boolean overwrite, final boolean preserveLastModified, final String encoding)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters, final Vector filterChains, final boolean overwrite, final boolean preserveLastModified, final String encoding, final Project project)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters, final Vector filterChains, final boolean overwrite, final boolean preserveLastModified, final String inputEncoding, final String outputEncoding, final Project project)\n
    copyFile(final File sourceFile, final File destFile, final FilterSetCollection filters, final Vector filterChains, final boolean overwrite, final boolean preserveLastModified, final boolean append, final String inputEncoding, final String outputEncoding, final Project project)\n
    '''
def setFileLastModified():
    '''returns None\n\n
    setFileLastModified(final File file, final long time)\n
    '''
def resolveFile():
    '''returns File\n\n
    resolveFile(File file, String filename)\n
    '''
def normalize():
    '''returns File\n\n
    normalize(final String path)\n
    '''
def dissect():
    '''returns String[]\n\n
    dissect(String path)\n
    '''
def toVMSPath():
    '''returns String\n\n
    toVMSPath(final File f)\n
    '''
def createTempFile():
    '''returns File\n\n
    createTempFile(final String prefix, final String suffix, final File parentDir)\n
    createTempFile(final String prefix, final String suffix, final File parentDir, final boolean deleteOnExit, final boolean createFile)\n
    createTempFile(final String prefix, final String suffix, final File parentDir, final boolean deleteOnExit)\n
    '''
def contentEquals():
    '''returns boolean\n\n
    contentEquals(final File f1, final File f2)\n
    contentEquals(final File f1, final File f2, final boolean textfile)\n
    '''
def getParentFile():
    '''returns File\n\n
    getParentFile(final File f)\n
    '''
def createNewFile():
    '''returns boolean\n\n
    createNewFile(final File f)\n
    createNewFile(final File f, final boolean mkdirs)\n
    '''
def isSymbolicLink():
    '''returns boolean\n\n
    isSymbolicLink(final File parent, final String name)\n
    '''
def removeLeadingPath():
    '''returns String\n\n
    removeLeadingPath(final File leading, final File path)\n
    '''
def isLeadingPath():
    '''returns boolean\n\n
    isLeadingPath(final File leading, final File path)\n
    '''
def toURI():
    '''returns String\n\n
    toURI(final String path)\n
    '''
def fromURI():
    '''returns String\n\n
    fromURI(final String uri)\n
    '''
def fileNameEquals():
    '''returns boolean\n\n
    fileNameEquals(final File f1, final File f2)\n
    '''
def rename():
    '''returns None\n\n
    rename(File from, File to)\n
    '''
def getFileTimestampGranularity():
    '''returns long\n\n
    getFileTimestampGranularity()\n
    '''
def hasErrorInCase():
    '''returns boolean\n\n
    hasErrorInCase(File localFile)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File dir, final String name)\n
    '''
def isUpToDate():
    '''returns boolean\n\n
    isUpToDate(final File source, final File dest, final long granularity)\n
    isUpToDate(final File source, final File dest)\n
    isUpToDate(final long sourceTime, final long destTime, final long granularity)\n
    isUpToDate(final long sourceTime, final long destTime)\n
    '''
def tryHardToDelete():
    '''returns boolean\n\n
    tryHardToDelete(final File f)\n
    '''
def getDefaultEncoding():
    '''returns String\n\n
    getDefaultEncoding()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    '''
