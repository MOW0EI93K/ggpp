from core.controllers import Controller
from core.arguments import parse_args
import multiprocessing
from core.utils import main
if __name__ == "__main__":
    main()
    multiprocessing.freeze_support()
    controller = Controller(
        arguments=parse_args())
    try:
        controller.join_workers()
    except KeyboardInterrupt:
        pass
