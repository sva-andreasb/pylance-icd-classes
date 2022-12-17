DOM = "int  0"
DOW = "int  1"
DOW_GEQ_DOM = "int  2"
DOW_LEQ_DOM = "int  3"
WALL_TIME = "int  0"
STANDARD_TIME = "int  1"
UTC_TIME = "int  2"
def ():
    '''returns DateTimeRule\n\n
    (final int month, final int dayOfMonth, final int millisInDay, final int timeType)\n
    (final int month, final int weekInMonth, final int dayOfWeek, final int millisInDay, final int timeType)\n
    (final int month, final int dayOfMonth, final int dayOfWeek, final boolean after, final int millisInDay, final int timeType)\n
    '''
def getDateRuleType():
    '''returns int\n\n
    getDateRuleType()\n
    '''
def getRuleMonth():
    '''returns int\n\n
    getRuleMonth()\n
    '''
def getRuleDayOfMonth():
    '''returns int\n\n
    getRuleDayOfMonth()\n
    '''
def getRuleDayOfWeek():
    '''returns int\n\n
    getRuleDayOfWeek()\n
    '''
def getRuleWeekInMonth():
    '''returns int\n\n
    getRuleWeekInMonth()\n
    '''
def getTimeRuleType():
    '''returns int\n\n
    getTimeRuleType()\n
    '''
def getRuleMillisInDay():
    '''returns int\n\n
    getRuleMillisInDay()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
