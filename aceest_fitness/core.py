# aceest_fitness/core.py
from datetime import datetime, date
from typing import Dict, List, Any

MET_VALUES = {
    "Warm-up": 3,
    "Workout": 6,
    "Cool-down": 2.5
}

class WorkoutManager:
    def __init__(self, default_weight_kg: float = 70.0):
        # structure: {"Warm-up": [entries], "Workout": [...], "Cool-down": [...]}
        self.workouts: Dict[str, List[Dict[str, Any]]] = {"Warm-up": [], "Workout": [], "Cool-down": []}
        self.daily_workouts: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        self.user_info: Dict[str, Any] = {"weight": default_weight_kg}

    def add_workout(self, category: str, exercise: str, duration_minutes: int) -> Dict[str, Any]:
        if category not in self.workouts:
            raise ValueError("Invalid category")
        if not exercise or not isinstance(exercise, str):
            raise ValueError("Invalid exercise name")
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Duration must be positive integer")

        weight = float(self.user_info.get("weight", 70))
        met = MET_VALUES.get(category, 5)
        # calories formula used in your GUI: (MET * 3.5 * weight / 200) * duration
        calories = (met * 3.5 * weight / 200.0) * duration_minutes
        entry = {
            "exercise": exercise,
            "duration": duration_minutes,
            "calories": calories,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.workouts[category].append(entry)
        today_iso = date.today().isoformat()
        if today_iso not in self.daily_workouts:
            self.daily_workouts[today_iso] = {"Warm-up": [], "Workout": [], "Cool-down": []}
        self.daily_workouts[today_iso][category].append(entry)
        return entry

    def list_all(self) -> Dict[str, List[Dict[str, Any]]]:
        return self.workouts

    def total_minutes(self) -> int:
        return sum(sum(e["duration"] for e in sessions) for sessions in self.workouts.values())

    def save_user_info(self, name: str, regn_id: str, age: int, gender: str, height_cm: float, weight_kg: float) -> Dict[str, Any]:
        if not name:
            raise ValueError("Name required")
        if age <= 0:
            raise ValueError("Invalid age")
        if height_cm <= 0 or weight_kg <= 0:
            raise ValueError("Invalid height/weight")

        bmi = weight_kg / ((height_cm/100) ** 2)
        if gender.upper() == "M":
            bmr = 10*weight_kg + 6.25*height_cm - 5*age + 5
        else:
            bmr = 10*weight_kg + 6.25*height_cm - 5*age - 161

        self.user_info.update({
            "name": name,
            "regn_id": regn_id,
            "age": age,
            "gender": gender.upper(),
            "height": height_cm,
            "weight": weight_kg,
            "bmi": bmi,
            "bmr": bmr
        })
        return self.user_info

    def get_daily_summary(self, date_iso: str):
        return self.daily_workouts.get(date_iso, {"Warm-up": [], "Workout": [], "Cool-down": []})
