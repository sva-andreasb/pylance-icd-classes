def ():
    '''returns FileAlterationObserver\n\n
    (final String directoryName)\n
    (final String directoryName, final FileFilter fileFilter)\n
    (final String directoryName, final FileFilter fileFilter, final IOCase caseSensitivity)\n
    (final File directory)\n
    (final File directory, final FileFilter fileFilter)\n
    (final File directory, final FileFilter fileFilter, final IOCase caseSensitivity)\n
    '''
def getDirectory():
    '''returns File\n\n
    getDirectory()\n
    '''
def getFileFilter():
    '''returns FileFilter\n\n
    getFileFilter()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final FileAlterationListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final FileAlterationListener listener)\n
    '''
def getListeners():
    '''returns Iterable<FileAlterationListener>\n\n
    getListeners()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def checkAndNotify():
    '''returns None\n\n
    checkAndNotify()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
