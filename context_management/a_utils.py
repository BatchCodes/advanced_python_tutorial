#! /usr/bin/python3

from random import random

RAISE_THRESHOLD = 0.1


class DemoException(Exception):
  def __init__(self, value):
    self.value = value


def dangerousOperation():
  value = random()
  if value < RAISE_THRESHOLD:
    raise DemoException(value)
  print(f"It worked this time {value:.4f}")


def dangerousMain():
  print("Starting dangerousMain \n")
  for _ in range(10):
    dangerousOperation()


if __name__ == "__main__":
  dangerousMain()
