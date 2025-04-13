from abc import ABC,abstractmethod

from app.models.gpt_model import GPTSource


class GPT(ABC):
    def summarize(self, source:GPTSource )->str:
        '''

        :param source: 
        :return:
        '''
        pass