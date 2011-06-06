import re, sys, untwisted

__all__ = 'rule', 'qwer'

class rule:
  def __init__(ctx, name):
    ctx.namespace = sys._getframe().f_back.f_locals
    ctx.name = name.split('.')

  def zxcv(ctx, name):
    result = ctx.namespace[ctx.name[0]]
    for itm in ctx.name[1:]:
      result = getattr(result, itm)

    if ctx.name[-1] == name[0]:
      if 1 < len(name):
        return result.zxcv(name[1:])

      a, b = result.zxcv(name)
      b.insert(0, result)

      return '(' + a + ')', b

    return result.zxcv(name)

  def __str__(ctx):
    result = ctx.namespace[ctx.name[0]]
    for itm in ctx.name[1:]:
      result = getattr(result, itm)

    return str(result)

# Unbound
class qwer:

  # For .__hash__()
  __metaclass__ = type

  def __init__(ctx, *args):
    ctx.args = args

  def zxcv(ctx, name):
    a = ''
    b = []
    for itm in ctx.args:
      if isinstance(itm, rule):
        c, d = itm.zxcv(name)

        a += c
        b += d

      else:
        a += itm

    return a, b

  # Bound
  class __call__:
    class __metaclass__(type):
      __get__ = untwisted.ctxual

    def __init__(ctx, poiu):
      ctx.poiu = poiu

    class __getattr__:
      class __metaclass__(type):
        __call__ = lambda ctx, name: type.__call__(ctx, re.split('\s+', name))
        __get__ = untwisted.ctxual

      def __init__(ctx, name):
        ctx.name = name

      def __getattr__(ctx, name):
        lkjh = list(ctx.name)
        lkjh.append(name)

        return type.__call__(ctx.ctx.__getattr__, lkjh)

      __getitem__ = __getattr__

      def __int__(ctx):
        a, b = ctx.ctx.ctx.zxcv(ctx.name)
        if not b:
          raise AttributeError

        result = re.match(a, ctx.ctx.poiu)
        if not result:
          raise ValueError

        return int(filter(None, result.groups())[0])

      def __iter__(ctx):
        a, b = ctx.ctx.ctx.zxcv(ctx.name)
        if not b:
          raise AttributeError

        result = re.match(a, ctx.ctx.poiu)
        if not result:
          raise ValueError

        return (b[i](result.groups()[i]) for i in range(len(b)) if result.groups()[i])

      def __str__(ctx):
        a, b = ctx.ctx.ctx.zxcv(ctx.name)
        if not b:
          raise AttributeError

        result = re.match(a, ctx.ctx.poiu)
        if not result:
          raise ValueError

        return ''.join(filter(None, result.groups()))

    __getitem__ = __getattr__

    __int__ = lambda ctx: int(ctx.poiu)

    def __len__(ctx):
      result = re.match(str(ctx.ctx), ctx.poiu)
      if not result:
        raise ValueError

      return result.end()

    __str__ = lambda ctx: ctx.poiu

  __str__ = lambda ctx: ''.join(map(str, ctx.args))
