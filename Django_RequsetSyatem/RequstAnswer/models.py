from django.db import models

# Create your models here.

class RequestInfo(models.Model):
    RequestNumber = models.AutoField(primary_key=True)
    RequestType = models.CharField(max_length=32,choices=(('RNAseq','RNAseq'), ('scRNAseq', 'scRNAseq'), ('ChIPseq', 'ChIPseq'), ('ATACseq', 'ATACseq'), ('MetaGenmics', 'MetaGenmics'), ('外显子测序', '外显子测序'), ('皮肤遗传解读', '皮肤遗传解读'), ('其他', '其他'),), default='RNAseq')
    RequestUser = models.CharField(max_length=10)
    RequestUserName = models.CharField(max_length=10)
    RequestEmail = models.CharField(max_length=256)
    RequestDate = models.DateTimeField(auto_now_add=True)
    RequestTarget = models.CharField(max_length=10)
    RequestContent = models.TextField(verbose_name='预约内容', blank=True)
    RequestTargetData = models.CharField(max_length=40)
    RequestTargetGroup = models.CharField(max_length=128)
    RequestStatus = models.CharField(max_length=32,choices=(('已提交, 待接受','已预约, 待接受'), ('已提交, 已接受', '已提交, 已接受'), ('已提交, 拒绝','已预约, 拒绝')), default='已提交, 待接受')

class RequestTargetInfo(models.Model):
    TargetName = models.CharField(max_length=10)
    TargetData = models.CharField(max_length=10)
    TargetTrueDate = models.DateField(auto_now_add=False)
    TargetStatus = models.CharField(max_length=32,choices=(('已预约','已预约'), ('未预约', '未预约'),), default='未预约')
