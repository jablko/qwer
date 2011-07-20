import re, sys, untwisted

__all__ = 'repetition', 'rule', 'qwer'

class asdf:
  def __init__(ctx, group, *args, **kwds):
    ctx.group = group
    ctx.args = args

    try:
      ctx.match = kwds['match']

    except KeyError:
      pass

    try:
      ctx.sibling = kwds['sibling']

    except KeyError:
      pass

def select(ctx, match, *args):
  try:
    itm = ctx.args[0]

  except IndexError:
    pass

  else:
    a = []
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
          itm[1].match = getattr(itm[1], 'match', match)

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
        itm[1].match = getattr(itm[1], 'match', match)

        yield itm[1]

        b = False

    c = select(itm[1], getattr(itm[1], 'match', match), *a)
    try:
      while True:
        yield c.next()

    except StopIteration as e:
      a = list(e.args)

    for itm in ctx.args[1:]:
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
            itm[1].match = getattr(itm[1], 'match', match)

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
          itm[1].match = getattr(itm[1], 'match', match)

          yield itm[1]

          b = False

      c = select(itm[1], getattr(itm[1], 'match', match), *a)
      try:
        while True:
          yield c.next()

      except StopIteration as e:
        a = list(e.args)

  try:
    itm = ctx.sibling

  except AttributeError:
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
          itm[1].match = getattr(itm[1], 'match', match)

          yield itm[1]

          b = False

    #return ...
    raise StopIteration(*a)

class poiu:
  __metaclass__ = type

  def __init__(ctx, *args):
    ctx.args = args

  def mnbv(ctx, e, name):
    try:
      name = map(untwisted.partial(re.findall, '\+|>|[^\s+>]+'), re.split(',', name))

    except TypeError:
      return poiu(ctx.args[name])

    a = []
    for itm in ctx.args:
      a.extend(select(itm, itm.match, *name))

    # Any selector which could match but didn't should result in an empty
    # sequence - only a selector which could never match any group should raise
    # an exception.  A selector which matches a repetition that didn't match
    # currently incorrectly raises an exception
    if not a:
      raise e

    return poiu(*filter(lambda itm: itm.match.group(itm.group), a))

  __getattr__ = untwisted.partial(mnbv, AttributeError)
  __getitem__ = untwisted.partial(mnbv, KeyError)

  def __int__(ctx):
    try:
      return int(ctx.args[0].match.group(ctx.args[0].group))

    except IndexError:
      raise ValueError

  __len__ = lambda ctx: ctx.args[0].match.end(ctx.args[0].group) - ctx.args[0].match.start(ctx.args[0].group)
  __nonzero__ = lambda ctx: bool(ctx.args)

  def __str__(ctx):
    try:
      return ctx.args[0].match.group(ctx.args[0].group)

    except IndexError:
      return ''

  join = lambda ctx, separator: separator.join(map(str, ctx))

class qwer:
  def __init__(ctx, *args):
    ctx.args = args

  def zxcv(ctx, group, pattern, subject, *args):
    start = 0
    a = []
    b = []
    for itm in ctx.args:
      try:
        group, pattern, start, c, d = itm.zxcv(group, pattern, subject, *args)

      except AttributeError:
        pattern += itm

      else:
        a.extend(c)
        b.extend(d)

    return group, pattern, start, a, b

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

    _, pattern, start, d, e = ctx.zxcv(0, '', subject, *a)

    match = jhgf(re.compile(pattern))(subject, start)
    if not match:
      raise ValueError

    if b:
      for itm in e:
        itm.match = getattr(itm, 'match', match)

      return poiu(*filter(lambda itm: itm.match.group(itm.group), e))

    f = iter(d)
    g = iter(d[1:])
    while True:
      try:
        f.next()[1].sibling = g.next()

      except StopIteration:
        break

    return poiu(asdf(0, *d, match=match))

  match = untwisted.partial(lkjh, lambda pattern: pattern.match)
  search = untwisted.partial(lkjh, lambda pattern: pattern.search)

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

    _, pattern, start, d, e = ctx.zxcv(0, '', subject, *a)

    if callable(replace):
      if b:
        def f(match):
          for itm in e:
            itm.match = getattr(itm, 'match', match)

          return replace(poiu(*filter(lambda itm: match.group(itm.group), e)))

      else:
        f = iter(d)
        g = iter(d[1:])
        while True:
          try:
            f.next()[1].sibling = g.next()

          except StopIteration:
            break

        f = lambda match: replace(poiu(asdf(0, *d, match=match)))

    else:
      f = replace

    try:
      return re.sub(pattern, f, subject, kwds['count'])

    except KeyError:
      return re.sub(pattern, f, subject)

