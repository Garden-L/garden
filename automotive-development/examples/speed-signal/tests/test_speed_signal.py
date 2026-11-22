import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from speed_signal import SpeedMonitor


class SpeedSignalTests(unittest.TestCase):
    def test_TC_001_accepts_valid_range_boundaries(self) -> None:
        monitor = SpeedMonitor()
        monitor.receive(0, 0)
        self.assertFalse(monitor.invalid)
        monitor.receive(2500, 1)
        self.assertFalse(monitor.invalid)

    def test_TC_002_rejects_outside_range(self) -> None:
        for value in (-1, 2501):
            with self.subTest(value=value):
                monitor = SpeedMonitor()
                monitor.receive(value, 0)
                self.assertTrue(monitor.invalid)

    def test_TC_003_timeout_is_strictly_after_100_ms(self) -> None:
        monitor = SpeedMonitor()
        monitor.receive(100, 0)
        monitor.tick(100)
        self.assertFalse(monitor.invalid)
        monitor.tick(101)
        self.assertTrue(monitor.invalid)

    def test_TC_004_three_valid_messages_recover(self) -> None:
        monitor = SpeedMonitor()
        monitor.receive(-1, 0)
        for now_ms in (1, 2):
            monitor.receive(100, now_ms)
            self.assertTrue(monitor.invalid)
        monitor.receive(100, 3)
        self.assertFalse(monitor.invalid)

    def test_TC_005_power_off_clears_and_pauses_monitoring(self) -> None:
        monitor = SpeedMonitor()
        monitor.receive(100, 0)
        monitor.tick(101)
        self.assertTrue(monitor.invalid)
        monitor.power_off()
        self.assertFalse(monitor.invalid)
        monitor.tick(500)
        self.assertFalse(monitor.invalid)
        monitor.power_on()
        monitor.receive(100, 501)
        monitor.tick(601)
        self.assertFalse(monitor.invalid)


if __name__ == "__main__":
    unittest.main()
