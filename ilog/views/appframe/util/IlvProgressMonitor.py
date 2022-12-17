START_PROGRESS_MESSAGE = "String  \"StartProgressTask\""
NEW_PROGRESS_VALUE_MESSAGE = "String  \"NewProgressTaskValueMessage\""
END_PROGRESS_MESSAGE = "String  \"EndProgressTask\""
def ():
    '''returns IlvProgressMonitor\n\n
    (final IlvApplication application, final Object o, final String e, final int n, final int max)\n
    (final Action c, final IlvApplication ilvApplication, final Object o, final String s, final int n, final int n2)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String b)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication a)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String s)\n
    '''
def updateAction():
    '''returns boolean\n\n
    updateAction(final Action action)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def setProgress():
    '''returns None\n\n
    setProgress(final int progress)\n
    '''
def incrementProgressValue():
    '''returns None\n\n
    incrementProgressValue(final int n)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isInProgress():
    '''returns boolean\n\n
    isInProgress()\n
    '''
def isCanceled():
    '''returns boolean\n\n
    isCanceled()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
