from typing import Tuple, Dict, Any

class IsoTpError(Exception):
    def __init__(self,
                 *args: Tuple[Any],
                 **kwargs: Dict[Any, Any]) -> None: ...

class FlowControlTimeoutError(IsoTpError): ...
class ConsecutiveFrameTimeoutError(IsoTpError): ...
class InvalidCanDataError(IsoTpError): ...
class UnexpectedFlowControlError(IsoTpError): ...
class UnexpectedConsecutiveFrameError(IsoTpError): ...
class ReceptionInterruptedWithSingleFrameError(IsoTpError): ...
class ReceptionInterruptedWithFirstFrameError(IsoTpError): ...
class WrongSequenceNumberError(IsoTpError): ...
class UnsuportedWaitFrameError(IsoTpError): ...
class MaximumWaitFrameReachedError(IsoTpError): ...
class FrameTooLongError(IsoTpError): ...
class ChangingInvalidRXDLError(IsoTpError): ...
class MissingEscapeSequenceError(IsoTpError): ...
class InvalidCanFdFirstFrameRXDL(IsoTpError): ...
class OverflowError(IsoTpError): ...
