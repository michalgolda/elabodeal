from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer

from elabodeal.models import File


class FilesAPIView(APIView):
	def get(self, request, name):
		file = File.objects.filter(name=name).first()
		fs = FileSystemStorage()

		full_file_name = f'{name}.{file.extension}'

		if not file or not fs.exists(full_file_name):
			return Response(status=404)

		file_binary = fs.open(full_file_name)
		return Response(
			file_binary, 
			content_type=file.mime, 
			headers={
				'Content-Disposition': f'attachment; filename="{full_file_name}' 
			}
		)