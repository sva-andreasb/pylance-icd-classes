ELEMENT = "String  \"query\""
NAMESPACE = "String  \"jabber:iq:search\""
def ():
    '''returns UserSearch\n\n
    ()\n
    '''
def getSearchForm():
    '''returns Form\n\n
    getSearchForm(final XMPPConnection con, final DomainBareJid searchService)\n
    '''
def sendSearchForm():
    '''returns ReportedData\n\n
    sendSearchForm(final XMPPConnection con, final Form searchForm, final DomainBareJid searchService)\n
    '''
def sendSimpleSearchForm():
    '''returns ReportedData\n\n
    sendSimpleSearchForm(final XMPPConnection con, final Form searchForm, final DomainBareJid searchService)\n
    '''
def parse():
    '''returns IQ\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
