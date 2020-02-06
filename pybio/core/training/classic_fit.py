from pybio.spec.node import Model
from pybio.spec.utils import get_instance


def classic_fit(pybio_model: Model, start: int = 0, batch_size: int = 1):
    """classic fit a la 'model.fit(X, y)'"""

    model = get_instance(pybio_model)
    readers = [get_instance(r) for r in pybio_model.spec.training.setup.readers]
    sampler = get_instance(pybio_model.spec.training.setup.sampler, readers=readers)
    X, y = sampler[start, batch_size]
    model.fit([X], [y])
    return model
    # todo: save/return model weights/checkpoint?!?
