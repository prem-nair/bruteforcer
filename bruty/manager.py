import requests

from time import sleep
from colorama import Fore
from collections import deque
from threading import Thread, active_count, Lock, current_thread

from requests.sessions import Session

lock = Lock()


class BruteManager():
    def __init__(self, pathToFile: str, debugMode: bool = False):
        self.cpm = 0
        self.success = 0
        self.fails = 0
        self.checked = 0
        self.retries = 0
        self.debugMode = debugMode
        self.allItems = deque()

        with open(pathToFile, 'r') as f:
            for i in f:
                if i.strip() != '':
                    self.allItems.append(i.strip())

        self.totalitems = len(self.allItems)

    def timer(self):
        sleep(1)
        counter = 0
        while True:
            threads = active_count()

            if threads <= 2:
                break
            with lock:
                counter += 1
                self.cpm = int(self.checked / counter * 60)
            # Subtract 2 from threads var because we have a main thread
            # and a thread for this function to run
            title = f'Progress {self.checked/self.totalitems*100:.2f}% | Checks Per Minute {self.cpm} | Success {self.success} | Fails {self.fails} | Retries {self.retries} | Threads {threads-2}'
            print(f'\x1B]0;{title}\x07', end='')
            sleep(0.5)
        sleep(1)

    def worker(self, function: function, *args, **kwargs):
        while True:
            with lock:
                if len(self.allItems) > 0:
                    item = self.allItems.popleft()
                else:
                    self.dprint('THREAD ENDED')
                    self.dprint(str(current_thread()))
                    return

            while True:
                try:
                    success = function(*args, 
                                       **kwargs)
                    with lock:
                        self.checked += 1
                        if success:
                            self.success += 1
                        else:
                            self.fails += 1
                    break
                except TypeError as e:
                    self.dprint(str(e))
                    self.dprint(f'{Fore.RED}Failed - retrying {item}')

                except (requests.exceptions.ProxyError,
                        requests.exceptions.SSLError,
                        requests.exceptions.ConnectionError) as e:
                    self.dprint(str(e))
                    self.dprint(
                        f'{Fore.RED}Failed proxy. Retrying with new proxy.')

                except (requests.exceptions.Timeout, TimeoutError,
                        requests.exceptions.ChunkedEncodingError) as e:
                    self.dprint(str(e))
                    self.dprint(f'{Fore.RED}Proxy timed out. Retrying with new proxy.')

                except requests.exceptions.ConnectionError:
                    self.dprint(
                        f'{Fore.RED}Cannot connect to proxy')

                except requests.exceptions.TooManyRedirects as e:
                    self.dprint(
                        f'{Fore.RED}Too many redirects')
                    self.dprint(str(e))

                except Exception as e:
                    self.dprint(
                        f'{Fore.RED}Unknown error occured')
                    self.dprint(str(e))

                with lock:
                    self.retries += 1

    def start(self, threadCount):
        threads = [Thread(target=self.worker)
                   for i in range(min(threadCount, self.totalitems))]
        threads.append(Thread(target=self.timer))
        [i.start() for i in threads]
        [i.join() for i in threads]        

    
    def dprint(self, x):
        if debugMode:
            print(x)