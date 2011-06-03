import sys

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

class qwer:
  def __init__(ctx, *args):
    ctx.args = args

  __getattr__ = lambda ctx, name: ''.join(itm[name] if isinstance(itm, rule) else itm for itm in ctx.args)
  __getitem__ = __getattr__
