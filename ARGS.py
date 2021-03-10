def courses(*args):
  for subject in args:
    print(subject)
courses("Big Data","CCNA","OOP2")
def courses(*args):
  for subject in args:
    return subject
print(courses("Big Data","CCNA","OOP2"))