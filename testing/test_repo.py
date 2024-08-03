import pytest
from db.mysql_repo import MysqlRepository
from db.csv_repo import CsvRepository
from model.lex import Lexentry

raw_out = [('coffee', 'ˈkʰɔ.fi', 'noun', 'boiled bean water'),
           ('drink', 'dɹɪŋk', 'verb', 'to imbibe')]

lexentries_out = [Lexentry(*item) for item in raw_out]

# For toggling between database implementations
#REPOTYPE = 'MySQL'
REPOTYPE = 'CSV'


def test_load_dict():
    if REPOTYPE == 'MySQL':
        repo = MysqlRepository()
    elif REPOTYPE == 'CSV':
        repo = CsvRepository()
    result = repo.load_lexicon()
    foundmatch = [any([item == entry for entry in lexentries_out]) for item in result]
    assert all(foundmatch)
