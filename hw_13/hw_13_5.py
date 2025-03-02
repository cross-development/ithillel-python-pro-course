"""
Asynchronous Web Server with Aiohttp.
This script sets up a simple web server with two endpoints:
- `/`        -> Returns "Hello, World!"
- `/slow`    -> Simulates a slow operation with a 5-second delay.
"""

import asyncio
from aiohttp import web


async def handle_hello(request: web.Request) -> web.Response:
    """
    Handles requests to the root endpoint.

    Args:
        request (web.Request): Incoming HTTP request.

    Returns:
        web.Response: A response containing "Hello, World!".
    """

    return web.Response(text="Hello, World!")


async def handle_slow(request: web.Request) -> web.Response:
    """
    Handles requests to the /slow endpoint, simulating a slow operation.

    Args:
        request (web.Request): Incoming HTTP request.

    Returns:
        web.Response: A response after a 5-second delay.
    """

    await asyncio.sleep(5)

    return web.Response(text="Operation completed!")


def register_routes(app: web.Application) -> None:
    """
    Registers all routes for the web application.

    Args:
        app (web.Application): The aiohttp web application instance.

    Returns:
        None
    """

    app.router.add_get('/', handle_hello)
    app.router.add_get('/slow', handle_slow)


def create_app() -> web.Application:
    """
    Creates and configures the web application.

    Returns:
        web.Application: The configured aiohttp web application.
    """

    app = web.Application()
    register_routes(app)

    return app


if __name__ == '__main__':
    web.run_app(create_app())
