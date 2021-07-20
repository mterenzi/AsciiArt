# AsciiArt

This takes static images and gifs and converts them into Ascii to be displayed in the terminal.

pip requirements:
Package           Version
----------------- -------
astroid           2.6.4
autopep8          1.5.7
colorama          0.4.4
isort             5.9.2
lazy-object-proxy 1.6.0
mccabe            0.6.1
numpy             1.21.1
Pillow            8.3.1
pip               20.2.3
pycodestyle       2.7.0
pylint            2.9.3
setuptools        49.2.1
toml              0.10.2
wrapt             1.12.1


Usage: ascii_art.py [-h] --image IMAGE [--dimensions [DIMENSIONS]] [--outfile OUTFILE] [--characters CHARACTERS] [--reverse [REVERSE]]

Converts images into Ascii art directly to the terminal. Works best with images resembling your terminals aspect ratio

optional arguments:
  -h, --help            show this help message and exit
  --image IMAGE         Path to an image file.
  --dimensions [DIMENSIONS]
                        Overrides terminal dimensions. Leave blank for image's dimensions. Ex. "1920,1080"
  --outfile OUTFILE     Path to an output file. Overwrites file location
  --characters CHARACTERS
                        Custom character set. Ordered from darkest to lightest Ex. "@,!,$"
  --reverse [REVERSE]   Reverse character set. Darkest values are now lightest and vice versa.
  
  
Some sample images with questionable redistribution legality
