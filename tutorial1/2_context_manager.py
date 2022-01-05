#! /usr/bin/python3

class NewException(BaseException):
  pass


class Context:
  def __enter__(self):
    print("Entering")
    return None

  def __exit__(self, errorType, value, traceback):
    if errorType == NewException:
      print("Handling Error")
      return True
    else:
      print("Exiting")


class FileContext:
  def __init__(self, name, method):
    self.file = open(name, method)

  def __enter__(self):
    print("Entering")
    return self.file

  def __exit__(self, errorType, value, traceback):
    print("Exiting")
    self.file.close()


PART = 1

if __name__ == "__main__":
  if PART == 1:

    with Context():
      print("Hello")

      raise NewException()

  elif PART == 2:
    with Context() as thing:
      print(f"{thing=}")

  elif PART == 3:
    with FileContext('file.txt', 'w') as f:
      print('Writing')
      f.write('Hello')
      raise
