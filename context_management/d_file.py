#! /usr/bin/python3
import os
from a_utils import (
    dangerousOperation,
    DemoException,
)

FILE_PATH = os.path.join(os.path.dirname(__file__), "if.txt")


class FileHandler:
  def __init__(self, filePath, method):
    self.file = open(filePath, method)

  def __enter__(self):
    return self.file

  def __exit__(self, errorType, value, traceback):
    self.file.close()
    if errorType == DemoException:
      print(f"It failed this time {value.value:.4f}")
      print(str(traceback))
      return True
    if errorType:
      print("Not Demo Exception \n")
    else:
      print("No Error \n")
    return True


if __name__ == "__main__":
  # try:
  #   file = open(FILE_PATH, "w")
  #   for i in range(10):
  #     dangerousOperation()
  #     file.write(f"{i}\n")
  # except DemoException as e:
  #   print(f"Handling Error {e.value:.4f}")
  # finally:
  #   file.close()
  with FileHandler(FILE_PATH, "w") as file:
    for i in range(10):
      dangerousOperation()
      file.write(f"{i}\n")
