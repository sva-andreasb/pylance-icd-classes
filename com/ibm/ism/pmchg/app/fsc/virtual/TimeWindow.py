COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def TimeWindow():
    '''public TimeWindow(final Date start, final Date end)
    '''
def getStartTime():
    '''public Date getStartTime()
    '''
def getEndTime():
    '''public Date getEndTime()
    '''
def getDuration():
    '''public double getDuration()
    '''
def isOverlapping():
    '''public boolean isOverlapping(final Date startTime, final Date finishTime)
    '''
def isBisecting():
    '''public boolean isBisecting(final Date startTime, final Date finishTime)
    '''
def isEnclosing():
    '''public boolean isEnclosing(final Date startTime, final Date finishTime)
    '''
def isIntersecting():
    '''public boolean isIntersecting(final Date start, final Date end)
    '''
def split():
    '''public TimeWindow split(final Date startTime, final Date finishTime)
    '''
def shrink():
    '''public void shrink(final Date startTime, final Date finishTime)
    '''
def intersect():
    '''public boolean intersect(final Date start, final Date end)
    '''
def copy():
    '''public TimeWindow copy()
    '''
def toString():
    '''public String toString()
    '''
def compareTo():
    '''public int compareTo(final TimeWindow tw)
    '''
