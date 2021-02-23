from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import CommentForm
from RequstAnswer.models import RequestInfo
from .models import Comment

from notifications.signals import notify
from Login.models import LoginUser


def post_comment(request, project, parent_comment_id=None):
    isactive = 'sub'
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    Project_model = RequestInfo.objects.get(RequestNumber=project)
    User = LoginUser.objects.get(username=request.session['user_name'])
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.Project = Project_model
            new_comment.user = User
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                if not parent_comment.user == User:
                    notify.send(
                        User,
                        recipient=parent_comment.user,
                        verb='回复了你',
                        target=Project_model,
                        action_object=new_comment,
                    )
#                return redirect('/RequstAnswer/sub/{}/'.format(project))
                return HttpResponse('提交成功！')
            new_comment.save()
            if not User == LoginUser.objects.get(username=Project_model.RequestUser):
                notify.send(
                        User,
                        recipient=LoginUser.objects.get(username=Project_model.RequestUser),
                        verb='回复了你',
                        target=Project_model,
                        action_object=new_comment,
                    )

            return redirect('/RequstAnswer/sub/{}/'.format(project))
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'project': project,
            'parent_comment_id': parent_comment_id
        }
        return render(request, 'comment/reply.html', context)
    else:
        return HttpResponse("仅接受GET/POST请求。")
