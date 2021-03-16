import asyncio
import concurrent.futures
import sys
import time
from enum import Enum
from multiprocessing import Pool, cpu_count


def contar_ate_100_000_000(x):
    print(f"Inicio da execucao de num {x}")
    i = 1
    while i < 100_000_000:
        i = i + 1

    print(f"Fim da execucao de num {x}")


async def contar_ate_100_000_000_async(x):
    return contar_ate_100_000_000(x)


class TipoExecucao(Enum):
    UM_PROCESSO = 1
    VARIOS_PROCESSOS = 2
    VARIAS_THREADS = 3
    ASYNCIO = 4


if __name__ == '__main__':
    started = time.time()

    tipo_execucao = TipoExecucao.VARIOS_PROCESSOS
    cores = cpu_count()

    if TipoExecucao.UM_PROCESSO == tipo_execucao:
        # Usando somente um processo
        for i in range(cores):
            contar_ate_100_000_000(i)
    elif TipoExecucao.VARIOS_PROCESSOS == tipo_execucao:
        # Usando vários processos
        pool = Pool(cores)
        pool.map(contar_ate_100_000_000, range(cores))
    elif TipoExecucao.VARIAS_THREADS == tipo_execucao:
        # Usando várias threads
        with concurrent.futures.ThreadPoolExecutor(cores) as thp:
            thp.map(contar_ate_100_000_000, range(cores))
    elif TipoExecucao.ASYNCIO == tipo_execucao:
        # Usando asyncio
        event_loop = asyncio.get_event_loop()
        tasks = []
        for i in range(cores):
            tasks.append(contar_ate_100_000_000_async(i))

        event_loop.run_until_complete(asyncio.wait(tasks))

    elapsed = time.time()
    print('Time taken :', elapsed - started)

    sys.exit(0)
