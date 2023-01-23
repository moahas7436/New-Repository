class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def contains(self, name):
    return name in self.__myTeam
  def iter(self):
    for member in self.__myTeam:
        print(member)
def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print (len(classmates))
  print(classmates.contains('Tim'))
  print(classmates.contains('Sam'))
  print(classmates.iter())


main()


