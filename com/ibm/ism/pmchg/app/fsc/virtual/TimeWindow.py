COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns TimeWindow\n\n
    (final Date start, final Date end)\n
    '''
def getStartTime():
    '''returns Date\n\n
    getStartTime()\n
    '''
def getEndTime():
    '''returns Date\n\n
    getEndTime()\n
    '''
def getDuration():
    '''returns double\n\n
    getDuration()\n
    '''
def isOverlapping():
    '''returns boolean\n\n
    isOverlapping(final Date startTime, final Date finishTime)\n
    '''
def isBisecting():
    '''returns boolean\n\n
    isBisecting(final Date startTime, final Date finishTime)\n
    '''
def isEnclosing():
    '''returns boolean\n\n
    isEnclosing(final Date startTime, final Date finishTime)\n
    '''
def isIntersecting():
    '''returns boolean\n\n
    isIntersecting(final Date start, final Date end)\n
    '''
def split():
    '''returns TimeWindow\n\n
    split(final Date startTime, final Date finishTime)\n
    '''
def shrink():
    '''returns None\n\n
    shrink(final Date startTime, final Date finishTime)\n
    '''
def intersect():
    '''returns boolean\n\n
    intersect(final Date start, final Date end)\n
    '''
def copy():
    '''returns TimeWindow\n\n
    copy()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final TimeWindow tw)\n
    '''
