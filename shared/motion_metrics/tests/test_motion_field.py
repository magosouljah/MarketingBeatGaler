import unittest

try:
    import numpy as np
    import cv2  # noqa: F401
    from shared.motion_metrics import motion_field as mf
except ImportError:  # optional dependency
    mf = None


def textured_card(size, seed):
    rng = np.random.default_rng(seed)
    t = rng.integers(0, 255, (size // 4, size // 4, 3), dtype=np.uint8)
    t = cv2.resize(t, (size, size), interpolation=cv2.INTER_CUBIC)
    return cv2.GaussianBlur(t, (5, 5), 0)


def paste(canvas, card, cx, cy):
    s = card.shape[0]
    x0, y0 = int(cx - s / 2), int(cy - s / 2)
    canvas[y0:y0 + s, x0:x0 + s] = card


@unittest.skipIf(mf is None, "numpy/OpenCV not installed")
class MotionFieldTests(unittest.TestCase):
    H, W = 320, 180

    def blank(self):
        return np.full((self.H, self.W, 3), 20, np.uint8)

    def test_rigid_translation_is_explained_by_affine(self):
        card = textured_card(64, 1)
        frames = []
        for i in range(6):
            f = self.blank()
            paste(f, card, 60 + 3 * i, 160)
            frames.append(f)
        res = mf.analyze(frames, 30.0)
        s = res["summary"]
        self.assertLess(s["affine_residual"], 0.25)
        self.assertGreater(s["coherence"], 0.9)

    def test_independent_opposite_motion_is_not_affine(self):
        a, b = textured_card(48, 2), textured_card(48, 3)
        frames = []
        for i in range(6):
            f = self.blank()
            paste(f, a, 50 + 3 * i, 80)     # top card moves right
            paste(f, b, 130 - 3 * i, 120)   # card just below moves left
            paste(f, a, 90, 230 - 3 * i)    # third card moves up
            frames.append(f)
        res = mf.analyze(frames, 30.0)
        s = res["summary"]
        self.assertGreater(s["affine_residual"], 0.4)
        self.assertLess(s["coherence"], 0.6)

    def test_static_frames_report_no_motion(self):
        card = textured_card(64, 4)
        f = self.blank()
        paste(f, card, 90, 160)
        res = mf.analyze([f.copy() for _ in range(4)], 30.0)
        self.assertEqual(res["summary"]["speed_med"], 0.0)
        self.assertIsNone(res["summary"]["affine_residual"])


if __name__ == "__main__":
    unittest.main()
