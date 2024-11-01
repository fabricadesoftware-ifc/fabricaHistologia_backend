import requests
from core.uploader.models import Image
from core.django_populate.infra.datas.image import images
from django.core.files.base import ContentFile
import mimetypes

def download_images(imageUrl):
    
    response = requests.get(imageUrl)
    if response.status_code == 200:
        return response.content
    return None

def populate_images():
    
    for image_data in images:

        try:
            image_downloaded = download_images(image_data['url'])

            if image_downloaded:
                filename = image_data['file'].split('/')[-1] or 'downloaded_image.jpg'
                content_type = mimetypes.guess_type(filename)[0]
                print(content_type)

                image_file = ContentFile(image_downloaded, name=filename)
                image_file.content_type = content_type
    
                image = Image.objects.create(
                    description = image_data['description'],
                    file = image_file
                )

                image.save()
        except Exception as e:
            print(f'erro seu bosta', e)