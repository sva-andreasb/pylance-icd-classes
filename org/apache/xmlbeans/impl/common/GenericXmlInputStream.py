def ():
    '''returns GenericXmlInputStream\n\n
    ()\n
    '''
def next():
    '''returns XMLEvent\n\n
    next()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def skip():
    '''returns boolean\n\n
    skip()\n
    skip(final int eventType)\n
    skip(final XMLName name)\n
    skip(final XMLName name, final int eventType)\n
    '''
def skipElement():
    '''returns None\n\n
    skipElement()\n
    '''
def peek():
    '''returns XMLEvent\n\n
    peek()\n
    '''
def getSubStream():
    '''returns XMLInputStream\n\n
    getSubStream()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getReferenceResolver():
    '''returns ReferenceResolver\n\n
    getReferenceResolver()\n
    '''
def setReferenceResolver():
    '''returns None\n\n
    setReferenceResolver(final ReferenceResolver resolver)\n
    '''
