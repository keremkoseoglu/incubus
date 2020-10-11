# Incubus

This is a simple idle app killer.

If you want to quit your app after a certain period of inactivity, you may use this library.

## Installation

To install from GitHub:

```
pip install git+https://github.com/keremkoseoglu/incubus.git
```

## Usage

In the example below, your Python app will close after 60 seconds of inactivity.

```
from incubus import IncubusFactory
inc = IncubusFactory.get_instance()
inc.start(60)
```

To let Incubus know that the user has performed some activity and reset the timer:

```
inc.user_event()
```
