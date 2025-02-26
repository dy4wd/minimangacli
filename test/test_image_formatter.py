import unittest

from pathlib import Path

from minimanga.image_formatter import _generate_path_to_save
from minimanga.config import SUFFIX_FOLDER_TO_SAVE


class TestImagesFormatter(unittest.TestCase):

    def test_generate_path_to_save(self):
        folder_to_save = Path(f"/home/user/Documents/Manga/manganame_{SUFFIX_FOLDER_TO_SAVE}/")
        image = Path("/home/user/Documents/Manga/manganame/vol/001.jpg")
        self.assertEqual(_generate_path_to_save(folder_to_save, image), Path(f"/home/user/Documents/Manga/manganame{SUFFIX_FOLDER_TO_SAVE}/vol/001.jpg"))


