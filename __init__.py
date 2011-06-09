import re, sys, untwisted

__all__ = 'rule', 'qwer'

class asdf:
  def __init__(ctx, name, *args):
    ctx.name = name
    ctx.args = args

  def select(ctx, name, group):
    result = []
    group += 1

    if ctx.name == name[0]:
      if 1 < len(name):
        name = name[1:]

      else:
        result = [(ctx, group)]

    for itm in ctx.args:
      a, group = itm.select(name, group)
      result.extend(a)

    return result, group

class poiu:
  __metaclass__ = type

  def __init__(ctx, match, group, *args):
    ctx.match = match
    ctx.group = group
    ctx.args = args

  class zxcv:
    class __metaclass__(type):
      __call__ = lambda ctx, e, name: type.__call__(ctx, e, re.split('\s+', name))
      __get__ = untwisted.ctxual

    def __init__(ctx, e, name):
      ctx.name = name

      ctx.iuyta = []

      group = ctx.ctx.group
      for itm in ctx.ctx.args:
        a, group = itm.select(name, group)
        ctx.iuyta.extend(a)

      if not ctx.iuyta:
        raise e

    def mnbv(ctx, e, name):
      if isinstance(name, int):
        try:
          return ctx.iuytb[name]

        except AttributeError:
          ctx.iuytb = [poiu(ctx.ctx.match, group, *itm.args) for itm, group in ctx.iuyta if ctx.ctx.match.group(group)]

          return ctx.iuytb[name]

      return type.__call__(ctx.ctx.zxcv, e, ctx.name + re.split('\s+', name))

    __getattr__ = untwisted.partial(mnbv, AttributeError)
    __getitem__ = untwisted.partial(mnbv, KeyError)

    __int__ = lambda ctx: int(ctx[0])
    __str__ = lambda ctx: str(ctx[0])

  __getattr__ = untwisted.partial(zxcv, AttributeError)
  __getitem__ = untwisted.partial(zxcv, KeyError)

  __int__ = lambda ctx: int(ctx.match.group(ctx.group))
  __len__ = lambda ctx: ctx.match.end(ctx.group) - ctx.match.start(ctx.group)
  __str__ = lambda ctx: ctx.match.group(ctx.group)

class rule:
  def __init__(ctx, name):
    ctx.namespace = sys._getframe().f_back.f_locals
    ctx.name = name.split('.')

  def compile(ctx):
    uytr = ctx.namespace[ctx.name[0]]
    for itm in ctx.name[1:]:
      uytr = getattr(uytr, itm)

    pattern, b = uytr.compile()

    return '(' + pattern + ')', (asdf(ctx.name[-1], *b),)

  def __str__(ctx):
    result = ctx.namespace[ctx.name[0]]
    for itm in ctx.name[1:]:
      result = getattr(result, itm)

    return str(result)

class qwer:
  def __init__(ctx, *args):
    ctx.args = args

  def compile(ctx):
    pattern = []
    b = []
    for itm in ctx.args:
      if isinstance(itm, rule):
        itm, c = itm.compile()

        b.extend(c)

      pattern.append(itm)

    return ''.join(pattern), b

  def lkjh(ctx, jhgf, subject):
    pattern, b = ctx.compile()

    match = jhgf(pattern, subject)
    if not match:
      raise ValueError

    return poiu(match, 0, *b)

  match = untwisted.partial(lkjh, re.match)
  search = untwisted.partial(lkjh, re.search)

  __str__ = lambda ctx: ''.join(map(str, ctx.args))
