def replace():
    '''returns int\n\n
    replace(final NGCCEventReceiver oldHandler, final NGCCEventReceiver newHandler)\n
    '''
def enterElement():
    '''returns None\n\n
    enterElement(final String uri, final String localName, final String qname, final Attributes atts)\n
    '''
def leaveElement():
    '''returns None\n\n
    leaveElement(final String uri, final String localName, final String qname)\n
    '''
def enterAttribute():
    '''returns None\n\n
    enterAttribute(final String uri, final String localName, final String qname)\n
    '''
def leaveAttribute():
    '''returns None\n\n
    leaveAttribute(final String uri, final String localName, final String qname)\n
    '''
def text():
    '''returns None\n\n
    text(final String value)\n
    '''
def joinByEnterElement():
    '''returns None\n\n
    joinByEnterElement(final NGCCEventReceiver source, final String uri, final String local, final String qname, final Attributes atts)\n
    '''
def joinByLeaveElement():
    '''returns None\n\n
    joinByLeaveElement(final NGCCEventReceiver source, final String uri, final String local, final String qname)\n
    '''
def joinByEnterAttribute():
    '''returns None\n\n
    joinByEnterAttribute(final NGCCEventReceiver source, final String uri, final String local, final String qname)\n
    '''
def joinByLeaveAttribute():
    '''returns None\n\n
    joinByLeaveAttribute(final NGCCEventReceiver source, final String uri, final String local, final String qname)\n
    '''
def joinByText():
    '''returns None\n\n
    joinByText(final NGCCEventReceiver source, final String value)\n
    '''
def sendEnterAttribute():
    '''returns None\n\n
    sendEnterAttribute(final int threadId, final String uri, final String local, final String qname)\n
    '''
def sendEnterElement():
    '''returns None\n\n
    sendEnterElement(final int threadId, final String uri, final String local, final String qname, final Attributes atts)\n
    '''
def sendLeaveAttribute():
    '''returns None\n\n
    sendLeaveAttribute(final int threadId, final String uri, final String local, final String qname)\n
    '''
def sendLeaveElement():
    '''returns None\n\n
    sendLeaveElement(final int threadId, final String uri, final String local, final String qname)\n
    '''
def sendText():
    '''returns None\n\n
    sendText(final int threadId, final String value)\n
    '''
