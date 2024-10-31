from core.veterinary.models import System

from core.django_populate.infra.datas.system import systems

def populate_systems():
    if System.objects.exists():
        return
    

    for systems_data in systems:
        try:
            # cria os sistemas
            system = System.objects.create(
                name=systems_data["name"],
                description=systems_data["description"],
            )

            system.save()

        except Exception as e:
            print(f"Erro ao popular sistemas '{systems_data['name']}': {e}")

    print("População de sistemas concluídas.")