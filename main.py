""" Main entry point """
from cgi import test
from incubus import IncubusFactory
from time import sleep

def test_incubus():
    inc = IncubusFactory.get_instance()
    inc.start(1)
    print("Going to sleep a bit")
    sleep(120)
    print("Woke up!")

if __name__ == "__main__":
    test_incubus()
