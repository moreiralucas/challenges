"""Battle Service Module"""
from typing import Dict, Optional, Tuple
from datetime import datetime, timedelta
from random import randint
from sqlalchemy import or_
from models import Hero, Threat, Battle


class BattleService(object):
    """Battle service class"""

    def __init__(self, threat: Threat) -> None:
        self.threat: Threat = threat

    def handle(self):
        """Handle battle"""
        now: datetime = datetime.utcnow()

        hero: Optional[Hero] = self._check_available_heroes(now)

        battle_end: datetime = now + timedelta(
            seconds=self._get_battle_time_by_threat(self.threat.danger_level)
        )

        battle: Battle = Battle(
            hero=hero,
            threat=self.threat,
            begin=now,
            end=battle_end,
        )
        battle.save()

        hero.last_battle = battle_end
        hero.save()

    def _check_available_heroes(self, now: datetime) -> Optional[Hero]:
        """Check if exists an hero available to battle with the threat"""

        available_hero: Optional[Hero] = Hero.query.filter(
            or_(Hero.last_battle is None, Hero.last_battle <= now),
            Hero.class_number == self.threat.danger_level_number,
        ).first()

        return available_hero

    def _get_battle_time_by_threat(self, danger_level: str) -> int:
        """Return the time of battle in seconds"""
        duration: Dict[str, Tuple[int, int]] = {
            "God": (300, 600),
            "Dragon": (60, 300),
            "Tiger": (10, 20),
            "Wolf": (1, 2),
        }
        return randint(*duration[danger_level])
