#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
prefixes   = ['fare','south','north','aber','ast','auch','auchter','bal','bally','ball','brad','bre','caer','car','cul','cum','cwm','din','dinas','dol','drum','dow','don','dum','duff','doune','fare','fin','kil','kin','kyle','lan','lhan','llan','lang','lin','nan','nans','mynydd','pen','pit','pol','pont','porth','shep','ship','stan','strath','tre','tilly','tullie','tulloch','win']
suffixes   = ['ay','ey','bost','bury','borough','brough','burgh','carden','caster','chester','cester','ceter','cot','cott','dale','dean','don','den','field','firth','frith','ham','ing','keth','cheth','lea','ley','leigh','mouth','ness','pool','shaw','stead','ster','thwaite','twatt','toft','tun','ton','wick','wich','wych','wyke','worth','worthy','wardine']
pre        = choice(prefixes)
suf        = choice(suffixes)
townName   = pre + suf
print(townName)
