def ():
    '''returns ChangeRecorder\n\n
    ()\n
    (final EObject rootObject)\n
    (final Resource resource)\n
    (final ResourceSet resourceSet)\n
    (final Collection rootObjects)\n
    '''
def isRecording():
    '''returns boolean\n\n
    isRecording()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def beginRecording():
    '''returns None\n\n
    beginRecording(final Collection rootObjects)\n
    beginRecording(final ChangeDescription changeDescription, final Collection rootObjects)\n
    '''
def summarize():
    '''returns ChangeDescription\n\n
    summarize()\n
    '''
def endRecording():
    '''returns ChangeDescription\n\n
    endRecording()\n
    '''
def notifyChanged():
    '''returns None\n\n
    notifyChanged(final Notification notification)\n
    '''
def setTarget():
    '''returns None\n\n
    setTarget(final Notifier target)\n
    '''
def unsetTarget():
    '''returns None\n\n
    unsetTarget(final Notifier oldTarget)\n
    '''
def getTarget():
    '''returns Notifier\n\n
    getTarget()\n
    '''
def isAdapterForType():
    '''returns boolean\n\n
    isAdapterForType(final Object type)\n
    '''
