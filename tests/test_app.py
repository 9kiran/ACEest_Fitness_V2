# tests/test_core.py
import pytest
from aceest_fitness.core import WorkoutManager

@pytest.fixture
def manager():
    m = WorkoutManager(default_weight_kg=70)
    # reset state per test
    return m

def test_add_workout_valid(manager):
    entry = manager.add_workout("Workout", "Running", 30)
    assert entry["exercise"] == "Running"
    assert entry["duration"] == 30
    assert "calories" in entry
    assert manager.total_minutes() == 30

def test_add_workout_invalid_category(manager):
    with pytest.raises(ValueError):
        manager.add_workout("InvalidCat", "Run", 10)

def test_add_workout_invalid_duration(manager):
    with pytest.raises(ValueError):
        manager.add_workout("Workout", "Run", -5)
    with pytest.raises(ValueError):
        manager.add_workout("Workout", "Run", 0)
    with pytest.raises(ValueError):
        manager.add_workout("Workout", "Run", "30")

def test_save_user_info_and_bmi(manager):
    info = manager.save_user_info("Alice", "R100", 30, "F", 165.0, 60.0)
    assert info["name"] == "Alice"
    assert round(info["bmi"], 1) == round(60.0 / ((165.0/100)**2), 1)
    assert "bmr" in info

def test_daily_workouts_populated(manager):
    manager.save_user_info("Bob", "B001", 25, "M", 175.0, 75.0)
    manager.add_workout("Warm-up", "Jumping Jacks", 10)
    today_iso = list(manager.daily_workouts.keys())[0]
    summary = manager.get_daily_summary(today_iso)
    assert "Warm-up" in summary
    assert len(summary["Warm-up"]) == 1
