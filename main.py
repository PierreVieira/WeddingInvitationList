import json
from enum import Enum
from typing import List
from collections import defaultdict
from pydantic import BaseModel, Field
from pathlib import Path


class GuestType(str, Enum):
    FAMILY = "FAMILY"
    FRIEND = "FRIEND"


class Person(BaseModel):
    name: str
    is_child: bool = Field(default=False, alias="isChild")
    probably_give_up: bool = Field(default=False, alias="probably_give_up")


class PeopleByLevel(BaseModel):
    level: int = 1
    people: List[Person]


class GuestGroup(BaseModel):
    type: GuestType
    people_by_level: List[PeopleByLevel] = Field(alias="people_by_level")


class GuestList(BaseModel):
    guest_groups: List[GuestGroup]

    @classmethod
    def from_json_file(cls, path: str) -> "GuestList":
        with open(path, 'r', encoding='utf-8') as file:
            raw_data = json.load(file)
        return cls(guest_groups=raw_data)

    def count_summary(self, guests_txt_path: str, output_txt_path: str):
        unique_names = set()
        total_children = 0
        total_probably_give_up = 0
        type_level_counter = defaultdict(lambda: defaultdict(int))

        for group in self.guest_groups:
            for level_group in group.people_by_level:
                for person in level_group.people:
                    name = person.name.strip()
                    if not name or name in unique_names:
                        continue
                    unique_names.add(name)
                    type_level_counter[group.type.value][level_group.level] += 1
                    if person.is_child:
                        total_children += 1
                    if person.probably_give_up:
                        total_probably_give_up += 1

        # Save names to guests.txt
        Path(guests_txt_path).write_text("\n".join(sorted(unique_names)), encoding='utf-8')

        # Build output summary
        lines = [f"Total guests: {len(unique_names)}", f"Total children: {total_children}",
                 f"Total will probably give up: {total_probably_give_up}",
                 f"Total will probably not give up: {len(unique_names) - total_probably_give_up}", "",
                 "Guest breakdown by type and level:"]

        for guest_type, levels in type_level_counter.items():
            for level, count in sorted(levels.items()):
                lines.append(f"- {guest_type} (level {level}): {count}")

        # Print and save to output.txt
        output = "\n".join(lines)
        print(output)
        Path(output_txt_path).write_text(output, encoding='utf-8')


if __name__ == "__main__":
    guest_list = GuestList.from_json_file("files/guests.json")
    guest_list.count_summary(
        guests_txt_path="files/output/guests_output.txt",
        output_txt_path="files/output/output.txt"
    )
