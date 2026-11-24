"""모듈 인계 예제를 위한 속도 감시 모델.

속도는 0.1 km/h 단위, 시간은 정수 밀리초 단위를 사용한다.
문서와 코드의 추적성을 보여 주는 예제이며 차량 소프트웨어가 아니다.
"""


class SpeedMonitor:
    def __init__(self) -> None:
        self.powered = True
        self.invalid = False
        self.last_valid_ms: int | None = None
        self.consecutive_valid = 0

    def receive(self, speed_deci_kmh: int, now_ms: int) -> None:
        if not self.powered:
            return
        if speed_deci_kmh < 0 or speed_deci_kmh > 2500:
            self.invalid = True
            self.consecutive_valid = 0
            return

        self.last_valid_ms = now_ms
        if self.invalid:
            self.consecutive_valid += 1
            if self.consecutive_valid >= 3:
                self.invalid = False
                self.consecutive_valid = 0

    def tick(self, now_ms: int) -> None:
        if self.powered and self.last_valid_ms is not None:
            if now_ms - self.last_valid_ms > 100:
                self.invalid = True
                self.consecutive_valid = 0

    def power_off(self) -> None:
        self.powered = False
        self.invalid = False
        self.last_valid_ms = None
        self.consecutive_valid = 0

    def power_on(self) -> None:
        self.powered = True
