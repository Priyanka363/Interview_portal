from .models import interview,interviewee

def add_interview(intrv,st,et):
  inv = interview.objects.create(st_time=st, end_time=et)

  for id in intrv:
    intrv_details=interviewee.objects.get(interviewee_id=id)
    inv.interviewees.add(intrv_details)

  inv.save()

def edit_interview(intrv,st,et,e_id):
  inv = interview.objects.get(id=e_id)
  inv.st_time=st
  inv.end_time=et
  inv.interviewees.clear()

  for id in intrv:
      intrv_details=interviewee.objects.get(interviewee_id=id)
      inv.interviewees.add(intrv_details)

  inv.save()