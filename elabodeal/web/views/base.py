from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string


class BaseView(View):
	auth_required = False

	def dispatch(self, request, *args, **kwargs):
		if self.auth_required:
			if not request.user.is_authenticated:
				return redirect('web:index')
			
			return self.handle(request, *args, **kwargs)

		return self.handle(request, *args, **kwargs)

	def handle(self, request, *args, **kwargs):
		return super(BaseView, self).dispatch(request, *args, **kwargs)

	def respond(self, template, context, request):	
		return HttpResponse(render_to_string(template, context, request))
