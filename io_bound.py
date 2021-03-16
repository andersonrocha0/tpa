import asyncio
import concurrent.futures
import sys
import time
from enum import Enum
from multiprocessing import Pool, cpu_count

import aiohttp
import requests


def get_ids_cervejarias():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    if r.status_code == 200:
        return [r['id'] for r in r.json()]


def get_cervejaria(id_c):
    r = requests.get(f'https://api.openbrewerydb.org/breweries/{id_c}')
    if r.status_code == 200:
        print(r.json())


async def get_cervejaria_async(id_c, session):
    async with session.get(f'https://api.openbrewerydb.org/breweries/{id_c}') as response:
        print(await response.json())


async def processar_async(ids):
    coros = []
    async with aiohttp.ClientSession() as session:
        for id_c in ids:
            coros.append(get_cervejaria_async(id_c, session))

        await asyncio.gather(*coros)


async def get_cervejaria_async_manual(id_c):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, get_cervejaria, id_c)


class TipoExecucao(Enum):
    UM_PROCESSO = 1
    VARIOS_PROCESSOS = 2
    VARIAS_THREADS = 3
    ASYNCIO_COM_LIB_HTTP = 4
    ASYNCIO_MANUAL = 5


if __name__ == '__main__':
    started = time.time()

    tipo_execucao = TipoExecucao.ASYNCIO_COM_LIB_HTTP
    cores = cpu_count()

    ids_cervejarias = get_ids_cervejarias()

    if TipoExecucao.UM_PROCESSO == tipo_execucao:
        # Usando somente um processo
        for id_cervejaria in ids_cervejarias:
            get_cervejaria(id_cervejaria)
    elif TipoExecucao.VARIOS_PROCESSOS == tipo_execucao:
        # Usando vários processos
        pool = Pool(cores)
        pool.map(get_cervejaria, ids_cervejarias)
    elif TipoExecucao.VARIAS_THREADS == tipo_execucao:
        # Usando várias threads
        with concurrent.futures.ThreadPoolExecutor(cores) as thp:
            thp.map(get_cervejaria, ids_cervejarias)
    elif TipoExecucao.ASYNCIO_COM_LIB_HTTP == tipo_execucao:
        # Usando asyncio
        event_loop = asyncio.get_event_loop()
        tasks = []

        event_loop.run_until_complete(processar_async(ids_cervejarias))
    elif TipoExecucao.ASYNCIO_MANUAL == tipo_execucao:
        # Usando asyncio manual
        event_loop = asyncio.get_event_loop()
        tasks = []

        for id_cervejaria in ids_cervejarias:
            tasks.append(get_cervejaria_async_manual(id_cervejaria))

        event_loop.run_until_complete(asyncio.wait(tasks))

    elapsed = time.time()
    print('Time taken :', elapsed - started)

    sys.exit(0)
