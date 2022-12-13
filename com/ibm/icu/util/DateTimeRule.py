DOM = "int  0"
DOW = "int  1"
DOW_GEQ_DOM = "int  2"
DOW_LEQ_DOM = "int  3"
WALL_TIME = "int  0"
STANDARD_TIME = "int  1"
UTC_TIME = "int  2"
def DateTimeRule():
    '''public DateTimeRule(final int month, final int dayOfMonth, final int millisInDay, final int timeType)
    public DateTimeRule(final int month, final int weekInMonth, final int dayOfWeek, final int millisInDay, final int timeType)
    public DateTimeRule(final int month, final int dayOfMonth, final int dayOfWeek, final boolean after, final int millisInDay, final int timeType)
    '''
def getDateRuleType():
    '''public int getDateRuleType()
    '''
def getRuleMonth():
    '''public int getRuleMonth()
    '''
def getRuleDayOfMonth():
    '''public int getRuleDayOfMonth()
    '''
def getRuleDayOfWeek():
    '''public int getRuleDayOfWeek()
    '''
def getRuleWeekInMonth():
    '''public int getRuleWeekInMonth()
    '''
def getTimeRuleType():
    '''public int getTimeRuleType()
    '''
def getRuleMillisInDay():
    '''public int getRuleMillisInDay()
    '''
def toString():
    '''public String toString()
    '''
