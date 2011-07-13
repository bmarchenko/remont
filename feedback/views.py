from remont_dp.feedback.models import Feedback
from django.views.generic.list_detail import object_list

def feedback(request):
  feedbacks = Feedback.objects.filter(status = 'p')
  
  return render_to_response('feedback.html', {'feedbacks' : feedbacks})