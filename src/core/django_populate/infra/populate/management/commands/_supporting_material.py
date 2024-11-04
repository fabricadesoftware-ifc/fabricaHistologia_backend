from core.uploader.models import Image
from core.veterinary.models import System
from core.supporting_materials.models import SupportingMaterial
from core.django_populate.infra.datas.supporting_materials import materials
from core.django_populate.domain import supporting_materials
from django.core.files.base import ContentFile
import os
import mimetypes

def populate_documents():
    
    path = supporting_materials.__path__[0]
    
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
                        description = file.replace(".jpg", ""),
                        file = content_file,
                    )

                    document.save()
        except Exception as e:
            print(f'erro seu bosta', e)


def populate_supporting_materials():
    if SupportingMaterial.objects.exists():
        return
    

    for material_data in materials:
        try:
            document = Image.objects.get(description=material_data["document"])
            system = System.objects.get(id=material_data["system_id"])
            print(document)
            supporting_material = SupportingMaterial.objects.create(
                name=material_data["name"],
                description=material_data["description"],
                document_supporting_material=document,
                field_name=material_data["field_name"],
                system=system,
            )
            
            supporting_material.save()

        except Exception as e:
            print(f"Erro ao popular materiais de apoio '{material_data['name']}': {e}")

    print("População de materiais de apoio concluídas.")