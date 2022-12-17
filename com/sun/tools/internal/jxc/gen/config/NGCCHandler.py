def spawnChildFromEnterElement():
    '''returns None\n\n
    spawnChildFromEnterElement(final NGCCEventReceiver child, final String uri, final String localname, final String qname, final Attributes atts)\n
    '''
def spawnChildFromEnterAttribute():
    '''returns None\n\n
    spawnChildFromEnterAttribute(final NGCCEventReceiver child, final String uri, final String localname, final String qname)\n
    '''
def spawnChildFromLeaveElement():
    '''returns None\n\n
    spawnChildFromLeaveElement(final NGCCEventReceiver child, final String uri, final String localname, final String qname)\n
    '''
def spawnChildFromLeaveAttribute():
    '''returns None\n\n
    spawnChildFromLeaveAttribute(final NGCCEventReceiver child, final String uri, final String localname, final String qname)\n
    '''
def spawnChildFromText():
    '''returns None\n\n
    spawnChildFromText(final NGCCEventReceiver child, final String value)\n
    '''
def revertToParentFromEnterElement():
    '''returns None\n\n
    revertToParentFromEnterElement(final Object result, final int cookie, final String uri, final String local, final String qname, final Attributes atts)\n
    '''
def revertToParentFromLeaveElement():
    '''returns None\n\n
    revertToParentFromLeaveElement(final Object result, final int cookie, final String uri, final String local, final String qname)\n
    '''
def revertToParentFromEnterAttribute():
    '''returns None\n\n
    revertToParentFromEnterAttribute(final Object result, final int cookie, final String uri, final String local, final String qname)\n
    '''
def revertToParentFromLeaveAttribute():
    '''returns None\n\n
    revertToParentFromLeaveAttribute(final Object result, final int cookie, final String uri, final String local, final String qname)\n
    '''
def revertToParentFromText():
    '''returns None\n\n
    revertToParentFromText(final Object result, final int cookie, final String text)\n
    '''
def unexpectedEnterElement():
    '''returns None\n\n
    unexpectedEnterElement(final String qname)\n
    '''
def unexpectedLeaveElement():
    '''returns None\n\n
    unexpectedLeaveElement(final String qname)\n
    '''
def unexpectedEnterAttribute():
    '''returns None\n\n
    unexpectedEnterAttribute(final String qname)\n
    '''
def unexpectedLeaveAttribute():
    '''returns None\n\n
    unexpectedLeaveAttribute(final String qname)\n
    '''
