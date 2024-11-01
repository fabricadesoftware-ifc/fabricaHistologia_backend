from core.uploader.models import Document
from core.django_populate.domain import supporting_materials
from django.core.files.base import ContentFile
import os

def populate_documents():
    
    path = supporting_materials.__path__[0]
    
    for file in os.listdir(path):
        filename = os.path.join(path, file)

        try:

            if filename:
                with open(filename, 'rb') as f:
                    content = f.read()

                    content_file = ContentFile(content)

                    content_file.name = filename

                    document = Document.objects.create(
                        description = f'material de apoio sobre ALGO',
                        file = content_file,
                    )

                    document.save()

        except Exception as e:
            print(f'erro seu bosta', e)