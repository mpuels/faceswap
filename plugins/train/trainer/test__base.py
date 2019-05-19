import datetime as dt
from pathlib import Path

import cv2
import numpy as np
from keras.models import Model as KerasModel

from plugins.train.model._base import ModelBase
from plugins.train.trainer._base import Samples

TEST_IMG_OUTPUT_ROOT = Path("/tmp/faceswap-test")
TEST_IMG_OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
for f in TEST_IMG_OUTPUT_ROOT.iterdir():
    f.unlink()


class ModelBaseMock(ModelBase):
    """Mock for class ModelBase."""

    # noinspection PyMissingConstructor
    def __init__(self,
                 name: str,
                 iterations: int,
                 predictor_mock_a: KerasModel,
                 predictor_mock_b: KerasModel,
                 face_input_shape: tuple):
        """Constructor.

        :param name: Property self.name will return this value.
        :param iterations: Property self.iterations will return this value.
        :param predictor_mock_a: Is available under self.predictors["a"].
        :param predictor_mock_b: Is available under self.predictors["b"].
        :param face_input_shape: Shape (height, width) of face images. Property
            self.input_shape will return this value.
        """
        self._name = name
        self.input_shape = face_input_shape
        self._iterations = iterations
        self.predictors = {
            "a": predictor_mock_a,
            "b": predictor_mock_b,
        }

    @property
    def config(self):
        raise NotImplementedError()

    @property
    def config_section(self):
        raise NotImplementedError()

    @property
    def config_changeable_items(self):
        raise NotImplementedError()

    @property
    def name(self):
        return self._name

    @property
    def models_exist(self):
        raise NotImplementedError()

    @staticmethod
    def set_gradient_type(memory_saving_gradients):
        raise NotImplementedError()

    def set_training_data(self):
        raise NotImplementedError()

    def calculate_coverage_ratio(self):
        raise NotImplementedError()

    def build(self):
        raise NotImplementedError()

    def build_autoencoders(self):
        raise NotImplementedError()

    def add_networks(self):
        raise NotImplementedError()

    def load_state_info(self):
        raise NotImplementedError()

    def add_network(self, network_type, side, network):
        raise NotImplementedError()

    def add_predictor(self, side, model):
        raise NotImplementedError()

    def store_input_shapes(self, model):
        raise NotImplementedError()

    def set_output_shape(self, model):
        raise NotImplementedError()

    def reset_pingpong(self):
        raise NotImplementedError()

    def compile_predictors(self, initialize=True):
        raise NotImplementedError()

    def get_optimizer(self, lr=5e-5, beta_1=0.5, beta_2=0.999):
        raise NotImplementedError()

    def loss_function(self, mask, side, initialize):
        raise NotImplementedError()

    def mask_loss_function(self, side, initialize):
        raise NotImplementedError()

    def converter(self, swap):
        raise NotImplementedError()

    @property
    def iterations(self):
        return self._iterations

    def map_models(self, swapped):
        raise NotImplementedError()

    def log_summary(self):
        raise NotImplementedError()

    def load_models(self, swapped):
        raise NotImplementedError()

    def save_models(self):
        raise NotImplementedError()

    def get_save_averages(self):
        raise NotImplementedError()

    def check_loss_drop(self, side, avg):
        raise NotImplementedError()

    def rename_legacy(self):
        raise NotImplementedError()