class repetition(qwer):
  def __init__(ctx, *args, **kwds):
    ctx.args = args
    ctx.kwds = kwds

  def zxcv(ctx, group, pattern, subject, *args):
    count = 0

    group, a, start, b, c = qwer.zxcv(ctx, group, pattern, subject, *args)

    if b:
      if ctx.kwds.get('min'):
        match = re.match(pattern + a, subject)

        count += 1

      else:
        b = []
        c = []

        match = re.match(pattern, subject)

      if not match:
        raise ValueError

      start = match.end()

      while True:
        group, pattern, _, e, f = qwer.zxcv(ctx, 0, '', subject, *args)

        d = re.compile(pattern).match(subject, start)
        if not d:
          if ctx.kwds.get('min') > count:
            raise ValueError

          break

        start = d.end()

        # To capture all repetitions of groups we may need multiple matches, so
        # we need a time and space efficient representation of which match each
        # group is associated with.  We don't know whether multiple matches are
        # needed until after the group tree is built.  Currently we add
        # references to the match to the roots of the tree, and to any selected
        # groups.  select() propagates the match to subsequently selected
        # descendants - could it also incorrectly propagate the match to a
        # sibling associated with a different match?

        for itm in e:
          itm[1].match = d

        for itm in f:
          itm.match = getattr(itm, 'match', d)

        b.extend(e)
        c.extend(f)

        count += 1
        try:
          if ctx.kwds['max'] < count:
            break

        except KeyError:
          pass

      return 0, '', start, b, c

    pattern += '(?:' + a[len(pattern):]
    try:
      if ctx.kwds['min'] == ctx.kwds['max']:
        #pattern += '){{{}}}'.format(ctx.kwds['min'])
        pattern += '){{{0}}}'.format(ctx.kwds['min'])

      else:
        #pattern += '){{{},{}}}'.format(ctx.kwds['min'], ctx.kwds['max'])
        pattern += '){{{0},{1}}}'.format(ctx.kwds['min'], ctx.kwds['max'])

    except KeyError:
      try:
        if 1 == ctx.kwds['min']:
          pattern += ')+'

        else:
          #pattern += '){{{},}}'.format(ctx.kwds['min'])
          pattern += '){{{0},}}'.format(ctx.kwds['min'])

      except KeyError:
        try:
          #pattern += '){{,{}}}'.format(ctx.kwds['max'])
          pattern += '){{,{0}}}'.format(ctx.kwds['max'])

        except KeyError:
          pattern += ')*'

    return group, pattern, start, b, c

class rule(qwer):
  def __init__(ctx, name):
    ctx.namespace = sys._getframe().f_back.f_locals
    ctx.name = name.split('.')

  def zxcv(ctx, group, pattern, subject, *args):
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

    if b:
      pattern += '('

    group, pattern, start, f, g = qwer.zxcv(group, pattern, subject, *a)

    if b:
      h = iter(f)
      i = iter(f[1:])
      while True:
        try:
          h.next()[1].sibling = i.next()

        except StopIteration:
          break

      h = asdf(e, *f)

      if c:
        g.insert(0, h)

      return group, pattern + ')', start, [(ctx.name[-1], h)], g

    return group, pattern, start, f, g
