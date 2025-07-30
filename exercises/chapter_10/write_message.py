from pathlib import Path

path = Path(__file__).parent / "messages.txt"

path.write_text("Hello, this is a message from write_message.py!")