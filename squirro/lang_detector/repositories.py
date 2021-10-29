from .models import Snippet


class StoreException(Exception):
    pass


class DBRepository:
    def add(self, snippet):
        try:
            return Snippet.objects.create(**snippet)
        except Exception as e:
            raise StoreException(e)

    def get(self, key):
        try:
            return Snippet.objects.get(pk=key)
        except Exception as e:
            raise StoreException(e)

    def update(self, instance, values):
        try:
            instance.text = values.get("text", instance.text)
            instance.language = values.get("language", instance.language)
            instance.save()
            return instance
        except Exception as e:
            raise StoreException(e)
