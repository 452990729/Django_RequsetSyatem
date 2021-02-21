from django import forms
from django.forms import ModelForm
from . import models


class NewRequest(ModelForm):
    class Meta:
        model = models.RequestInfo
        fields = ['RequestType', 'RequestContent', 'RequestTargetData', 'RequestEmail']
    RequestType = forms.ChoiceField(label='咨询类型', choices=(('RNAseq','RNAseq'), ('WES', 'WES'), ('SingleCell', 'SingleCell'), ('MetaGenmics', 'MetaGenmics'), ('个性化分析', '个性化分析'), ('遗传咨询', '遗传咨询'), ('其他', '其他'),), required=True)
    RequestTargetData = forms.ChoiceField(label='咨询时间', required=True)
    RequestEmail = forms.CharField(label='邮箱', max_length=20)

    def __init__(self, *args, **kwargs):
        super(NewRequest, self).__init__(*args, **kwargs)
        self.fields['RequestTargetData'].choices = models.RequestTargetInfo.objects.exclude(TargetStatus='已预约').values_list('TargetData', 'TargetData')
