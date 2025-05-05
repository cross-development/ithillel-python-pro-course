# WebSocket endpoints

import logging

from fastapi import APIRouter

from starlette.websockets import WebSocket

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time communication.

    Args:
        websocket (WebSocket): The WebSocket connection
    """

    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received: {data}")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
