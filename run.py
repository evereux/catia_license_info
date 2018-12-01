#! python3
# -*- coding: utf-8 -*-

from application_server import app
from application_server.main import main, pretty_print_log_data


def run_console():
    config_file = 'config.json'
    result = main(config_file)
    pretty_print_log_data(result)


def run_webapp():
    app.run(use_reloader=True, use_debugger=True, port=5000, debug=True)


if __name__ == '__main__':
    run_webapp()

    # console = '--console'
    # webserver = '--webserver'
    #
    # try:
    #     if sys.argv[1] == console:
    #         run_console()
    #     elif sys.argv[1] == webserver:
    #
    # except:
    #     print('Please append either "{}" or "{}" after {}.'.format(console, webserver, sys.argv[0]))
