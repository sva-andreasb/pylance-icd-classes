def VEvent():
    '''public VEvent()
    public VEvent(final boolean initialise)
    public VEvent(final PropertyList properties)
    public VEvent(final PropertyList properties, final ComponentList<VAlarm> alarms)
    public VEvent(final Date start, final String summary)
    public VEvent(final Date start, final Date end, final String summary)
    public VEvent(final Date start, final TemporalAmount duration, final String summary)
    '''
def getAlarms():
    '''public final ComponentList<VAlarm> getAlarms()
    '''
def toString():
    '''public final String toString()
    '''
def validate():
    '''public final void validate(final boolean recurse)
    '''
def getConsumedTime():
    '''public final PeriodList getConsumedTime(final Date rangeStart, final Date rangeEnd)
    public final PeriodList getConsumedTime(final Date rangeStart, final Date rangeEnd, final boolean normalise)
    '''
def getOccurrence():
    '''public final VEvent getOccurrence(final Date date)
    '''
def getClassification():
    '''public final Clazz getClassification()
    '''
def getCreated():
    '''public final Created getCreated()
    '''
def getDescription():
    '''public final Description getDescription()
    '''
def getStartDate():
    '''public final DtStart getStartDate()
    '''
def getGeographicPos():
    '''public final Geo getGeographicPos()
    '''
def getLastModified():
    '''public final LastModified getLastModified()
    '''
def getLocation():
    '''public final Location getLocation()
    '''
def getOrganizer():
    '''public final Organizer getOrganizer()
    '''
def getPriority():
    '''public final Priority getPriority()
    '''
def getDateStamp():
    '''public final DtStamp getDateStamp()
    '''
def getSequence():
    '''public final Sequence getSequence()
    '''
def getStatus():
    '''public final Status getStatus()
    '''
def getSummary():
    '''public final Summary getSummary()
    '''
def getTransparency():
    '''public final Transp getTransparency()
    '''
def getUrl():
    '''public final Url getUrl()
    '''
def getRecurrenceId():
    '''public final RecurrenceId getRecurrenceId()
    '''
def getEndDate():
    '''public final DtEnd getEndDate()
    public final DtEnd getEndDate(final boolean deriveFromDuration)
    '''
def getDuration():
    '''public final Duration getDuration()
    '''
def getUid():
    '''public final Uid getUid()
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
def Factory():
    '''public Factory()
    '''
def createComponent():
    '''public VEvent createComponent()
    public VEvent createComponent(final PropertyList properties)
    public VEvent createComponent(final PropertyList properties, final ComponentList subComponents)
    '''
