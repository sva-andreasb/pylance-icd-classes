def IdentityConstraint():
    '''public IdentityConstraint(final Collection errorListener, final boolean trackIdrefs)
    '''
def element():
    '''public void element(final ValidatorListener.Event e, final SchemaType st, final SchemaIdentityConstraint[] ics)
    '''
def endElement():
    '''public void endElement(final ValidatorListener.Event e)
    '''
def attr():
    '''public void attr(final ValidatorListener.Event e, final QName name, final SchemaType st, final String value)
    '''
def text():
    '''public void text(final ValidatorListener.Event e, final SchemaType st, final String value, final boolean emptyContent)
    '''
def isValid():
    '''public boolean isValid()
    '''
def errorForEvent():
    '''public static XmlError errorForEvent(final String code, final Object[] args, final int severity, final ValidatorListener.Event event)
    public static XmlError errorForEvent(final String msg, final int severity, final ValidatorListener.Event event)
    '''
