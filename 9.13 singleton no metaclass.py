class _Spam:
    def __init__(self):
        print('Creating Spam')


_spam_instance = None


def Spam():
    global _spam_instance
    if _spam_instance is None:
        _spam_instance = _Spam()
    return _spam_instance
