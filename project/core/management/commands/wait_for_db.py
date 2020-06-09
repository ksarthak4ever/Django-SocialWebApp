import time

from django.db import connections #to test if db connection is available
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""
	Django command to pause execution till database is available.
	"""

	def handle(self, *args, **options):
		self.stdout.write('Waiting for database...')
		db_conn = None
		# while there is no value in db_conn
		# try to set to db connections and if the connection
		# is not available then django raises operational error and we raise an output and app sleeps for 1 second.This repeats till the db connection is available.
		while not db_conn:
			try:
				db_conn = connections['default']
			except OperationalError:
				self.stdout.write('Database unavailable,Waiting 1 second')
				time.sleep(1)

		self.stdout.write(self.style.SUCCESS('Database available!'))