from modeltranslation.translator import translator, TranslationOptions
from user import models


class UserTranslationOptions(TranslationOptions):
    fields = (
        'address',
    )


translator.register(models.User, UserTranslationOptions)
