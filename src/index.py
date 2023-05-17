import os
import threading
import webview
import argparse
from time import time
from lib.serialhandler import SerialHandler, DataFrame, FormatData, FileHandler
from lib.api import Api

dataframe = None
file_handler = None
serial_handler = None
args = None


def get_entrypoint():

    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../gui/index.html'):  # unfrozen development
        return '../gui/index.html'

    if exists('../Resources/gui/index.html'):  # frozen py2app
        return '../Resources/gui/index.html'

    if exists('./gui/index.html'):
        return './gui/index.html'

    raise Exception('No index.html found')


def set_interval(interval):

    def decorator(function):

        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop():  # executed in another thread
                while not stopped.wait(interval):  # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True  # stop if the program exits
            t.start()
            return stopped

        return wrapper

    return decorator


entry = get_entrypoint()


@set_interval(1)
def update_ticker():
    if len(webview.windows) > 0:
        webview.windows[0].evaluate_js(
            'window.pywebview.state.setTicker("%d")' % time())


@set_interval(.01)
def get_data_from_serial():
    raise NotImplementedError()


def init_serial_connection():
    global dataframe
    global file_handler
    global serial_handler

    dataframe = DataFrame()
    file_handler = FileHandler(dataframe)
    serial_handler = SerialHandler(args.port, args.boudrate)


if __name__ == '__main__':
    global args

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('port', type=str, help='Serial Port path')
    parser.add_argument('boudrate', type=int, help='Serial Port boudrate')

    args = parser.parse_args()

    init_serial_connection()

    window = webview.create_window('pywebview-react boilerplate',
                                   entry,
                                   js_api=Api())
    webview.start(update_ticker, debug=True)
