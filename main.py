""" Main entry point """
from time import sleep
from incubus import IncubusFactory

def test_incubus():
    """ Test of the library """
    inc = IncubusFactory.get_instance()
    inc.start(1)
    print("Going to sleep a bit")
    sleep(120)
    print("Woke up!")

if __name__ == "__main__":
    test_incubus()
