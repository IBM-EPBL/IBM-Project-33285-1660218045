import ibm_db
# conn= ibm_db.connect("DATABASE=XXXXX;HOSTNAME=XXXXXX;PORT=XXXXX;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=XXXXX;PWD=XXXXXX",'','')
#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xlv63468;PWD=MtP5ek11x8XcsWHN","","")
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLSererCertificate=DigiCertGlobalRootCA.crt;UID=xlv63468;PWD=hSfXKl6zJkX3zQk3",'','')
sql= "SELECT * FROM SIGNUP"
stmt= ibm_db.exec_immediate(conn,sql)
dictionary= ibm_db.fetch_assoc(stmt)
print(dictionary)