# Generated by Django 2.2 on 2021-02-23 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestInfo',
            fields=[
                ('RequestNumber', models.AutoField(primary_key=True, serialize=False)),
                ('RequestType', models.CharField(choices=[('RNAseq', 'RNAseq'), ('scRNAseq', 'scRNAseq'), ('ChIPseq', 'ChIPseq'), ('ATACseq', 'ATACseq'), ('MetaGenmics', 'MetaGenmics'), ('外显子测序', '外显子测序'), ('皮肤遗传解读', '皮肤遗传解读'), ('其他', '其他')], default='RNAseq', max_length=32)),
                ('RequestUser', models.CharField(max_length=10)),
                ('RequestUserName', models.CharField(max_length=10)),
                ('RequestEmail', models.CharField(max_length=256)),
                ('RequestDate', models.DateTimeField(auto_now_add=True)),
                ('RequestTarget', models.CharField(max_length=10)),
                ('RequestContent', models.TextField(blank=True, verbose_name='预约内容')),
                ('RequestTargetData', models.CharField(max_length=40)),
                ('RequestTargetGroup', models.CharField(max_length=128)),
                ('RequestStatus', models.CharField(choices=[('已提交, 待接受', '已预约, 待接受'), ('已提交, 已接受', '已提交, 已接受'), ('已提交, 拒绝', '已预约, 拒绝')], default='已提交, 待接受', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='RequestTargetInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TargetName', models.CharField(max_length=10)),
                ('TargetData', models.CharField(max_length=10)),
                ('TargetTrueDate', models.DateField()),
                ('TargetStatus', models.CharField(choices=[('已预约', '已预约'), ('未预约', '未预约')], default='未预约', max_length=32)),
            ],
        ),
    ]
