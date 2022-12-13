RA_IMessage = "IMessage[]  new IMessage[0]"
WEAVEINFO = "Kind  new Kind(\"weaveinfo\", 5)"
INFO = "Kind  new Kind(\"info\", 10)"
DEBUG = "Kind  new Kind(\"debug\", 20)"
TASKTAG = "Kind  new Kind(\"task\", 25)"
WARNING = "Kind  new Kind(\"warning\", 30)"
ERROR = "Kind  new Kind(\"error\", 40)"
FAIL = "Kind  new Kind(\"fail\", 50)"
ABORT = "Kind  new Kind(\"abort\", 60)"
KINDS = "List<Kind>  Collections.unmodifiableList((List<? extends Kind>)Arrays.asList(IMessage.WEAVEINFO, IMessage.INFO, IMessage.DEBUG, IMessage.TASKTAG, IMessage.WARNING, IMessage.ERROR, IMessage.FAIL, IMessage.ABORT))"
def isSameOrLessThan():
    '''public boolean isSameOrLessThan(final Kind kind)
    '''
def compareTo():
    '''public int compareTo(final Kind other)
    '''
def toString():
    '''public String toString()
    '''
def compare():
    '''public int compare(final Kind one, final Kind two)
    '''
