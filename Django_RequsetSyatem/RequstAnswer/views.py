import os
import time
import json
from django.shortcuts import render,redirect,HttpResponse
from . import models
from .forms import NewRequest
from Login.models import LoginUser
from Comment.models import Comment
from Comment.forms import CommentForm
from django.utils import timezone
from notifications.signals import notify

# Create your views here.

def GetCTL(request):
    user = request.session['user_name']
    if LoginUser.objects.get(username=user).info_right == 'admin':
        CTL = 'admin'
    else:
        CTL = 'normal'
    return CTL

def CreateNew(request):
    isactive = 'new'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    user = request.session['user_name']
    CTL = GetCTL(request)
    if request.method == "POST":
        NewRequestForm = NewRequest(request.POST)
        message = "请检查输入！"
        if NewRequestForm.is_valid():
            RequestType = NewRequestForm.cleaned_data['RequestType']
            RequestContent = NewRequestForm.cleaned_data['RequestContent']
            RequestTargetData = NewRequestForm.cleaned_data['RequestTargetData']
            RequestEmail = NewRequestForm.cleaned_data['RequestEmail']
            RequestUserName = NewRequestForm.cleaned_data['RequestUserName']
            RequestTargetGroup = NewRequestForm.cleaned_data['RequestTargetGroup']
            new_requset = models.RequestInfo()
            new_requset.RequestUser = user
            new_requset.RequestEmail = RequestEmail
            new_requset.RequestContent = RequestContent
            new_requset.RequestTargetData = RequestTargetData
            new_requset.RequestTarget = models.RequestTargetInfo.objects.get(TargetData=RequestTargetData).TargetName
            new_requset.RequestType = RequestType
            new_requset.RequestUserName = RequestUserName
            new_requset.RequestTargetGroup = RequestTargetGroup
            new_requset.RequestStatus = '已提交, 待接受'
            new_requset.save()
            notify.send(
                LoginUser.objects.get(username=user),
                recipient=LoginUser.objects.get(username=models.RequestTargetInfo.objects.get(TargetData=RequestTargetData).TargetName),
                verb='提交了预约',
                target=new_requset
            )
            RequestTargetInfoModel = models.RequestTargetInfo.objects.get(TargetData=RequestTargetData)
            RequestTargetInfoModel.TargetStatus = '已预约'
            RequestTargetInfoModel.save()
            return redirect('/RequstAnswer/index/')
        return render(request, 'RequstAnswer/new.html', locals())
    NewRequestForm = NewRequest()
    return render(request, 'RequstAnswer/new.html', locals())

def Index(request):
    isactive = 'Requestinfor'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    data_list = []
    user = request.session['user_name']
    CTL = GetCTL(request)
    list_ob = models.RequestInfo.objects.order_by('RequestTargetData').filter(RequestUser=user)
    for data_info in list_ob:
        data_list.append({
            '预约编号':data_info.RequestNumber,
            '项目类型':data_info.RequestType,
            '预约时间':data_info.RequestTargetData,
            '发起预约时间':data_info.RequestDate.strftime('%Y-%m-%d %H:%M'),
            '预约人员':data_info.RequestUserName,
            '预约状态':data_info.RequestStatus,
        })
    data_dic = {}
    data_dic['userrequest'] = data_list
    data_dic['CTL'] = CTL
    return render(request, 'RequstAnswer/index.html', data_dic,)

def Detail(request, project):
    isactive = 'Requestinfor'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    CTL = GetCTL(request)
    Project_model = models.RequestInfo.objects.get(RequestNumber=project)
    RequestNumber = Project_model.RequestNumber
    RequestType = Project_model.RequestType
#    RequestUser = Project_model.RequestUser
    RequestContent = Project_model.RequestContent
    RequestDate = Project_model.RequestDate.strftime('%Y-%m-%d %H:%M')
    RequestTargetData = Project_model.RequestTargetData
    RequestStatus = Project_model.RequestStatus
    return render(request, 'RequstAnswer/detail.html', locals())

