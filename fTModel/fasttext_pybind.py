# encoding: utf-8
# module fasttext_pybind
# from F:\WorkSpace\git\repositories\Heroku-WebApp\venv\lib\site-packages\fasttext_pybind.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


# functions

def train(arg0, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """ train(arg0: fasttext::FastText, arg1: fasttext_pybind.args) -> None """
    pass


# classes

class args(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: fasttext_pybind.args) -> None """
        pass

    bucket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cutoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dsub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    epoch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lrUpdateRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minCountLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    neg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretrainedVectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qnorm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saveOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verbose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wordNgrams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class fasttext(__pybind11_builtins.pybind11_object):
    # no doc
    def getArgs(self):  # real signature unknown; restored from __doc__
        """ getArgs(self: fasttext_pybind.fasttext) -> fasttext_pybind.args """
        pass

    def getInputMatrix(self):  # real signature unknown; restored from __doc__
        """ getInputMatrix(self: fasttext_pybind.fasttext) -> fasttext_pybind.Matrix """
        pass

    def getInputVector(self, arg0, arg1):  # real signature unknown; restored from __doc__
        """ getInputVector(self: fasttext_pybind.fasttext, arg0: fasttext_pybind.Vector, arg1: int) -> None """
        pass

    def getLabels(self):  # real signature unknown; restored from __doc__
        """ getLabels(self: fasttext_pybind.fasttext) -> Tuple[List[str], List[int]] """
        pass

    def getLine(self, arg0):  # real signature unknown; restored from __doc__
        """ getLine(self: fasttext_pybind.fasttext, arg0: str) -> Tuple[List[str], List[str]] """
        pass

    def getOutputMatrix(self):  # real signature unknown; restored from __doc__
        """ getOutputMatrix(self: fasttext_pybind.fasttext) -> fasttext_pybind.Matrix """
        pass

    def getSentenceVector(self, arg0, arg1):  # real signature unknown; restored from __doc__
        """ getSentenceVector(self: fasttext_pybind.fasttext, arg0: fasttext_pybind.Vector, arg1: str) -> None """
        pass

    def getSubwordId(self, arg0):  # real signature unknown; restored from __doc__
        """ getSubwordId(self: fasttext_pybind.fasttext, arg0: str) -> int """
        return 0

    def getSubwords(self, arg0):  # real signature unknown; restored from __doc__
        """ getSubwords(self: fasttext_pybind.fasttext, arg0: str) -> Tuple[List[str], List[int]] """
        pass

    def getVocab(self):  # real signature unknown; restored from __doc__
        """ getVocab(self: fasttext_pybind.fasttext) -> Tuple[List[str], List[int]] """
        pass

    def getWordId(self, arg0):  # real signature unknown; restored from __doc__
        """ getWordId(self: fasttext_pybind.fasttext, arg0: str) -> int """
        return 0

    def getWordVector(self, arg0, arg1):  # real signature unknown; restored from __doc__
        """ getWordVector(self: fasttext_pybind.fasttext, arg0: fasttext_pybind.Vector, arg1: str) -> None """
        pass

    def isQuant(self):  # real signature unknown; restored from __doc__
        """ isQuant(self: fasttext_pybind.fasttext) -> bool """
        return False

    def loadModel(self, arg0):  # real signature unknown; restored from __doc__
        """ loadModel(self: fasttext_pybind.fasttext, arg0: str) -> None """
        pass

    def multilineGetLine(self, arg0, p_str=None):  # real signature unknown; restored from __doc__
        """ multilineGetLine(self: fasttext_pybind.fasttext, arg0: List[str]) -> Tuple[List[List[str]], List[List[str]]] """
        pass

    def predict(self, arg0, arg1, arg2):  # real signature unknown; restored from __doc__
        """ predict(self: fasttext_pybind.fasttext, arg0: str, arg1: int, arg2: float) -> List[Tuple[float, str]] """
        return []

    def quantize(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8,
                 arg9):  # real signature unknown; restored from __doc__
        """ quantize(self: fasttext_pybind.fasttext, arg0: str, arg1: bool, arg2: int, arg3: bool, arg4: int, arg5: float, arg6: int, arg7: int, arg8: int, arg9: bool) -> None """
        pass

    def saveModel(self, arg0):  # real signature unknown; restored from __doc__
        """ saveModel(self: fasttext_pybind.fasttext, arg0: str) -> None """
        pass

    def test(self, arg0, arg1):  # real signature unknown; restored from __doc__
        """ test(self: fasttext_pybind.fasttext, arg0: str, arg1: int) -> Tuple[int, float, float] """
        pass

    def tokenize(self, arg0):  # real signature unknown; restored from __doc__
        """ tokenize(self: fasttext_pybind.fasttext, arg0: str) -> List[str] """
        return []

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: fasttext_pybind.fasttext) -> None """
        pass


class loss_name(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: fasttext_pybind.loss_name, arg0: fasttext_pybind.loss_name) -> bool """
        return False

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: fasttext_pybind.loss_name) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: fasttext_pybind.loss_name) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: fasttext_pybind.loss_name, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: fasttext_pybind.loss_name) -> int """
        return 0

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: fasttext_pybind.loss_name, arg0: fasttext_pybind.loss_name) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: fasttext_pybind.loss_name) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: fasttext_pybind.loss_name, arg0: tuple) -> None """
        pass

    hs = None  # (!) forward: hs, real value is ''
    ns = None  # (!) forward: ns, real value is ''
    softmax = None  # (!) forward: softmax, real value is ''
    __members__ = {
        'hs': '<failed to retrieve the value>',
        'ns': '<failed to retrieve the value>',
        'softmax': '<failed to retrieve the value>',
    }


class Matrix(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: fasttext_pybind.Matrix) -> None

        2. __init__(self: fasttext_pybind.Matrix, arg0: int, arg1: int) -> None
        """
        pass

    __pybind11_module_local_v2__ = None  # (!) real value is ''


class model_name(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: fasttext_pybind.model_name, arg0: fasttext_pybind.model_name) -> bool """
        return False

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: fasttext_pybind.model_name) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: fasttext_pybind.model_name) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: fasttext_pybind.model_name, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: fasttext_pybind.model_name) -> int """
        return 0

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: fasttext_pybind.model_name, arg0: fasttext_pybind.model_name) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: fasttext_pybind.model_name) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: fasttext_pybind.model_name, arg0: tuple) -> None """
        pass

    cbow = None  # (!) forward: cbow, real value is ''
    skipgram = None  # (!) forward: skipgram, real value is ''
    supervised = None  # (!) forward: supervised, real value is ''
    __members__ = {
        'cbow': '<failed to retrieve the value>',
        'skipgram': '<failed to retrieve the value>',
        'supervised': '<failed to retrieve the value>',
    }


class Vector(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: fasttext_pybind.Vector, arg0: int) -> None """
        pass


# variables with complex values

cbow = None  # (!) real value is ''

hs = None  # (!) real value is ''

ns = None  # (!) real value is ''

skipgram = None  # (!) real value is ''

softmax = None  # (!) real value is ''

supervised = None  # (!) real value is ''

__loader__ = None  # (!) real value is ''

__spec__ = None  # (!) real value is ''

