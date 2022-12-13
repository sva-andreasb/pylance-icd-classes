def FileAlterationObserver():
    '''    public FileAlterationObserver(final String directoryName)
    public FileAlterationObserver(final String directoryName, final FileFilter fileFilter)
    public FileAlterationObserver(final String directoryName, final FileFilter fileFilter, final IOCase caseSensitivity)
    public FileAlterationObserver(final File directory)
    public FileAlterationObserver(final File directory, final FileFilter fileFilter)
    public FileAlterationObserver(final File directory, final FileFilter fileFilter, final IOCase caseSensitivity)
    '''
def getDirectory():
    '''    public File getDirectory()
    '''
def getFileFilter():
    '''    public FileFilter getFileFilter()
    '''
def addListener():
    '''    public void addListener(final FileAlterationListener listener)
    '''
def removeListener():
    '''    public void removeListener(final FileAlterationListener listener)
    '''
def getListeners():
    '''    public Iterable<FileAlterationListener> getListeners()
    '''
def initialize():
    '''    public void initialize()
    '''
def destroy():
    '''    public void destroy()
    '''
def checkAndNotify():
    '''    public void checkAndNotify()
    '''
def toString():
    '''    public String toString()
    '''
