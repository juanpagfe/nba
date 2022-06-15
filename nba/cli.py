#!/usr/bin/env python3
from urllib.request import urlopen
import json, argparse
URL = "https://mach-eight.uc.r.appspot.com/"

def parse_args():
    """Parses arguments and prevent argument errors"""
    parser = argparse.ArgumentParser(prog='nba', usage='%(prog)s [target]', add_help=False)
    parser._optionals.title = "argumentos opcionales"
    parser._positionals.title = "argumentos posicionales"
    parser.add_argument("target", metavar='target', type=int, nargs=1, help="El tamaño debe ser un número entero en pulgadas")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Mostrar este mensaje de ayuda')
    args = parser.parse_args()
    if args.target is None:
        parser.print_help()
    return args

def printPairs(target):
    """Find the pairs of players that when their height is sumarized, is equals to the given target"""
    with urlopen(URL) as response:
        players = json.loads(response.read())['values']
        result = ""
        while len(players) > 0:
            first = players.pop(0)
            for second in players:
                num = num + 1
                if int(first['h_in']) + int(second['h_in']) == target:
                    result = result + '- {} {}\t\t{} {}{}'.format(first['first_name'], first['last_name'], 
                    second['first_name'], second['last_name'], "\n" if len(players) > 0 else "")
        print(result.strip() if result != "" else 'No se encontraron coincidencias')

def run():
    args = parse_args()
    printPairs(args.target[0])
