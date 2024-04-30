from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .forms import ChatmessagesForm
from .models import Chat,Item

@login_required
def new_chats(request,item_pk):
  item= get_object_or_404(Item,pk=item_pk)
  if item.created_by==request.user:
    return redirect('dashboard:index')
  chats=Chat.objects.filter(item=item).filter(members__in=[request.user.id])

  if chats:
    return redirect('chat:detail',pk=chats.first().id)
   


  if request.method=='POST':
    form=ChatmessagesForm(request.POST)
    if form.is_valid():
      chat=Chat.objects.create(item=item)
      chat.members.add(request.user)
      chat.members.add(item.created_by)
      chat.save()

      chat_message=form.save(commit=False)
      chat_message.chat=chat
      chat_message.created_by=request.user
      chat_message.save()

      return redirect('item:detail',pk=item_pk)
  else:
      form=ChatmessagesForm()
      return render(request,'chat/new.html',{
      'form':form,
    })
@login_required
def inbox(request):
  chats=Chat.objects.filter(members__in=[request.user.id])
  return render(request, 'chat/inbox.html',{
    'chats':chats
  })
@login_required
def detail(request,pk):
  chat=Chat.objects.filter(members__in=[request.user.id]).get(pk=pk)
  if request.method == 'POST':
    form = ChatmessagesForm(request.POST)
    if form.is_valid():
      chat_message=form.save(commit=False)
      chat_message.chat=chat
      chat_message.created_by=request.user
      chat_message.save()
      return redirect('chat:detail',pk=pk)
  else:
    form= ChatmessagesForm()
  return render(request,'chat/chat.html',{
    'chat':chat,
    'form':form,
  })