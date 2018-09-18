def number(x):
  List=['0','1','2','3','4','5','6','7','8','9']
  for i in range(len(List)):
    if x==List[i]:
      return 'True'
  return 'False'

def DAlphabet(x):
  List= ['l','b','c','k','e','z','g','h','@','y']
  for i in range(len(List)):
    if x==List[i]:
      return i

def decrypt(info):
  n=len(info)
  i=1
  datax=''
  while (number(info[n-i-1])=='True'):    
    i+=1 
  data=info[:n-i]
  for i in range(len(data)):
    if (number(info[i])=='False'):
      datax+=str(DAlphabet(info[i]))
      
  return datax
