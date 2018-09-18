def Alphabet(x):
  List= ['l','b','c','k','e','z','g','h','@','y']
  return List[x]

def encrypt(info):
  import numpy as np
  List=[]
  Listx=[]
  Data=''
  while (info>9):
    List.append(Alphabet(int(info%10)))
    info=info/10
  List.append(Alphabet(int(info%10)))
  n= len(List)
  for i in range(n):
    Listx.append(List[n-i-1])
  for i in range(n):
    Data+=str(int(np.random.rand()*info*2.85))+Listx[i]
  Data+=str(int(np.random.rand()*info*10))+Alphabet(int(np.random.rand()*info*2))
  return Data

