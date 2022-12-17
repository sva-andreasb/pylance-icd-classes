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
    '''returns boolean\n\n
    isSameOrLessThan(final Kind kind)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Kind other)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Kind one, final Kind two)\n
    '''
