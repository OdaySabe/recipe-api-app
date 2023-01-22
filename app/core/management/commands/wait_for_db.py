from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as PSOperationalError
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        self.stdout.write("Waiting for Database")
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except(OperationalError,PSOperationalError):
                self.stdout.write("DB not avaliable yet.  Waiting 1 second ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB is avaliable"))

