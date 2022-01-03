import sys

def reversebyte(dump,dumpout):
  c = len(dump)
  c -= 1
  for i in range (len(dump)):
    dumpout[i] += dump[c]
    i += 1
    c -= 1
  return dumpout

def openfile (s):
  sys.stderr.write(s + "\n")
  sys.stderr.write("Usage: %s <infile> <outfile>\n" % sys.argv[0])
  sys.exit(1)

if __name__ == '__main__':
  
  if len(sys.argv) != 3:
    openfile("invalid argument count")
  outfile = sys.argv.pop()
  infile  = sys.argv.pop()
  
  file = open(infile,"rb")
  
  dump = bytearray(file.read())
  dumpout = bytearray(len(dump))
  outdump = reversebyte(dump,dumpout)
  
  
  new = open(outfile,"wb")
  new.write(outdump)
  new.close()
  file.close()
