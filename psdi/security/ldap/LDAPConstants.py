LDAPUSER_DTDFILENAME = "String  \"ldapuser.dtd\""
LDAPGROUP_DTDFILENAME = "String  \"ldapgroup.dtd\""
LDAP_GROUP = "String  \"GroupMapping\""
LDAP_USER = "String  \"UserMapping\""
LDAP_PARAM = "String  \"SynchParameter\""
LDAP_ADAPTER = "String  \"SynchAdapter\""
LDAP_CLASS = "String  \"SynchClass\""
LDAP_CREDENTIAL = "String  \"Credential\""
LDAP_PRINCIPAL = "String  \"Principal\""
LDAP_SSL = "String  \"SSLEnabled\""
LDAP_PORT = "String  \"Port\""
LDAP_HOST = "String  \"Host\""
LDAP_HOST_VAL = "String  \"myldapserverhost\""
LDAP_PARAM_VAL = "String  \"globalcatalogport=3268\""
LDAP_ADAPTER_VAL = "String  \"psdi.security.ldap.DefaultLdapSyncAdapter\""
LDAP_CLASS_VAL = "String  \"psdi.security.ldap.ads.ActiveDirectorySynchronizer\""
LDAP_PRINCIPAL_VAL = "String  \"cn=principaluser,dc=mydomain,dc=com\""
LDAP_SSL_VAL = "String  \"0\""
LDAP_PORT_VAL = "String  \"389\""
LDAP_USER_VAL = "String  \"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><!DOCTYPE ldapsync SYSTEM \\"ldapuser.dtd\\"><ldapsync><user> <basedn>ou=allmaximousers,dc=mydomain,dc=com</basedn> <filter>(&amp;(objectCategory=person)(objectClass=user))</filter> <scope>subtree</scope> <attributes>  <attribute>sAMAccountName</attribute>  <attribute>givenName</attribute>  <attribute>sn</attribute>  <attribute>displayName</attribute>  <attribute>streetAddress</attribute>  <attribute>homePhone</attribute>  <attribute>memberOf</attribute>  <attribute>telephoneNumber</attribute>  <attribute>mail</attribute>  <attribute>st</attribute>  <attribute>postalCode</attribute>  <attribute>c</attribute>  <attribute>l</attribute> </attributes> <datamap>  <table name=\\"MAXUSER\\">   <keycolumn name=\\"USERID\\" type=\\"UPPER\\">sAMAccountName</keycolumn>   <column name=\\"LOGINID\\" type=\\"ALN\\">sAMAccountName</column>   <column name=\\"PERSONID\\" type=\\"UPPER\\">sAMAccountName</column>  </table>  <table name=\\"PERSON\\">   <keycolumn name=\\"PERSONID\\" type=\\"UPPER\\">sAMAccountName</keycolumn>   <column name=\\"FIRSTNAME\\" type=\\"ALN\\">givenName</column>   <column name=\\"LASTNAME\\" type=\\"ALN\\">sn</column>   <column name=\\"DISPLAYNAME\\" type=\\"ALN\\">displayName</column>   <column name=\\"ADDRESSLINE1\\" type=\\"ALN\\">streetAddress</column>   <column name=\\"STATEPROVINCE\\" type=\\"ALN\\">st</column>   <column name=\\"CITY\\" type=\\"ALN\\">l</column>   <column name=\\"POSTALCODE\\" type=\\"ALN\\">postalCode</column>   <column name=\\"COUNTRY\\" type=\\"ALN\\">c</column>   <column name=\\"STATUSDATE\\" type=\\"ALN\\">{:sysdate}</column>  </table>  <table allowdelete=\\"true\\" name=\\"PHONE\\">   <keycolumn name=\\"PERSONID\\" type=\\"UPPER\\">sAMAccountName</keycolumn>   <keycolumn name=\\"TYPE\\" type=\\"ALN\\">{Work}</keycolumn>   <keycolumn name=\\"ISPRIMARY\\" type=\\"YORN\\">{1}</keycolumn>   <column name=\\"PHONENUM\\" required=\\"true\\" type=\\"ALN\\">telephoneNumber</column>  </table>  <table allowdelete=\\"true\\" name=\\"PHONE\\">   <keycolumn name=\\"PERSONID\\" type=\\"UPPER\\">sAMAccountName</keycolumn>   <keycolumn name=\\"TYPE\\" type=\\"ALN\\">{Home}</keycolumn>   <keycolumn name=\\"ISPRIMARY\\" type=\\"YORN\\">{0}</keycolumn>   <column name=\\"PHONENUM\\" required=\\"true\\" type=\\"ALN\\">homePhone</column>  </table>  <table allowdelete=\\"true\\" name=\\"EMAIL\\">   <keycolumn name=\\"PERSONID\\" type=\\"UPPER\\">sAMAccountName</keycolumn>   <keycolumn name=\\"TYPE\\" type=\\"ALN\\">{Work}</keycolumn>   <keycolumn name=\\"ISPRIMARY\\" type=\\"YORN\\">{1}</keycolumn>   <column name=\\"EMAILADDRESS\\" required=\\"true\\" type=\\"ALN\\">mail</column>  </table> </datamap></user></ldapsync>\""
LDAP_GROUP_VAL = "String  \"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><!DOCTYPE ldapsync SYSTEM \\"ldapgroup.dtd\\"><ldapsync>    <group>        <basedn>ou=allmaximogroups,dc=mydomain,dc=com</basedn>        <filter>(&amp;(objectCategory=Group)(objectClass=group))</filter>        <scope>subtree</scope>        <attributes>            <attribute>sAMAccountName</attribute>            <attribute>description</attribute>            <attribute>memberOf</attribute>        </attributes>        <datamap>            <table name=\\"MAXGROUP\\">                <keycolumn name=\\"GROUPNAME\\" type=\\"UPPER\\">sAMAccountName</keycolumn>                <column name=\\"DESCRIPTION\\" type=\\"ALN\\">description</column>            </table>        </datamap>        <memberdatamap>            <membertable name=\\"GROUPUSER\\">                <keycolumn name=\\"GROUPNAME\\" type=\\"UPPER\\">sAMAccountName</keycolumn>                <membercolumn name=\\"USERID\\" type=\\"UPPER\\">                    <member>member</member>                    <memberuser>sAMAccountName</memberuser>                    <membergroup>sAMAccountName</membergroup>                </membercolumn>                <column name=\\"GROUPUSERID\\" type=\\"INTEGER\\">{:uniqueid}</column>            </membertable>        </memberdatamap>    </group></ldapsync>\""
