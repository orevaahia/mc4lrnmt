import logging
import random

from polyglot.text import Text
from polyglot.detect.base import logger as polyglot_logger

polyglot_logger.setLevel("ERROR")



class CleanTest:
    """
    This class takes in separate source and target files and does the following.
    1. Remove duplicate entries
    2. Tokenize  the data
    """
    def __init__(self, source: str, target: str):
        self.src = source
        self.trg = target

    def read_file(self):
        logging.info(
            "Reading parallel files in"
        )
        with open(self.src, 'r') as source_file, open(self.trg, 'r') as target_file:
            source_text = source_file.read().splitlines()
            target_text = target_file.read().splitlines()
        assert len(source_text) == len(target_text)

        return source_text, target_text

    def tokenize(self, lc: bool=False):
        """
        Tokenize sentences using polyglot
        """
        logging.info(
            "Reading parallel files in"
        )
        source_text, target_text = self.read_file()

        tokenized_src_sentences = []
        tokenized_trg_sentences = []
        for src in source_text:
            src_i = Text(src, hint_language_code="en").words
            tokenized_src = " ".join(src_i)
            if lc:
                tokenized_src = tokenized_src.lower()
            tokenized_src_sent = tokenized_src
            tokenized_src_sentences.append(tokenized_src_sent)

        for trg in target_text:
            trg_i = Text(trg, hint_language_code="ig").words
            tokenized_trg = " ".join(trg_i)
            if lc:
                tokenized_trg = tokenized_trg.lower()
            tokenized_trg_sent = tokenized_trg
            tokenized_trg_sentences.append(tokenized_trg_sent)

        return tokenized_src_sentences, tokenized_trg_sentences



    def remove_duplicates(self, tokenize: bool=True) -> None:
        """
        Remove duplicates in source and target test sets 
        """
        source_file = self.src[:-3] + '-tokenized' + self.src[-3:]
        target_file = self.trg[:-3] + '-tokenized' + self.trg[-3:]
        
        if tokenize:
            source_sentences, target_sentences = self.tokenize()
        else:
            source_sentences, target_sentences = self.read_file()

        parallel_dict = dict(zip(source_sentences, target_sentences))
        unique_source = set(source_sentences)
        
        new_dict = {}
        for key, value in parallel_dict.items():
            if key in unique_source:
                new_dict[key] = value
        
        logging.info(
            f"The length of sentences after cleaning is {len(new_dict)}"
        )
        with open(source_file, 'w') as source_filehandle:
            for source_listitem in list(new_dict.keys()):
                source_filehandle.write('%s\n' % source_listitem)
                
        with open(target_file, 'w') as target_filehandle:
            for target_listitem in list(new_dict.values()):
                target_filehandle.write('%s\n' % target_listitem)
        logging.info(
            "Finished cleaning and saving files"
        )


class SampleData:
    """
    This class takes in separate source and target files and does the following.
    1. Shuffles the data and returns a sample of the parallel sentences
    """
    def __init__(self, source: str, target: str):
        self.src = source
        self.trg = target
        
    def read_file(self):
        """
        Read files in
        """
        with open(self.src, 'r') as source_file, open(self.trg, 'r') as target_file:
            source_text = source_file.read().splitlines()
            target_text = target_file.read().splitlines()

        assert len(source_text) == len(target_text)

        return source_text, target_text
    
    def shuffle(self):
        source_text, target_text = self.read_file()
        parallel_dict = dict(zip(source_text, target_text))
        dict_list = list(parallel_dict.items())
        random.seed(42)
        random.shuffle(dict_list)

        shuffled_dict = dict(dict_list)

        return shuffled_dict
    
    def create_new_file(self, sample_size):
        shuffled_dict = self.shuffle()
        
        source_file = self.src[:-3] + '-sampled-' + str(sample_size) + self.src[-3:]
        target_file = self.trg[:-3] + '-sampled-' + str(sample_size) + self.trg[-3:]

        assert sample_size < len(shuffled_dict)

        with open(source_file, 'w') as source_filehandle:
            for source_listitem in list(shuffled_dict.keys())[:sample_size]:
                source_filehandle.write('%s\n' % source_listitem)

        with open(target_file, 'w') as target_filehandle:
            for target_listitem in list(shuffled_dict.values())[:sample_size]:
                target_filehandle.write('%s\n' % target_listitem)
