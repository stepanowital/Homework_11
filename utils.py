import json

from typing import List


def load_candidates_from_json() -> List[dict]:
	with open("candidates.json", "r", encoding="utf-8") as file:
		return json.load(file)


def get_candidate(candidate_id: int) -> dict:
	for candidate in load_candidates_from_json():
		if candidate["id"] == candidate_id:
			return candidate


def get_candidates_by_name(candidate_name: str) -> List[dict]:
	result = []
	for candidate in load_candidates_from_json():
		if candidate["name"] == candidate_name:
			result.append(candidate)
	return result


def get_candidates_by_skill(skill_name: str):
	result = []
	for candidate in load_candidates_from_json():
		if skill_name.lower() in candidate["skills"].lower().split(", "):
			result.append(candidate)
	return result
