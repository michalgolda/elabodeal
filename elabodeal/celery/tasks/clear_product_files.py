import json

from django.core.files.storage import DefaultStorage

from elabodeal.celery import app
from elabodeal.models import File


@app.task(name='clear_product_files')
def clear_product_files(file_list):
	file_list = json.loads(file_list)
	storage = DefaultStorage()

	for file in file_list:
		storage.delete(file['name'])
		File.objects.filter(id=file['id']).delete()