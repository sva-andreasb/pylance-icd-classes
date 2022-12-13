CREATED = "int  1"
DELETED = "int  2"
RENAMED = "int  3"
def getType():
    '''public int getType()
    '''
def dispatch():
    '''public void dispatch(final Object listener)
    '''
def getFolder():
    '''public Folder getFolder()
    '''
def getNewFolder():
    '''public Folder getNewFolder()
    '''
def FolderEvent():
    '''public FolderEvent(final Object source, final Folder folder, final int type)
    public FolderEvent(final Object source, final Folder oldFolder, final Folder newFolder, final int type)
    '''
