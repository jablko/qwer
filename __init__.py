import re, sys, untwisted

__all__ = 'rule', 'qwer'

def select(ctx, *args):
  a = []

  try:
    itm = ctx[1][0]

  except IndexError:
    pass

  else:
    b = True
    for name in args:
      #head, *rest = name
      head, rest = name[0], name[1:]

      if '+' == head:
        continue

      if '>' == head:
        #head, *rest = rest
        head, rest = rest[0], rest[1:]

        if (not head.endswith(':first-child') or 12 < len(head) and '*' != head[:-12] and head[:-12] != itm[0]) and '*' != head and head != itm[0]:
          continue

        if rest:
          a.append(rest)

          continue

        if b:
          yield itm[1]

          b = False

        continue

      if (not head.endswith(':first-child') or 12 < len(head) and '*' != head[:-12] and head[:-12] != itm[0]) and '*' != head and head != itm[0]:
        a.append(name)

        continue

      if rest:
        a.append(rest)

        continue

      a.append(name)

      if b:
        yield itm[1]

        b = False

    c = select(itm[1], *a)
    try:
      while True:
        yield c.next()

    except StopIteration as e:
      a = list(e.args)

  for itm in ctx[1][1:]:
    b = True
    for name in args:
      #head, *rest = name
      head, rest = name[0], name[1:]

      if '+' == head:
        continue

      if '>' == head:
        #head, *rest = rest
        head, rest = rest[0], rest[1:]

        if head.endswith(':first-child') or '*' != head and head != itm[0]:
          continue

        if rest:
          a.append(rest)

          continue

        if b:
          yield itm[1]

          b = False

        continue

      if head.endswith(':first-child') or '*' != head and head != itm[0]:
        a.append(name)

        continue

      if rest:
        a.append(rest)

        continue

      a.append(name)

      if b:
        yield itm[1]

        b = False

    c = select(itm[1], *a)
    try:
      while True:
        yield c.next()

    except StopIteration as e:
      a = list(e.args)

  try:
    itm = ctx[2]

  except IndexError:
    pass

  else:
    a = []
    b = True
    for name in args:
      #head, *rest = name
      head, rest = name[0], name[1:]

      if '+' == head:
        #head, *rest = rest
        head, rest = rest[0], rest[1:]

        if head.endswith(':first-child') or '*' != head and head != itm[0]:
          continue

        if rest:
          a.append(rest)

          continue

        if b:
          yield itm[1]

          b = False

    #return ...
    raise StopIteration(*a)

class poiu:
  __metaclass__ = type

  def __init__(ctx, match, *args):
    ctx.match = match
    ctx.args = args

  def mnbv(ctx, e, name):
    try:
      name = map(untwisted.partial(re.findall, '\+|>|[^\s+>]+'), re.split(',', name))

    except TypeError:
      return poiu(ctx.match, ctx.args[name])

    a = []
    for itm in ctx.args:
      a.extend(select(itm, *name))

    if not a:
      raise e

    return poiu(ctx.match, *filter(lambda itm: ctx.match.group(itm[0]), a))

  __getattr__ = untwisted.partial(mnbv, AttributeError)
  __getitem__ = untwisted.partial(mnbv, KeyError)

  def __int__(ctx):
    try:
      return int(ctx.match.group(ctx.args[0][0]))

    except IndexError:
      raise ValueError

  __len__ = lambda ctx: ctx.match.end(ctx.args[0][0]) - ctx.match.start(ctx.args[0][0])
  __nonzero__ = lambda ctx: bool(ctx.args)

  def __str__(ctx):
    try:
      return ctx.match.group(ctx.args[0][0])

    except IndexError:
      return ''

  join = lambda ctx, separator: separator.join(map(str, ctx))

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
      #head, *rest = itm
      head, rest = itm[0], itm[1:]
      try:
        #*d, e = rest
        d, e = rest[:-1], rest[-1]

      except IndexError:
        #head, *rest = head
        head, rest = head[0], head[1:]
        if ctx.name[-1] == head:
          if rest:
            a.append((rest,))

            continue

          group += 1

          a.append(itm)

          b = True

          continue

      else:
        if ctx.name[-1] == head:
          if d:
            a.append(rest)

            continue

          group += 1

          a.append((head, ()))
          a.extend(e)

          b = True
          c = True

          continue

      a.append(itm)

    e = group
    group, pattern, f, g = qwer.compile(group, *a)

    if b:
      h = iter(f)
      i = iter(f[1:])
      while True:
        try:
          h.next()[1].append(i.next())

        except StopIteration:
          break

      h = [e, f]

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

    # Guaranteed to match *any* string
    pattern = re.compile('([^,]*?)\((.*?)\)|([^,]*)')

    for itm in args:

      # Zero length match only between commas
      match = pattern.match(itm)
      while True:
        try:
          c = re.findall('\+|>|[^\s+>]+', match.group(1))

        except TypeError:
          c = re.findall('\+|>|[^\s+>]+', match.group(3))
          c.append(())

          a.append(c)

          b = True

        else:
          d = map(untwisted.compose(lambda *args: args, untwisted.partial(re.findall, '\+|>|[^\s+>]+')), re.split(',', match.group(2)))
          if c:
            c.append(d)

            a.append(c)

            b = True

          else:
            a.extend(d)

        if not len(itm) > match.end():
          break

        match = pattern.match(itm, match.end() + 1)

    _, pattern, d, e = ctx.compile(0, *a)

    match = jhgf(pattern, subject)
    if not match:
      raise ValueError

    if b:
      return poiu(match, *filter(lambda itm: match.group(itm[0]), e))

    f = iter(d)
    g = iter(d[1:])
    while True:
      try:
        f.next()[1].append(g.next())

      except StopIteration:
        break

    return poiu(match, [0, d])

  match = untwisted.partial(lkjh, re.match)
  search = untwisted.partial(lkjh, re.search)

  def replace(ctx, replace, subject, *args, **kwds):
    a = []
    b = False

    # Guaranteed to match *any* string
    pattern = re.compile('([^,]*?)\((.*?)\)|([^,]*)')

    for itm in args:

      # Zero length match only between commas
      match = pattern.match(itm)
      while True:
        try:
          c = re.findall('\+|>|[^\s+>]+', match.group(1))

        except TypeError:
          c = re.findall('\+|>|[^\s+>]+', match.group(3))
          c.append(())

          a.append(c)

          b = True

        else:
          d = map(untwisted.compose(lambda *args: args, untwisted.partial(re.findall, '\+|>|[^\s+>]+')), re.split(',', match.group(2)))
          if c:
            c.append(d)

            a.append(c)

            b = True

          else:
            a.extend(d)

        if not len(itm) > match.end():
          break

        match = pattern.match(itm, match.end() + 1)

    _, pattern, d, e = ctx.compile(0, *a)

    if callable(replace):
      if b:
        f = lambda match: replace(poiu(match, *filter(lambda itm: match.group(itm[0]), e)))

      else:
        f = iter(d)
        g = iter(d[1:])
        while True:
          try:
            f.next()[1].append(g.next())

          except StopIteration:
            break

        f = lambda match: replace(poiu(match, [0, d]))

    else:
      f = replace

    try:
      return re.sub(pattern, f, subject, kwds['count'])

    except KeyError:
      return re.sub(pattern, f, subject)
