COPYRIGHT = "String  CopyRight.COPYRIGHT"
TABLE_TLOAMDPAINVSOURCE = "String  TLOAMDPAINVSOURCE""
ATT_TLOAMDPAINVSOURCE_INVSOURCE = "String  invsource""
ATT_TLOAMDPAINVSOURCE_ISACTIVE = "String  isactive""
ATT_TLOAMDPAINVSOURCE_LASTUPLOADEDTIME = "String  lastuploadedtime""
ATT_TLOAMDPAINVSOURCE_LASTPROCESSINGTIME = "String  lastprocessingtime""
REL_TLOAMSOFTWARE = "String  TLOAMSOFTWARE""
TABLE_TLOAMFSNRUNSTATUS = "String  tloamfsnrunstatus""
COLUMN_TLOAMFSNRUNSTATUS_MAPPINGNAME_INDEX = "int  1"
COLUMN_TLOAMFSNRUNSTATUS_ENDTIME = "int  2"
COLUMN_TLOAMFSNRUNSTATUS_FAILED = "int  3"
QUERY_SQL_TLOAMFSNRUNSTATUS = "SqlFormat  new SqlFormat("select mappingname, endtime, failed from tloamfsnrunstatus")"