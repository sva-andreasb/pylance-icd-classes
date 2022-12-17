XA_RBBASE = "int  100"
XA_RBROLLBACK = "int  100"
XA_RBCOMMFAIL = "int  101"
XA_RBDEADLOCK = "int  102"
XA_RBINTEGRITY = "int  103"
XA_RBOTHER = "int  104"
XA_RBPROTO = "int  105"
XA_RBTIMEOUT = "int  106"
XA_RBTRANSIENT = "int  107"
XA_RBEND = "int  107"
XA_NOMIGRATE = "int  9"
XA_HEURHAZ = "int  8"
XA_HEURCOM = "int  7"
XA_HEURRB = "int  6"
XA_HEURMIX = "int  5"
XA_RETRY = "int  4"
XA_RDONLY = "int  3"
XAER_ASYNC = "int  -2"
XAER_RMERR = "int  -3"
XAER_NOTA = "int  -4"
XAER_INVAL = "int  -5"
XAER_PROTO = "int  -6"
XAER_RMFAIL = "int  -7"
XAER_DUPID = "int  -8"
XAER_OUTSIDE = "int  -9"
def ():
    '''returns XAException\n\n
    ()\n
    (final int errcode)\n
    (final String s)\n
    '''
