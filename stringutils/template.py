from __init__ import *
class Template extends String:
  str = ""
  bstr = ""
  def __init__(string):
    str = string
    bstr = string
  def temp(*vars):
    s = String(str)
    for i,v in *vars:
      s.replaceAll("#{" + i + "}",v)
  def tempA(*vars):
    for s in *vars:
      i = 1
      while i < len(*vars):
        s.replace("#{" + i + "}",i)
        
# temp: {varaaaaanamek}
# tempA: {1} to #{10000000000000000000000000000+}
