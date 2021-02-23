from django import forms
from django.forms import ModelForm
from . import models


class NewRequest(ModelForm):
    class Meta:
        model = models.RequestInfo
        fields = ['RequestType', 'RequestTargetGroup', 'RequestContent', 'RequestTargetData', 'RequestUserName', 'RequestEmail']
    RequestType = forms.ChoiceField(label='咨询类型', choices=(('RNAseq','RNAseq'), ('scRNAseq', 'scRNAseq'), ('ChIPseq', 'ChIPseq'), ('ATACseq', 'ATACseq'), ('MetaGenmics', 'MetaGenmics'), ('外显子测序', '外显子测序'), ('皮肤遗传解读', '皮肤遗传解读'), ('其他', '其他'),), required=True)
    RequestTargetGroup = forms.CharField(label='课题组', max_length=20)
    RequestTargetData = forms.ChoiceField(label='咨询时间', required=True)
    RequestUserName = forms.CharField(label='预约人员', max_length=10)
    RequestEmail = forms.CharField(label='邮箱', max_length=20)

    def __init__(self, *args, **kwargs):
        super(NewRequest, self).__init__(*args, **kwargs)
        self.fields['RequestTargetData'].choices = models.RequestTargetInfo.objects.exclude(TargetStatus='已预约').values_list('TargetData', 'TargetData')

