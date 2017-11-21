
import os
from . import ASCIIArt

def save(art, name):
    with open(name+'.txt', 'w') as f:
        f.write(''.join(art))

def main(args):
    if args.image:
        name = os.path.splitext(os.path.basename(args.image))[0]
        art = ASCIIArt(args.image, args.scale)
        save(art.draw_ascii(curve=args.curve), name)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-s', '--scale', type=float, default=1)
    parser.add_argument('-c', '--curve', type=float, default=1.2)
    parser.add_argument('image')
    main(parser.parse_args())
