n=25
db=len(bin(n)[2:])
print(db)
st="{0:"+str(db)+"d} {1:"+str(db)+"o} {2:"+str(db)+"X} {3:"+str(db)+"b}"
for i in range(1,n+1):
  print(st.format(i,i,i,i))