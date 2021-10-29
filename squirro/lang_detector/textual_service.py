from .language_detector import LanguageDetector
from .repositories import DBRepository


class TextualService:
    """Service which detects the language of incoming data before
    storing it."""

    def __init__(self):
        self.ld = LanguageDetector()
        self.store = DBRepository()

    def add(self, key, value):
        lang = self.ld.process(value)
        instance = self.store.add({'id': key, 'text': value, 'language': lang})
        return instance

    def get(self, key):
        ret = self.store.get(key)
        return ret

    def update(self, instance, values):
        lang = self.ld.process(values.get("text"))
        values["language"] = lang
        instance = self.store.update(instance, values)
        return instance
