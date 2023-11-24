from tensorflow import keras

from prophecy.utils.paths import models_path


def get_model(model: str, version: str) -> keras.Model:
    model_path = models_path / f"{model}{version}.h5"

    if not model_path.exists():
        raise ValueError(f"{model_path} does not exist")

    return keras.models.load_model(str(model_path))
