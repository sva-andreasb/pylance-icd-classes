STOPPED = "int  1"
RUNNING = "int  2"
SUSPENDED = "int  3"
def ():
    '''returns IlvValueSource\n\n
    (final String name)\n
    (final IlvValueSource ilvValueSource)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def copy():
    '''returns IlvGroupElement\n\n
    copy()\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener listener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener listener)\n
    '''
