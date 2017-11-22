def replaceAll(str,key,val):
  d = str.split(key)
  return val.join(d)

class String:
  str = ""
  bstr
  def __init__(string):
    str = string
    bstr = string
  def reverse():
    return str[::-1]
  def replaceAll(key,val):
    d = str.split(key)
    str = val.join(d)
    return val.join(d)
  def appendTo(string):
    str = str + string
    return str
  def appendFileTo(file):
    str = str + open(file,"r").read()
    return str
  def sub(start,end,step):
    str = str[start:end:step]
    return str
  def format(*vars):
    for i,v in *vars:
      str = replaceAll(str,"$" + i,v)
  def reset():
    str = bstr
    return str, true
  def encode():
    str = str.encode(encoding="base64",errors="ignore")
    return str
  def decode():
    str = str.decode("base64")
    return str
  def triangle():
    str += str
    print(str)
    str = bstr
  def len():
    return len(str)
