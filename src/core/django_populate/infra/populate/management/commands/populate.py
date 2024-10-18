from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.django_populate.infra.populate.management.commands._systems import populate_systems
from core.django_populate.infra.populate.management.commands._quiz import populate_quizzes





class Command(BaseCommand):
    """
     Populates the database with the minimum information for the system to work.
    If the database is not empty, some data will not be populated.

    Raises:
        CommandError: If something goes wrong
    """

    help = """
        Populates the database with the minimum information for the system to work.
        If the database is not empty, some data will not be populated.
    """

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--systems",
            action="store_true",
            help="Insert systems in database"
        )
        parser.add_argument(
            "--quizzes",
            action="store_true",
            help="Insert quizzes in database"
        )

    def handle(self, *args, **options):
        try:
            if options.get("systems"):
                self.__handle_systems()
            if options.get("quizzes"):
                self.__handle_quizzes()

            self.stdout.write(
                self.style.SUCCESS(
                    "\n Data successfully populated :D"
                )
            )

        except CommandError as exc:
            raise CommandError("Check if the parameters are correct") from exc

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))  # pylint: disable=no-member

    
    
    def __handle_systems(self) -> None:
        self.stdout.write("Populating systems data in the database...", ending=" ")
        populate_systems()
        self.stdout.write(self.style.SUCCESS("OK"))
    
    def __handle_quizzes(self) -> None:
        self.stdout.write("Populating quizzes data in the database...", ending=" ")
        populate_quizzes()
        self.stdout.write(self.style.SUCCESS("OK"))