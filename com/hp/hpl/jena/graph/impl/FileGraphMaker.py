def ():
    '''returns FileGraphMaker\n\n
    (final String root)\n
    (final String root, final ReificationStyle style)\n
    (final String root, final ReificationStyle style, final boolean deleteOnClose)\n
    '''
def getFileBase():
    '''returns String\n\n
    getFileBase()\n
    '''
def createGraph():
    '''returns Graph\n\n
    createGraph()\n
    createGraph(final String name, final boolean strict)\n
    '''
def openGraph():
    '''returns Graph\n\n
    openGraph(final String name, final boolean strict)\n
    '''
def notifyClosed():
    '''returns None\n\n
    notifyClosed(final File f)\n
    '''
def removeGraph():
    '''returns None\n\n
    removeGraph(final String name)\n
    '''
def hasGraph():
    '''returns boolean\n\n
    hasGraph(final String name)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File file, final String name)\n
    '''
def listGraphs():
    '''returns ExtendedIterator<String>\n\n
    listGraphs()\n
    '''
def map1():
    '''returns String\n\n
    map1(final String x)\n
    '''
