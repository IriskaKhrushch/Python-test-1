def God():
    return [ Man("Adam"), Woman("Eva") ]

class Human:
   def __init__( self, name ):
      self.name = name

class Man( Human ):
   def __init__( self, name ):
      self.name = name

class Woman( Human ):
   def __init__( self, name ):
      self.name = name