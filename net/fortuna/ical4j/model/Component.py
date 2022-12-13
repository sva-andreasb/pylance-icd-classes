BEGIN = "String  BEGIN""
END = "String  END""
VEVENT = "String  VEVENT""
VTODO = "String  VTODO""
VJOURNAL = "String  VJOURNAL""
VFREEBUSY = "String  VFREEBUSY""
VTIMEZONE = "String  VTIMEZONE""
VALARM = "String  VALARM""
VAVAILABILITY = "String  VAVAILABILITY""
VVENUE = "String  VVENUE""
AVAILABLE = "String  AVAILABLE""
EXPERIMENTAL_PREFIX = "String  X-""
def toString():
'''public String toString()
'''
pass
def getName():
'''public final String getName()
'''
pass
def getProperties():
'''public final PropertyList<Property> getProperties()
public final <C extends Property> PropertyList<C> getProperties(final String name)
'''
pass
def getProperty():
'''public final <T extends Property> T getProperty(final String name)
'''
pass
def validate():
'''public final void validate()
'''
pass
def equals():
'''public boolean equals(final Object arg0)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def copy():
'''public Component copy()
'''
pass
def calculateRecurrenceSet():
'''public final PeriodList calculateRecurrenceSet(final Period period)
'''
pass
