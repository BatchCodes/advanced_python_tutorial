#! /usr/bin/python3

from a_utils import (
    DemoException,
    dangerousMain,
)


def safeMain():
  try:
    print("Before")
    raise Exception()
    dangerousMain()
  except DemoException as e:
    print("Handling Error")
    print(f"It failed this time {e.value:.4f}")
  finally:
    print("Finally")

  print("After")


if __name__ == "__main__":
  safeMain()
