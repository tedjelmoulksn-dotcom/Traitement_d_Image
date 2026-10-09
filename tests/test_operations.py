import unittest
import cv2
import numpy as np
from scipy.signal import convolve2d
from image_lab.operations import quantize_u8, mse_psnr, frequency_filter
from image_lab.runtime import michelson

class ImageOperationTests(unittest.TestCase):
    def test_quantisation_bins(self):
        ramp = np.arange(256, dtype=np.uint8)
        for levels in [2, 4, 8, 16, 32, 64, 128, 256]:
            output = quantize_u8(ramp, levels)
            self.assertEqual(np.unique(output).size, levels)
            self.assertEqual(output.dtype, np.uint8)
        with self.assertRaises(ValueError): quantize_u8(ramp, 3)

    def test_metric_avoids_unsigned_wrap(self):
        a = np.array([0, 255], dtype=np.uint8)
        b = np.array([255, 0], dtype=np.uint8)
        self.assertEqual(mse_psnr(a, b), (65025.0, 0.0))
        mse, psnr = mse_psnr(a, a)
        self.assertEqual(mse, 0); self.assertTrue(np.isinf(psnr))
        self.assertEqual(michelson(a), 1)
        self.assertEqual(michelson(np.zeros(4)), 0)

    def test_dc_and_complementary_frequency_masks(self):
        for shape in [(8, 12), (9, 11)]:
            constant = np.ones(shape)
            low, _, _ = frequency_filter(constant, 0)
            high, _, _ = frequency_filter(constant, 0, True)
            np.testing.assert_allclose(low, constant, atol=1e-12)
            np.testing.assert_allclose(high, 0, atol=1e-12)
            image = np.random.default_rng(42).normal(size=shape)
            low, _, _ = frequency_filter(image, 2)
            high, _, _ = frequency_filter(image, 2, True)
            np.testing.assert_allclose(low + high, image, atol=1e-12)

    def test_opencv_convolution_matches_scipy(self):
        image = np.random.default_rng(7).normal(size=(7, 11))
        kernel = np.array([[0, -1, 0], [1, 1, 1], [0, -1, 0]], dtype=float)
        cv = cv2.filter2D(image, cv2.CV_64F, np.flip(kernel), borderType=cv2.BORDER_REFLECT)
        scipy = convolve2d(image, kernel, mode="same", boundary="symm")
        np.testing.assert_allclose(cv, scipy, atol=1e-12)

if __name__ == "__main__": unittest.main()
