import asyncio
from typing import Coroutine


async def limit_execution_time(
        coro: Coroutine,
        max_execution_time: float) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить,
    # однако иногда она выполняется
    # слишком долго, это время необходимо ограничить переданным
    # на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена,
    # и все они завершились за заданное
    # время.
    #
    # YOUR CODE GOES HERE
    try:
        await asyncio.wait_for(coro, timeout=max_execution_time)
    except asyncio.TimeoutError:
        print('Timeout!')


async def limit_execution_time_many(
        *coros: Coroutine,
        max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time,
    # но корутин на вход приходит несколько.
    #
    # YOUR CODE GOES HERE
    wrapped_coros = [
        asyncio.wait_for(cor, timeout=max_execution_time)
        for cor in coros
    ]

    try:
        await asyncio.wait_for(
            asyncio.gather(*wrapped_coros),
            timeout=max_execution_time
        )
    except asyncio.TimeoutError:
        print('Timeout!')
