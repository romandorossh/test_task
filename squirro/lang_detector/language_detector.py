class LanguageDetector:
    """Dummy language detector which makes use of a language specific rule
    set."""

    def __init__(self):
        pass

    def process(self, text):
        """Detect the language for the provided `text`. Returns a
        two-letter language code (ISO 639-1)."""
        text = text.lower()

        german_articles = ["die", "der", "das"]
        if any(art in text for art in german_articles) or u'z\xfcrich' in text:
            ret = 'de'
        else:
            ret = 'en'
        return ret
