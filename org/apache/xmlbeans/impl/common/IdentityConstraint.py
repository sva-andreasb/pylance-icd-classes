def ():
    '''returns IdentityConstraint\n\n
    (final Collection errorListener, final boolean trackIdrefs)\n
    '''
def element():
    '''returns None\n\n
    element(final ValidatorListener.Event e, final SchemaType st, final SchemaIdentityConstraint[] ics)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final ValidatorListener.Event e)\n
    '''
def attr():
    '''returns None\n\n
    attr(final ValidatorListener.Event e, final QName name, final SchemaType st, final String value)\n
    '''
def text():
    '''returns None\n\n
    text(final ValidatorListener.Event e, final SchemaType st, final String value, final boolean emptyContent)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
