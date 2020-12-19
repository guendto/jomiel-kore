# jomiel-kore

![code-style]

[code-style]: https://img.shields.io/badge/code%20style-black-000000.svg

The minimalistic foundation for creating new [Python] applications.

## License

`jomiel-kore` is licensed under the [Apache License version 2.0][aplv2].

## Requirements

`jomiel-kore` is written for [Python] 3.6 and later.

## Installation

```shell
pip install jomiel-kore
```

## Building packages from repo

```shell
git clone https://github.com/guendto/jomiel-kore
cd jomiel-kore
git tag -s KEYID -am 'jomiel-kore version VERSION (INITIALS)' TAGNAME
pip install pep517
python -m pep517.build [-s|-b] .
```

The packages are created under the dist/ dir.

## Acknowledgements

`jomiel-kore` uses [pre-commit] and its many hooks to lint and format
the project files. See the .pre-commit-config.yaml file for details.

[python]: https://www.python.org/about/gettingstarted/
[aplv2]: https://www.tldrlegal.com/l/apache2
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org