class KerasModelMock(KerasModel):
    # noinspection PyMissingConstructor
    def __init__(self, side: str):
        """Mock a KerasModel that was trained to swap faces.

        No base method is implemented, except `predict()`.

        Parameters
        ----------
        side : Name of the predictor. When PredictorMock.feed() is called with a batch
            of n images, then PredictorMock.feed() will return n images of size
            (FACE_HEIGHT, FACE_WIDTH) where the i-th image has the text "<side>: <i>"
            on it.
        """
        self._side = side

    def predict(self, x: np.ndarray, batch_size=None, verbose=0, steps=None) -> np.ndarray:
        """Mock a prediction for each face image in x.

        Instead of replacing a face with another face, this method draws the
        string f"{self._side}: {i}" for the i-th image in `x`.

        Parameters
        ----------
        x
            Shape of x must be (batch_size, face_height, face_width, channels).
        batch_size
            Not used.
        verbose
            Not used.
        steps
            Not used.

        Returns
        -------
        np.ndarray of same shape as `x`.
        """
        predictions = np.zeros(x.shape)
        for i in range(x.shape[0]):
            background_img = np.zeros(x.shape[1:], np.uint8)
            predictions[i] = cv2.putText(background_img,
                                         f'{self._side}:{i + 1}',
                                         (10, 40),
                                         cv2.FONT_HERSHEY_SIMPLEX,
                                         0.8,
                                         (255, 255, 255),
                                         2)
        return predictions

    def compile(self,
                optimizer,
                loss=None,
                metrics=None,
                loss_weights=None,
                sample_weight_mode=None,
                weighted_metrics=None,
                target_tensors=None,
                **kwargs):
        raise NotImplementedError()

    def fit(self,
            x=None,
            y=None,
            batch_size=None,
            epochs=1,
            verbose=1,
            callbacks=None,
            validation_split=0.,
            validation_data=None,
            shuffle=True,
            class_weight=None,
            sample_weight=None,
            initial_epoch=0,
            steps_per_epoch=None,
            validation_steps=None,
            **kwargs):
        raise NotImplementedError()

    def evaluate(self,
                 x=None,
                 y=None,
                 batch_size=None,
                 verbose=1,
                 sample_weight=None,
                 steps=None):
        raise NotImplementedError()

    def train_on_batch(self, x, y, sample_weight=None, class_weight=None):
        raise NotImplementedError()

    def test_on_batch(self, x, y, sample_weight=None):
        raise NotImplementedError()

    def predict_on_batch(self, x):
        raise NotImplementedError()

    def fit_generator(self,
                      generator,
                      steps_per_epoch=None,
                      epochs=1,
                      verbose=1,
                      callbacks=None,
                      validation_data=None,
                      validation_steps=None,
                      class_weight=None,
                      max_queue_size=10,
                      workers=1,
                      use_multiprocessing=False,
                      shuffle=True,
                      initial_epoch=0):
        raise NotImplementedError()

    def evaluate_generator(self,
                           generator,
                           steps=None,
                           max_queue_size=10,
                           workers=1,
                           use_multiprocessing=False,
                           verbose=0):
        raise NotImplementedError()

    def predict_generator(self,
                          generator,
                          steps=None,
                          max_queue_size=10,
                          workers=1,
                          use_multiprocessing=False,
                          verbose=0):
        raise NotImplementedError()


def generate_images(label: str,
                    num_images: int,
                    height: int,
                    width: int) -> np.ndarray:
    """Generate num_images images.

    The i-th generated image has the text "<label>:<i>" on it.

    :param label:
    :param num_images:
    :param height:
    :param width:
    :return: The returned np.ndarray has the shape (num_images, height, width, 3).
    """
    images = np.zeros((num_images, height, width, 3))
    for i in range(num_images):
        background_img = np.zeros((height, width, 3), np.uint8)
        images[i] = cv2.putText(background_img,
                                f'{label}:{i + 1}',
                                (5, 25),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (255, 255, 0),
                                2)
    return images


def test_samples():
    # given
    batch_size = 14
    iterations = 45678

    predictor_mock_a = KerasModelMock("a")
    predictor_mock_b = KerasModelMock("b")

    face_height = 64
    face_width = 64

    model_name = "mock"

    model = ModelBaseMock(model_name,
                          iterations,
                          predictor_mock_a,
                          predictor_mock_b,
                          (face_height, face_width))
    use_mask = False
    coverage_ratio = 0.625
    scaling = 1.0

    def func_utc_now_mock():
        return dt.datetime(2019, 5, 19, 20, 21)

    samples = Samples(model,
                      use_mask,
                      coverage_ratio,
                      batch_size,
                      scaling=scaling,
                      func_utc_now=func_utc_now_mock)

    frame_height = 128
    frame_width = 128
    full_images_a = generate_images("fa", batch_size, frame_height, frame_width)
    full_images_b = generate_images("fb", batch_size, frame_height, frame_width)
    faces_a = np.ones((batch_size, face_height, face_width, 3))
    faces_b = np.ones((batch_size, face_height, face_width, 3))
    samples.images["a"] = [full_images_a, faces_a]
    samples.images["b"] = [full_images_b, faces_b]

    # when
    training_preview = samples.show_sample()

    cv2.imwrite(str(TEST_IMG_OUTPUT_ROOT / "training-preview.png"), training_preview)


def test_predictor_mock():
    face_height = 64
    face_width = 64
    predictor_mock = KerasModelMock("a")
    faces = np.zeros((6, face_height, face_width, 3))
    predicted_faces = predictor_mock.predict(faces)
    for i, predicted_face in enumerate(predicted_faces):
        cv2.imwrite(str(TEST_IMG_OUTPUT_ROOT / f"predictor-mock-{i}.png"), predicted_face)


def test_generate_images():
    height = 128
    width = 128
    images = generate_images("fb", 4, height, width)
    for i, image in enumerate(images):
        cv2.imwrite(str(TEST_IMG_OUTPUT_ROOT / f"generated-images-{i}.png"), image)
