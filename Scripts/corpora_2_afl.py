import sys
import os
import os.path
import argparse
from shutil import copyfile

def _format(idx):
    """ Format to afl corpus
    """
    length = len(str(idx))
    fix_length = 6 - length
    return 'id:' + '0' * fix_length + str(idx) + ','

def is_bypass(p, n):
    if ',sync:' in n or '/.state' in p:
        return True
    return False

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='Corpora rename script for afl-fuzz')
    parser.add_argument('-i', '--input',required=True, help='input directory')
    parser.add_argument('-o', '--output',required=True, help='output directory')
    parser.add_argument('-n', '--number', type=int, required=False, default=0,
                        help='first id')
    parser.add_argument('--afl', required=False, action='store_true',
                        help='afl working directory')
    args = parser.parse_args()

    in_dir = args.input
    out_dir = args.output
    idx = args.number
    is_afl = args.afl

    try:
        os.makedirs(out_dir, exist_ok=True)
    except Exception as e:
        print(str(e))

    for (root, dirs, files) in os.walk(in_dir):
        for sample in files:
            if is_afl and is_bypass(root, sample):
                continue

            src_path = os.path.join(root, sample)
            afl_testcase = _format(idx) + sample
            target_path = os.path.join(out_dir, afl_testcase)
            copyfile(src_path, target_path)

            idx += 1
