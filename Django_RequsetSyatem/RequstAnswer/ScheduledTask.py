import time
import datetime
from . import models


def CheckDate():
    now = datetime.date.today()
    list_ob = models.RequestTargetInfo.objects.filter(TargetStatus='未预约')
    for ob in list_ob:
        if (ob.TargetTrueDate-now).days<0:
            ob.TargetStatus = '已预约'
            ob.save()

def GetOneWeek():
    now = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    list_one = []
    for i in range(7):
        list_one.append(now+one_day*i)
    return list_one

def MakeDate():
    list_one = GetOneWeek()
    for date in list_one:
        list_tmp = models.RequestTargetInfo.objects.filter(TargetTrueDate=date)
        if len(list_tmp) == 0:
            sft = date.weekday()
            new_date = models.RequestTargetInfo()
            if sft == 0:
                list_tmp = ['8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00', '14:30-15:30', '15:30-16:30', '16:30-17:30']
                for i in list_tmp:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'lixuefei'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周一 '+i+' 李雪飞'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
            elif sft == 1:
                list_tmp = ['8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00', '14:30-15:30', '15:30-16:30', '16:30-17:30']
                for i in list_tmp:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'luojunjie'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周二 '+i+' 罗俊杰(遗传解读)'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
            elif sft == 2:
                list_tmp1 = ['9:00-10:00', '10:00-11:00', '11:00-12:00']
                list_tmp2 = ['14:30-15:30', '15:30-16:30', '16:30-17:30']
                for i in list_tmp1:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'wangdong'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周三 '+i+' 王栋'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
                for i in list_tmp2:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'huyongfei'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周三 '+i+' 胡永飞'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
            elif sft == 3:
                list_tmp1 = ['8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00']
                list_tmp2 = ['14:30-15:30', '15:30-16:30', '16:30-17:30']
                for i in list_tmp1:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'huyongfei'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周四 '+i+' 胡永飞'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
                for i in list_tmp2:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'zhoujiajian'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周四 '+i+' 周家健'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
            elif sft == 4:
                list_tmp = ['14:30-15:30', '15:30-16:30', '16:30-17:30']
                for i in list_tmp:
                    new_date = models.RequestTargetInfo()
                    new_date.TargetName = 'zhoujiajian'
                    new_date.TargetTrueDate = date
                    new_date.TargetData = date.strftime('%Y-%m-%d')+' 周五 '+i+' 周家健'
                    new_date.TargetStatus = '未预约'
                    new_date.save()
        else:
            pass
    CheckDate()



