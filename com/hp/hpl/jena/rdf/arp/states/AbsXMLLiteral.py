def ():
    '''returns AbsXMLLiteral\n\n
    (final FrameI p, final AbsXMLContext x, final StringBuffer r)\n
    (final AbsXMLLiteral p, final Map<String, String> ns)\n
    (final XMLHandler h, final AbsXMLContext x)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] chrs, final int start, final int length)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def startElement():
    '''returns FrameI\n\n
    startElement(final String uri, final String localName, final String rawName, final Attributes atts)\n
    '''
