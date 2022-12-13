BEGIN = "String  \"BEGIN\""
END = "String  \"END\""
VEVENT = "String  \"VEVENT\""
VTODO = "String  \"VTODO\""
VJOURNAL = "String  \"VJOURNAL\""
VFREEBUSY = "String  \"VFREEBUSY\""
VTIMEZONE = "String  \"VTIMEZONE\""
VALARM = "String  \"VALARM\""
VAVAILABILITY = "String  \"VAVAILABILITY\""
VVENUE = "String  \"VVENUE\""
AVAILABLE = "String  \"AVAILABLE\""
EXPERIMENTAL_PREFIX = "String  \"X-\""
def toString():
    '''public String toString()
    '''
def getName():
    '''public final String getName()
    '''
def getProperties():
    '''public final PropertyList<Property> getProperties()
    public final <C extends Property> PropertyList<C> getProperties(final String name)
    '''
def getProperty():
    '''public final <T extends Property> T getProperty(final String name)
    '''
def validate():
    '''public final void validate()
    '''
def equals():
    '''public boolean equals(final Object arg0)
    '''
def hashCode():
    '''public int hashCode()
    '''
def copy():
    '''public Component copy()
    '''
def calculateRecurrenceSet():
    '''public final PeriodList calculateRecurrenceSet(final Period period)
    '''
