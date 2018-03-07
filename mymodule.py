# mymodule.py
import pdb

def test ():
  pdb.set_trace()
  name = "Narf"
  print(name[10])
  print("done")
  
if __name__ == '__main__':
  test()