"""WebSocket notifications for students joining meetings."""

from fastapi import WebSocket, APIRouter, WebSocketDisconnect

active_connections = {}

router = APIRouter()


async def send_personal_message(message: str, websocket: WebSocket):
    """Helper function to send a message to a single WebSocket."""

    await websocket.send_text(message)


async def broadcast_message(meeting_id: int, message: str):
    """Broadcast message to all WebSocket connections in the meeting."""

    if meeting_id in active_connections:
        for connection in active_connections[meeting_id]:
            await send_personal_message(message, connection)


@router.websocket("/ws/meeting/{meeting_id}")
async def notify(websocket: WebSocket, meeting_id: int):
    """Handle WebSocket connection for students joining meetings."""

    await websocket.accept()

    if meeting_id not in active_connections:
        active_connections[meeting_id] = []

    active_connections[meeting_id].append(websocket)

    try:
        await broadcast_message(meeting_id, f"A new student has joined meeting {meeting_id}!")

        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"You sent: {data}")

    except WebSocketDisconnect:
        active_connections[meeting_id].remove(websocket)
        await broadcast_message(meeting_id, f"A student has left meeting {meeting_id}.")
