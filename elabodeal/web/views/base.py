from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string


class BaseView(View):
	auth_required = False
	publisher_required = False

	def dispatch(self, request, *args, **kwargs):
		if self.auth_required:
			if not request.user.is_authenticated:
				return redirect('web:login')
				
		if self.publisher_required:
			if not request.user.publisher:
				return redirect('web:salesmanager-start')

		return self.handle(request, *args, **kwargs)

	def handle(self, request, *args, **kwargs):
		return super(BaseView, self).dispatch(request, *args, **kwargs)

	def respond(self, template, request, context = None):	
		return HttpResponse(render_to_string(template, context, request))


class BaseAjaxView(BaseView):
	def dispatch(self, request, *args, **kwargs):
		if self.auth_required:
			if not request.user.is_authenticated:
				return self.respond(message='Unauthorized', 
									status=401)

			if self.publisher_required:
				if not request.user.publisher:
					return self.respond(message='Forbidden',
										status=403)

		return self.handle(request, *args, **kwargs)

	def respond(self, message = None, data = None, status = 200):
		response = JsonResponse({'msg': message, 
								'data': data, 
							 	'status': status})
		response.status_code = status

		return response
