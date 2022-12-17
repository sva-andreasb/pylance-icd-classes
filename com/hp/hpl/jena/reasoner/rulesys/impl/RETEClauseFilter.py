TESTValue = "byte  1"
TESTFunctorName = "byte  2"
TESTIntraMatch = "byte  3"
CREATEToken = "byte  4"
BIND = "byte  5"
END = "byte  6"
ADDRSubject = "byte  16"
ADDRPredicate = "byte  32"
ADDRObject = "byte  48"
ADDRFunctorNode = "byte  64"
def ():
    '''returns RETEClauseFilter\n\n
    (final byte[] instructions, final Object[] args)\n
    '''
def setContinuation():
    '''returns None\n\n
    setContinuation(final RETESinkNode continuation)\n
    '''
def fire():
    '''returns None\n\n
    fire(final Triple triple, final boolean isAdd)\n
    '''
def clone():
    '''returns RETENode\n\n
    clone(final Map<RETENode, RETENode> netCopy, final RETERuleContext context)\n
    '''
