#! /usr/bin/python3

from a_utils import (
    DemoException,
    dangerousMain,
)


class SafeMain:
  def __init__(self):
    print("init")

  def __enter__(self):
    print("enter")
    return "thing from enter"

  def __exit__(self, errorType, value, traceback):
    print(f"{errorType=}")
    print(f"{value=}")
    print(f"{traceback=}")
    if errorType == DemoException:
      print(f"It failed this time {value.value:.4f}")
      print(str(traceback))
      return True

    if errorType:
      print("Not Demo Exception \n")
    else:
      print("No Error \n")

    # return True


if __name__ == "__main__":
  with SafeMain() as thing:
    # print(f"{thing=}")
    # dangerousMain()
    raise Exception()
    # pass
  print("helloooooo")

try:
  pass
except:
  pass
