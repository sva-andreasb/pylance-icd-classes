def Calendar():
    '''public Calendar(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def isAvailable():
    '''public boolean isAvailable(final Date date)
    '''
def appValidate():
    '''public void appValidate()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def canApplyShift():
    '''public void canApplyShift(final ShiftRemote shift)
    public void canApplyShift(final String shiftname)
    '''
def applyShift():
    '''public void applyShift(final Vector shiftSet)
    public void applyShift(final String shiftname)
    public void applyShift(final String shiftname, final Date startdate, final Date enddate)
    '''
def setWPIncrement():
    '''public void setWPIncrement(final int i)
    '''
def applyNonWorkTime():
    '''public boolean applyNonWorkTime(final MboSetRemote nonWorkTimeSet)
    public void applyNonWorkTime(final String nonWorkType, final String description, final Date startDate, final Date endDate)
    '''
def calculateAvailability():
    '''public double calculateAvailability()
    public double calculateAvailability(final Date startDate, final Date endDate)
    '''
def calculateHours():
    '''public double calculateHours(final Date date1, final Date date2)
    '''
def calculateDownTime():
    '''public double calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)
    '''
def getDownTime():
    '''public double getDownTime(final Date currentChangeDate, final Date lastChangeDate)
    public double getDownTime(final Date currentChangeDate, final Date lastChangeDate, final TimeZone tz)
    '''
def getWorkPeriodData():
    '''public double getWorkPeriodData(final WorkPeriodSet workPeriodSet, final Date lastChangeDate, final Date currentChangeDate)
    public double getWorkPeriodData(final WorkPeriodSet workPeriodSet, final Date lastChangeDate, final Date currentChangeDate, final TimeZone tz)
    '''
def addDates():
    '''public Date addDates(final Date date, final int days)
    '''
def combineDateTime():
    '''public Date combineDateTime(final Date date, final Date time)
    public Date combineDateTime(final Date date, final Date time, final TimeZone tz)
    '''
def deleteWorkPeriod():
    '''public void deleteWorkPeriod(final Date startDate, final Date endDate)
    '''
def calculateWorkHours():
    '''public double calculateWorkHours(final Date workDate)
    '''
def getWorkPeriodSet():
    '''public WorkPeriodSetRemote getWorkPeriodSet(final Date workDate)
    '''
def getMonthsAvailableHours():
    '''public String[][] getMonthsAvailableHours(final com.ibm.icu.util.Calendar cal)
    '''
def add():
    '''public void add()
    '''
