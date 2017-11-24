def replaceAll(str,key,val):
  d = str.split(key)
  return val.join(d)

class String:
  str = ""
  bstr = ""
  length = len(str)
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
  def l():
    return len(str)
  def replace(i,v):
    str = str.replace(i,v,1)
    return str
  def r(i,v):
    str = str.replace(i,v,1)
    return str
  def pyformat(*vars)
    return str.format(*vars)
  def lenm(num):
    return len(str) - num
  def lena(num):
    return len(str) + num
  def lent(num):
    return len(str) * num
  def lend(num):
    return len(str) / num
  def set(stri):
    str = stri
  def bomb():
    str = ""
  def bstra(action="delete",data=""):
    if action == "delete":
      bstr = ""
      str = ""
      return bstr,str
    elif action == "return":
      return bstr,str
    elif action == "append":
      bstr = bstr + data
      return bstr,str
    elif action == "get":
      return bstr,str
    else:
      return false,"Error: Invalid action."
  def get():
    return str

class File:
  str = ""
  bstr = ""
  length = len(str)
  def __init__(file):
    str = open(file,"r").read()
    bstr = str
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
  def l():
    return len(str)
  def replace(i,v):
    str = str.replace(i,v,1)
    return str
  def r(i,v):
    str = str.replace(i,v,1)
    return str
  def pyformat(*vars)
    return str.format(*vars)
  def lenm(num):
    return len(str) - num
  def lena(num):
    return len(str) + num
  def lent(num):
    return len(str) * num
  def lend(num):
    return len(str) / num
  def set(stri):
    str = stri
  def bomb():
    str = ""
  def bstra(action="delete",data=""):
    if action == "delete":
      bstr = ""
      str = ""
      return bstr,str
    elif action == "return":
      return bstr,str
    elif action == "append":
      bstr = bstr + data
      return bstr,str
    elif action == "get":
      return bstr,str
    else:
      return false,"Error: Invalid action."
  def get():
    return str
