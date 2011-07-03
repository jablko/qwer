import re, sys, untwisted

__all__ = 'rule', 'qwer'

def select(name, *args):
  for itm in args:
    for itm in itm[1]:
      if '>' == name[0]:
        if name[1] == itm[0]:
          if 2 < len(name):
            name = name[2:]

          else:
            yield itm[1]

            continue

        else:
          continue

      elif name[0] == itm[0]:
        if 1 < len(name):
          name = name[1:]

        else:
          yield itm[1]

      for itm in select(name, itm[1]):
        yield itm

class poiu:
  __metaclass__ = type

  def __init__(ctx, match, *args):
    ctx.match = match
    ctx.args = args

  def mnbv(ctx, e, name):
    try:
      name = re.findall('>|[^\s>]+', name)

    except TypeError:
      return poiu(ctx.match, ctx.args[name])

    a = list(select(name, *ctx.args))
    if not a:
      raise e

    return poiu(ctx.match, *filter(lambda itm: ctx.match.group(itm[0]), a))

  __getattr__ = untwisted.partial(mnbv, AttributeError)
  __getitem__ = untwisted.partial(mnbv, KeyError)

  __int__ = lambda ctx: int(ctx.match.group(ctx.args[0][0]))
  __len__ = lambda ctx: ctx.match.end(ctx.args[0][0]) - ctx.match.start(ctx.args[0][0])
  __nonzero__ = lambda ctx: bool(ctx.args)
  __str__ = lambda ctx: ctx.match.group(ctx.args[0][0])

class rule:
  def __init__(ctx, name):
    ctx.namespace = sys._getframe().f_back.f_locals
    ctx.name = name.split('.')

  def compile(ctx, group, *args):
    qwer = reduce(getattr, ctx.name[1:], ctx.namespace[ctx.name[0]])

    a = []
    b = False
    c = False
    for itm in args:
      if ctx.name[-1] == itm[0]:
        if isinstance(itm[-1], str):
          if 1 < len(itm):
            a.append(itm[1:])

          else:
            group += 1

            a.append(itm)

            b = True

        elif 2 < len(itm):
          a.append(itm[1:])

        else:
          group += 1

          d = list(itm[:-1])
          d.append(())
          a.append(d)

          a.extend(itm[-1])

          b = True
          c = True

      else:
        a.append(itm)

    e = group
    group, pattern, f, g = qwer.compile(group, *a)

    if b:
      h = e, f

      if c:
        g.insert(0, h)

      return group, '(' + pattern + ')', [(ctx.name[-1], h)], g

    return group, pattern, f, g

class qwer:
  def __init__(ctx, *args):
    ctx.args = args

  def compile(ctx, group, *args):
    pattern = []
    a = []
    b = []
    for itm in ctx.args:
      try:
        group, itm, c, d = itm.compile(group, *args)

      except AttributeError:
        pass

      else:
        a.extend(c)
        b.extend(d)

      pattern.append(itm)

    return group, ''.join(pattern), a, b

  def lkjh(ctx, jhgf, subject, *args):
    a = []
    b = False
    for itm in args:
      match = re.match('\((.+)\)|(.+?)(?:\((.+)\))?$', itm)
      if match.group(1):
        a.extend(map(untwisted.partial(re.findall, '>|[^\s>]+'), re.split(',', match.group(1))))

      else:
        c = re.findall('>|[^\s>]+', match.group(2))
        c.append(map(untwisted.partial(re.findall, '>|[^\s>]+'), re.split(',', match.group(3))) if match.group(3) else ())
        a.append(c)

        b = True

    _, pattern, d, e = ctx.compile(0, *a)

    match = jhgf(pattern, subject)
    if not match:
      raise ValueError

    if b:
      return poiu(match, *filter(lambda itm: match.group(itm[0]), e))

    return poiu(match, (0, d))

  match = untwisted.partial(lkjh, re.match)
  search = untwisted.partial(lkjh, re.search)

  def replace(ctx, replace, subject, *args, **kwds):
    a = []
    b = False
    for itm in args:
      match = re.match('\((.+)\)|(.+?)(?:\((.+)\))?$', itm)
      if match.group(1):
        a.extend(map(untwisted.partial(re.findall, '>|[^\s>]+'), re.split(',', match.group(1))))

      else:
        c = re.findall('>|[^\s>]+', match.group(2))
        c.append(map(untwisted.partial(re.findall, '>|[^\s>]+'), re.split(',', match.group(3))) if match.group(3) else ())
        a.append(c)

        b = True

    _, pattern, d, e = ctx.compile(0, *a)

    if callable(replace):
      if b:
        f = lambda match: replace(poiu(match, *filter(lambda itm: match.group(itm[0]), e)))

      else:
        f = lambda match: replace(poiu(match, (0, d)))

    else:
      f = replace

    try:
      return re.sub(pattern, f, subject, kwds['count'])

    except KeyError:
      return re.sub(pattern, f, subject)
