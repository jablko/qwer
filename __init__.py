import re, sys, untwisted

__all__ = 'rule', 'qwer'

def select(name, *args):
  for itm in args:
    if name[0] == itm[0]:
      if 1 < len(name):
        name = name[1:]

      else:
        yield itm[1]

    for itm in select(name, *itm[1][1]):
      yield itm

class poiu:
  __metaclass__ = type

  def __init__(ctx, match, *args):
    ctx.match = match
    ctx.args = args

  def mnbv(ctx, e, name):
    try:
      name = re.split('\s+', name)

    except TypeError:
      return poiu(ctx.match, ctx.args[name])

    a = []
    for itm in ctx.args:
      a.extend(select(name, *itm[1]))

    if not a:
      raise e

    return poiu(ctx.match, *filter(lambda itm: ctx.match.group(itm[0]), a))

  __getattr__ = untwisted.partial(mnbv, AttributeError)
  __getitem__ = untwisted.partial(mnbv, KeyError)

  __int__ = lambda ctx: int(ctx.match.group(ctx.args[0][0]))
  __len__ = lambda ctx: ctx.match.end(ctx.args[0][0]) - ctx.match.start(ctx.args[0][0])
  __str__ = lambda ctx: ctx.match.group(ctx.args[0][0])

class rule:
  def __init__(ctx, name):
    ctx.namespace = sys._getframe().f_back.f_locals
    ctx.name = name.split('.')

  def compile(ctx, *args):
    qwer = reduce(getattr, ctx.name[1:], ctx.namespace[ctx.name[0]])

    a = False
    b = list(args[:1])
    for itm in args[1:]:
      if ctx.name[-1] == itm[0]:
        if 1 < len(itm):
          itm = itm[1:]

        else:
          a = True

      b.append(itm)

    pattern, b = qwer.compile(*b)
    if a:
      c = args[0][-1][0] + 1, b
      args[0].append(c)

      return '(' + pattern + ')', ((ctx.name[-1], c),)

    return pattern, b

class qwer:
  def __init__(ctx, *args):
    ctx.args = args

  def compile(ctx, *args):
    pattern = []
    b = []
    for itm in ctx.args:
      try:
        itm, c = itm.compile(*args)

      except AttributeError:
        pass

      else:
        b.extend(c)

      pattern.append(itm)

    return ''.join(pattern), b

  def lkjh(ctx, jhgf, subject, *args):
    a = [(0, [])]
    pattern, _ = ctx.compile(a, *map(untwisted.partial(re.split, '\s+'), args))
    if args:
      a.pop(0)

    match = jhgf(pattern, subject)
    if not match:
      raise ValueError

    return poiu(match, *filter(lambda itm: match.group(itm[0]), a))

  match = untwisted.partial(lkjh, re.match)
  search = untwisted.partial(lkjh, re.search)
