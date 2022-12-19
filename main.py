from pathlib import Path
from people_detector import PeopleDetector
import argparse

if __name__ == '__main__':
	input_path = Path('input/')
	output_path = Path('output/')

	pd = PeopleDetector(input_path, output_path)
	pd.process()
