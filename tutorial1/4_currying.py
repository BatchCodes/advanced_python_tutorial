#! /usr/bin/python3

def curriedAdd(arg1):

  def func(arg2):
    return arg1 + arg2

  return func


def curry(func):
  curry.__curried_func_name__ = func.__name__
  f_args, f_kwargs = [], {}

  def f(*args, **kwargs):
    nonlocal f_args, f_kwargs
    if args or kwargs:
      f_args += args
      f_kwargs.update(kwargs)
      return f
    else:
      result = func(*f_args, *f_kwargs)
      f_args, f_kwargs = [], {}
      return result
  return f


def mean(*args):
  return sum(args) / len(args)


PART = 2

if __name__ == "__main__":
  if PART == 1:
    print(curriedAdd(1)(3))
  elif PART == 2:
    curriedMean = curry(mean)
    print(curriedMean(1, 2, 3, 4)())
    print(curriedMean(1)(2)(3)(4)())
