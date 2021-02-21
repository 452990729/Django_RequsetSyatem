from django.db import models

# Create your models here.

class RequestInfo(models.Model):
    RequestNumber = models.AutoField(primary_key=True)
    RequestType = models.CharField(max_length=32,choices=(('RNAseq','RNAseq'), ('WES', 'WES'), ('SingleCell', 'SingleCell'), ('MetaGenmics', 'MetaGenmics'), ('个性化分析', '个性化分析'), ('遗传咨询', '遗传咨询'), ('其他', '其他'),), default='已预约')
    RequestUser = models.CharField(max_length=10)
    RequestEmail = models.CharField(max_length=256)
    RequestDate = models.DateTimeField(auto_now_add=True)
    RequestTarget = models.CharField(max_length=10)
    RequestContent = models.TextField(verbose_name='预约内容', blank=True)
    RequestTargetData = models.CharField(max_length=40)
    RequestStatus = models.CharField(max_length=32,choices=(('已预约','已预约'), ('已确认', '已确认'),), default='已预约')

class RequestTargetInfo(models.Model):
    TargetName = models.CharField(max_length=10)
    TargetData = models.CharField(max_length=10)
    TargetTrueDate = models.DateField(auto_now_add=False)
    TargetStatus = models.CharField(max_length=32,choices=(('已预约','已预约'), ('未预约', '未预约'),), default='未预约')
