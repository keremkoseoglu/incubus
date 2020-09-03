""" Main entry point """
from incubus import IncubusFactory
from time import sleep


inc = IncubusFactory.get_instance()
inc.start(1)
print("Going to sleep a bit")
sleep(120)
