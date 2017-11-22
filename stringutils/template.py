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
      s.replaceAll("!{" + i + "}",v)
