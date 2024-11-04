from core.uploader.models import Image
from core.django_populate.domain import images
from django.core.files.base import ContentFile
import os
import mimetypes

def populate_images():
    
    path = images.__path__[0]
    
    for i in range(0, len(os.listdir(path))):
        file = os.listdir(path)[i]
        print(file)
        filename = os.path.join(path, file)

        try:

            if filename:
                with open(filename, 'rb') as f:
                    content = f.read()

                    content_type = mimetypes.guess_type(filename)[0]

                    content_file = ContentFile(content, name=filename)
                    content_file.content_type = content_type

                    document = Image.objects.create(
                        description = file.replace('.png', ''),
                        file = content_file,
                    )

                    document.save()
        except Exception as e:
            print(f'erro seu bosta', e)