from pathlib import Path
from multiprocessing import Pool
import cv2
import numpy as np
import logging

class PeopleDetector:
    MAX_THREADS_COUNT: int = 6

    def __init__(self, input_images_dir: Path, output_images_dir: Path):
        self.__configure_logging()

        self.__input_images_dir: Path = input_images_dir
        self.__output_images_dir: Path = output_images_dir

        if not (self.__input_images_dir.exists() or self.__output_images_dir.exists()):
            raise Exception("Input or output path doesn't exist !")

        self.__images_to_process: List = list()

    def __configure_logging(self):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    def __load_images_to_process(self):
        for f in self.__input_images_dir.iterdir():
            if f.is_file():
                self.__images_to_process.append(f.name)
                logging.debug(f"[+] Loaded image: {f.name}")

    def detect_and_save_results(self, image_name: str):
        logging.info(f"[+] Processing image: {image_name}")

        body_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        input_path = str(self.__input_images_dir / image_name)
        output_path = str(self.__output_images_dir / image_name)


        img = cv2.imread(input_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        boxes = body_cascade.detectMultiScale(img_gray, 1.3, 5)

        if not len(boxes):
            logging.warn(f"[-] Empty image: {image_name}")
            return
        else:
            logging.warn(f"[+] Processed image: {image_name}")

        for (x, y, w, h) in boxes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imwrite(output_path, img)

    '''
    Core method. Detect people on given images and save results.
    '''
    def process(self):
        self.__load_images_to_process()

        with Pool(PeopleDetector.MAX_THREADS_COUNT) as pool:
            pool.map(self.detect_and_save_results, self.__images_to_process[:40])



