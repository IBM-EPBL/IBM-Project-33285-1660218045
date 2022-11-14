import ibm_db
# conn= ibm_db.connect("DATABASE=XXXXX;HOSTNAME=XXXXXX;PORT=XXXXX;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=XXXXX;PWD=XXXXXX",'','')
#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xlv63468;PWD=MtP5ek11x8XcsWHN","","")
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=31249;SECURITY=SSL;SSLSererCertificate=DigiCertGlobalRootCA.crt;UID=rzl30414;PWD=yMzTHnTnEpxoKqFd",'','')
sql= "SELECT * FROM SIGNUP"
stmt= ibm_db.exec_immediate(conn,sql)
dictionary= ibm_db.fetch_assoc(stmt)
print(dictionary)