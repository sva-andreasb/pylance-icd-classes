def VEvent():
'''public VEvent()
public VEvent(final boolean initialise)
public VEvent(final PropertyList properties)
public VEvent(final PropertyList properties, final ComponentList<VAlarm> alarms)
public VEvent(final Date start, final String summary)
public VEvent(final Date start, final Date end, final String summary)
public VEvent(final Date start, final TemporalAmount duration, final String summary)
'''
pass
def getAlarms():
'''public final ComponentList<VAlarm> getAlarms()
'''
pass
def toString():
'''public final String toString()
'''
pass
def validate():
'''public final void validate(final boolean recurse)
'''
pass
def getConsumedTime():
'''public final PeriodList getConsumedTime(final Date rangeStart, final Date rangeEnd)
public final PeriodList getConsumedTime(final Date rangeStart, final Date rangeEnd, final boolean normalise)
'''
pass
def getOccurrence():
'''public final VEvent getOccurrence(final Date date)
'''
pass
def getClassification():
'''public final Clazz getClassification()
'''
pass
def getCreated():
'''public final Created getCreated()
'''
pass
def getDescription():
'''public final Description getDescription()
'''
pass
def getStartDate():
'''public final DtStart getStartDate()
'''
pass
def getGeographicPos():
'''public final Geo getGeographicPos()
'''
pass
def getLastModified():
'''public final LastModified getLastModified()
'''
pass
def getLocation():
'''public final Location getLocation()
'''
pass
def getOrganizer():
'''public final Organizer getOrganizer()
'''
pass
def getPriority():
'''public final Priority getPriority()
'''
pass
def getDateStamp():
'''public final DtStamp getDateStamp()
'''
pass
def getSequence():
'''public final Sequence getSequence()
'''
pass
def getStatus():
'''public final Status getStatus()
'''
pass
def getSummary():
'''public final Summary getSummary()
'''
pass
def getTransparency():
'''public final Transp getTransparency()
'''
pass
def getUrl():
'''public final Url getUrl()
'''
pass
def getRecurrenceId():
'''public final RecurrenceId getRecurrenceId()
'''
pass
def getEndDate():
'''public final DtEnd getEndDate()
public final DtEnd getEndDate(final boolean deriveFromDuration)
'''
pass
def getDuration():
'''public final Duration getDuration()
'''
pass
def getUid():
'''public final Uid getUid()
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
def Factory():
'''public Factory()
'''
pass
def createComponent():
'''public VEvent createComponent()
public VEvent createComponent(final PropertyList properties)
public VEvent createComponent(final PropertyList properties, final ComponentList subComponents)
'''
pass
