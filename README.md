# Ron Swanson Client

Python client to the [Ron Swanson](https://github.com/jamesseanwright/ron-swanson-quotes) API.

## Installation

In order to install the package run

```shell
pip install ron-swanson-client
```

## Quickstart

The package is as simple as it is. At first, create the instance of `RonSwanson` class

```python
from ron_swanson.api import RonSwanson

ron = RonSwanson()
```

Then run the method of the `ron` instance to make a call to the API.

There are three methods available. Please, see the full example below.

```python
import typing
from ron_swanson.api import RonSwanson

if __name__ == '__main__':
    ron = RonSwanson()

    # Get single quote of Ron Swanson
    one_quote: str = ron.one()

    # Get five quotes in a list
    five_quotes: typing.List[str] = ron.random(count=5)

    # Search for quotes
    results: typing.List[str] = ron.search(term="food")
```

## License

The project is licensed under [MIT license](LICENSE).
