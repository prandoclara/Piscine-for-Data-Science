def NULL_not_found(object: any) -> int:
  if object is None:
    print(f"Nothing : None {type(object)}")
  elif type(object) == float and object != object: # NAN = la seule valeur au monde qui n'est pas egale a elle-meme, hack connu pour detecter Nan
    print(f"Cheese : nan {type(object)}")
  elif type(object) is int and object == 0:
    print(f"Zero: 0 {type(object)}")
  elif object == "":
    print(f"Empty: {type(object)}")
  elif object is False: 
    print(f"Fake: False {type(object)}")
  else:
    print("Type not found")
  return 1

