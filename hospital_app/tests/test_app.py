import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from app import health_message

def test_health_message():
    result = health_message()
    assert result["status"] == "UP"
