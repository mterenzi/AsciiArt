import os
import sys
import argparse
import numpy as np
from PIL import Image, ImageOps, ImageSequence


def parse_args():
	description = 'Converts images into Ascii art directly to the terminal. \
		Works best with images resembling your terminals aspect ratio'
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('--image', type=str, default=None, required=True,
						help='Path to an image file.')
	parser.add_argument('--dimensions', type=str, nargs='?', default='term', const='img',
						help="Overrides terminal dimensions.\
							Leave blank for image's dimensions.\
							Ex. \"1920,1080\"")
	parser.add_argument('--outfile', type=str, default=None, required=False,
						help='Path to an output file. Overwrites file location')
	parser.add_argument('--characters', type=str, default=None, required=False,
						help='Custom character set. Ordered from darkest to lightest\
							Ex. "@!$"')
	parser.add_argument('--reverse', type=bool, default=False, required=False,
						nargs='?', const='True',
						help='Reverse character set. Darkest values are now lightest\
							and vice versa.')

	args = vars(parser.parse_args())
	return args



def convert_image(img, dimensions):
	if dimensions != 'img':
		if dimensions == 'term':
			terminal_dimensions = os.get_terminal_size()
			dimensions = (terminal_dimensions.columns, terminal_dimensions.lines)
		else:
			dimensions = dimensions.split(',')
			dimensions = [int(dimensions[0]), int(dimensions[1])]
		
		img = img.resize(dimensions)
	else:
		dimensions = img.size

	gray_img = ImageOps.grayscale(img)
	return gray_img, dimensions


def get_character(char):
	global characters

	char_index = int((char / 255) * (len(characters) - 1))
	return characters[char_index]


def convert_ascii(img):
	img_array = np.array(img)

	terminal = []
	for y in img_array:
		terminal_row = []
		for x in y:
			terminal_row.append(get_character(x))
		terminal.append(terminal_row)
	return terminal


def print_terminal(terminal, outfile):
	if outfile:
		file = open(outfile, 'w+')
	else:
		file = sys.stdout

	for y in terminal:
		for x in y:
			print(x, end='', file=file)
		print(file=file)

	if outfile:
		file.close()


def single_image(args, img):
	img, dimensions = convert_image(img, args['dimensions'])
	terminal = convert_ascii(img)
	print_terminal(terminal, args['outfile'])
	
	return dimensions


def multi_image(args, img):
	for img in ImageSequence.Iterator(img):
		img, dimensions = convert_image(img, args['dimensions'])
		terminal = convert_ascii(img)
		
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

		print_terminal(terminal, args['outfile'])

	return dimensions



if __name__ == '__main__':
	args = parse_args()
	if not args['characters']:
		characters = list(".'`^,:;!><~+_-?][}{)(|\\/*#&%@$")
	else:
		characters = list(args['characters'])

	if args['reverse']:
		characters.reverse()

	with Image.open(args['image']) as img:
		try:
			if img.is_animated:
				multi_image(args, img)
			else:
				dimensions = single_image(args, img)
		except AttributeError:
			dimensions = single_image(args, img)
	
	print('Output Dimensions: ', dimensions)
