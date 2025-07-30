from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5]

contents = json.dumps(numbers, indent=4)

path = Path('exercises/chapter_10/numbers.json')
path.write_text(contents)
