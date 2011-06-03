import re, sys, untwisted

__all__ = 'rule', 'qwer'

class rule:
  def __init__(ctx, name):
    ctx.namespace = sys._getframe().f_back.f_locals
    ctx.name = name.split('.')

  def __getattr__(ctx, name):
    result = ctx.namespace[ctx.name[0]]
    for itm in ctx.name[1:]:
      result = getattr(result, itm)

    if ctx.name[-1] == name:
      return '(' + result[name] + ')'

    return result[name]

  __getitem__ = __getattr__

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

  __getattr__ = lambda ctx, name: ''.join(itm[name] if isinstance(itm, rule) else itm for itm in ctx.args)
  __getitem__ = __getattr__

  # Bound
  class __call__:
    class __metaclass__(type):
      __get__ = untwisted.ctxual

    def __init__(ctx, poiu):
      ctx.poiu = poiu

    class __getattr__:
      class __metaclass__(type):
        __get__ = untwisted.ctxual

      def __init__(ctx, name):
        ctx.name = name

      __str__ = lambda ctx: ''.join(re.match(ctx.ctx.ctx[ctx.name], ctx.ctx.poiu).groups())

    __getitem__ = __getattr__

  __str__ = lambda ctx: ''.join(map(str, ctx.args))
