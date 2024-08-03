import csv
import os
from typing import List
from db.repository import Repository
from model.lex import *


class CsvRepository(Repository):

    ROOT = os.path.dirname(os.path.abspath(__file__))
    LEXICON = "../data/lexicon.csv"

    def __init__(self):
        super().__init__()

    def load_lexicon(self) -> List[Lexentry]:
        try:
            with open(os.path.normpath(os.path.join(self.ROOT, self.LEXICON)),
                 'r', encoding='utf-8', newline='') as lexicon:
                csv_reader = csv.reader(lexicon)
                next(csv_reader)
                return [Lexentry(*row) for row in csv_reader]
        except FileNotFoundError:
            return []
