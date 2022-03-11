from django.shortcuts import render, get_object_or_404
from django.views import View 

from .models import Course
# Base view class = view 
class CourseView(View):
	template_name = "courses/course_detail.html"
	def get(self, request, id=None, *args, **kwargs):
		context={}
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			context['object'] = obj
		return render(request, self.template_name, context)


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
	print(request.method)
	return render(request, 'about.html', {})


