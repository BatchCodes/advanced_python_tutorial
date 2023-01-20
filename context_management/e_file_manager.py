#! /usr/bin/python3

import os
from a_utils import (
    dangerousOperation,
    DemoException,
)

FILE_PATH = os.path.join(os.path.dirname(__file__), "if.txt")


class FileContext:
  def __init__(self, path, method):
    self.path = path
    self.method = method
    self.count = 0
    self.failingValues = dict()
    with open(self.path, "w") as file:
      file.write("Creating Context Manager\n")

  def __enter__(self):
    self.count += 1
    self.file = open(self.path, self.method)
    self.file.write(f"Entering {self.count}\n")
    return self.file

  def __exit__(self, errorType, value, traceback):
    self.file.close()
    if errorType == DemoException:
      print(f"Handling Error {value.value:.4f}")
      self.failingValues[self.runNumber] = value.value
      return True

  def __call__(self, runNumber):
    self.runNumber = runNumber
    return self


if __name__ == "__main__":
  fileContext = FileContext(FILE_PATH, "a")

  def write(run):
    with fileContext(run) as file:
      for i in range(10):
        dangerousOperation()
        file.write(f"{i}\n")

  for j in range(14):
    write(j)

  print(f"\n{fileContext.failingValues=}")
