from django.shortcuts import render, redirect
from django.db.models import Q
from .models import interviewee,interview
from .add_change import add_interview, edit_interview
from datetime import datetime

# Create your views here.
def add(request):
  context={}

  if(request.method == 'POST'):
    intrv=request.POST.getlist('interviewees')
    st=request.POST.get('st')
    et=request.POST.get('et')
    if(st>=et):
      error='Enter correct schedule'
      context['error']=error

    elif(len(intrv)<2):
      error='Schedule interview for more than 1 candidate'
      context['error']=error

    else:
      overlap_candidates=[]

      for id in intrv:
        overlap=interview.objects.filter(Q(interviewees__interviewee_id=id, st_time__gte=st , st_time__lte=et) | Q(interviewees__interviewee_id=id, end_time__gte=st, end_time__lte=et))
        if(len(overlap)>0):
          _interviewee = interviewee.objects.get(interviewee_id=id)
          overlap_candidates.append(_interviewee.f_name+" "+_interviewee.l_name)
      
      if(len(overlap_candidates)>0):
        context['error'] = "No slots free for " + ",".join(overlap_candidates)

      else:
        add_interview(intrv,st,et)
    
  in_details=interviewee.objects.all()
  context['list']=in_details
  return render(request,'add.html',context)
  
def listt(request):
  in_details=interview.objects.filter(st_time__gte=datetime.now()).order_by('st_time')
  # interview.objects.filter
  context={'in_details':in_details} 
  return render(request,'listt.html',context)

def update(request,e_id):
  context={}

  if(request.method == 'POST'):
    intrv=request.POST.getlist('interviewees')
    st=request.POST.get('st')
    et=request.POST.get('et')
    if(st>=et):
      error='Enter correct schedule'
      context['error']=error

    elif(len(intrv)<2):
      error='Schedule interview for more than 1 candidate'
      context['error']=error

    else:
      overlap_candidates=[]

      for id in intrv:
        overlap=interview.objects.filter(Q(interviewees__interviewee_id=id, st_time__gte=st , st_time__lte=et) | Q(interviewees__interviewee_id=id, end_time__gte=st, end_time__lte=et)).exclude(id=e_id)
        if(len(overlap)>0):
          _interviewee = interviewee.objects.get(interviewee_id=id)
          overlap_candidates.append(_interviewee.f_name+" "+_interviewee.l_name)
      
      if(len(overlap_candidates)>0):
        context['error'] = "No slots free for " + ",".join(overlap_candidates)

      else:
        edit_interview(intrv,st,et,e_id)
        return redirect('/listt')

  interview_detail=interview.objects.get(id=e_id)
  in_details=interviewee.objects.all()
  context.update({'interview_detail':interview_detail,'in_details':in_details, 'e_id':e_id})
  return render(request,'update.html',context)