import time
import datetime
from . import models


def CheckDate():
    now = datetime.date.today()
    for ob in models.RequestTargetInfo.objects.filter(TargetStatus='未预约'):
        print((ob.TargetTrueDate-now).days)
        print('fsfd')
        if (ob.TargetTrueDate-now).days<0:
#            ob.TargetStatus = '已预约'
#            ob.save()
            pass
CheckDate()