def Del(request, project):
    isactive = 'Requestinfor'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    Project_model = models.RequestInfo.objects.get(RequestNumber=project)
    user = Project_model.RequestUser
    notify.send(
        LoginUser.objects.get(username=user),
        recipient=LoginUser.objects.get(username=models.RequestTargetInfo.objects.get(TargetData=Project_model.RequestTargetData).TargetName),
        verb='删除了预约',
        target=Project_model,
    )
    RequestTargetData = Project_model.RequestTargetData
    RequestTargetInfoModel = models.RequestTargetInfo.objects.get(TargetData=RequestTargetData)
    RequestTargetInfoModel.TargetStatus = '未预约'
    RequestTargetInfoModel.save()
    Project_model.delete()
    return Index(request)

def SubIndex(request):
    isactive = 'sub'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    user = request.session['user_name']
    CTL = GetCTL(request)
    list_project_model = models.RequestInfo.objects.order_by('RequestStatus').filter(RequestTarget=user)
    data_list = []
    for data_info in list_project_model:
        data_list.append({
            '预约编号':data_info.RequestNumber,
            '项目类型':data_info.RequestType,
            '预约时间':data_info.RequestTargetData,
            '预约人员':data_info.RequestUserName,
            '课题组':data_info.RequestTargetGroup,
            '预约状态':data_info.RequestStatus,
        })
    data_dic = {}
    data_dic['userrequest'] = data_list
    data_dic['CTL'] = CTL
    return render(request, 'RequstAnswer/subindex.html', data_dic)

def SubDetail(request, project):
    isactive = 'sub'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    CTL = GetCTL(request)
    Project_model = models.RequestInfo.objects.get(RequestNumber=project)
    RequestNumber = Project_model.RequestNumber
    RequestType = Project_model.RequestType
    RequestUser = Project_model.RequestUser
    RequestTargetGroup = Project_model.RequestTargetGroup
    RequestUserName = Project_model.RequestUserName
    RequestEmail = Project_model.RequestEmail
    RequestContent = Project_model.RequestContent
    RequestTargetData = Project_model.RequestTargetData
    RequestStatus = Project_model.RequestStatus
    RequestDate = Project_model.RequestDate.strftime('%Y-%m-%d %H:%M')
    comments = Comment.objects.filter(Project=project)
    comment_form = CommentForm()
    return render(request, 'RequstAnswer/subdetail.html', locals())

def CheckProject(request, project):
    isactive = 'sub'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    Project_model = models.RequestInfo.objects.get(RequestNumber=project)
    user = request.session['user_name']
    notify.send(
        LoginUser.objects.get(username=user),
        recipient=LoginUser.objects.get(username=Project_model.RequestUser),
        verb='确认了预约',
        target=Project_model,
    )
    Project_model.RequestStatus = '已提交, 已接受'
    Project_model.save()
    return SubIndex(request)

def RejectProject(request, project):
    isactive = 'sub'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    Project_model = models.RequestInfo.objects.get(RequestNumber=project)
    user = request.session['user_name']
    notify.send(
        LoginUser.objects.get(username=user),
        recipient=LoginUser.objects.get(username=Project_model.RequestUser),
        verb='拒绝了预约',
        target=Project_model,
    )
    Project_model.RequestStatus = '已提交, 拒绝'
    Project_model.save()
    RequestTargetData = Project_model.RequestTargetData
    RequestTargetInfoModel = models.RequestTargetInfo.objects.get(TargetData=RequestTargetData)
    RequestTargetInfoModel.TargetStatus = '未预约'
    RequestTargetInfoModel.save()
    return SubIndex(request)

def Upload(request):
    file_obj = request.FILES.get('UploadFile')
    file_type = request.GET.get('dir')
    file_obj.name = '{}{}'.format(time.time(), file_obj.name)
    file_dir = 'media{}{}'.format(os.sep, file_type)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = os.path.join("media", file_type, file_obj.name)
    with open(file_path, 'wb') as f:
        for line in file_obj:
            f.write(line)
    dic = {'error': 0, 'url': '/media/{}/{}'.format(file_type, file_obj.name), 'message': '出现内部错误'}
    return HttpResponse(json.dumps(dic))
