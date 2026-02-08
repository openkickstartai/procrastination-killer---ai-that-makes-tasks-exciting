"""
Quest Engine - Transforms boring tasks into exciting quests
"""

import uuid
import datetime
from typing import Dict, List, Optional
import random


class Quest:
    def __init__(self, quest_id: str, title: str, description: str, 
                 story: str, difficulty: str, estimated_time: int,
                 rewards: List[str], motivation_score: float):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.story = story
        self.difficulty = difficulty
        self.estimated_time = estimated_time
        self.rewards = rewards
        self.motivation_score = motivation_score
        self.created_at = datetime.datetime.now()
        self.completed = False

class QuestEngine:
    def __init__(self):
        self.quest_templates = self._load_quest_templates()
        
    def _load_quest_templates(self) -> Dict[str, Dict]:
        """Load quest templates based on different themes"""
        return {
            "gaming": {
                "prefixes": ["Epic", "Legendary", "Mythic"],
                "monsters": ["Procrastination Dragon", "Distraction Demon", "Boredom Beast"],
                "rewards": ["XP", "Achievement Points", "Loot Drops"],
                "verbs": ["Defeat", "Conquer", "Vanquish", "Overcome"]
            },
            "fantasy": {
                "prefixes": ["Noble", "Heroic", "Courageous"],
                "monsters": ["Laziness Troll", "Delay Golem", "Excuse Spirit"],
                "rewards": ["Gold Coins", "Magic Items", "Experience"],
                "verbs": ["Slay", "Banish", "Cleanse", "Restore"]
            },
            "sci_fi": {
                "prefixes": ["Quantum", "Cyber", "Neural"],
                "monsters": ["Time Waster", "Focus Virus", "Motivation Glitch"],
                "rewards": ["Data Credits", "Tech Points", "Upgrade Modules"],
                "verbs": ["Debug", "Optimize", "Delete", "Upgrade"]
            },
            "productivity": {
                "prefixes": ["Strategic", "Efficient", "Focused"],
                "monsters": ["Chaos Monster", "Mess Dragon", "Clutter Beast"],
                "rewards": ["Productivity Points", "Clarity Gems", "Order Tokens"],
                "verbs": ["Organize", "Streamline", "Conquer", "Master"]
            }
        }
    
    async def analyze_task(self, task: str) -> Dict:
        """Analyze a task to understand its nature"""
        # Simple keyword analysis for task categorization
        categories = {
            "cleaning": ["clean", "wash", "organize", "tidy", "declutter"],
            "work": ["work", "job", "project", "task", "assignment"],
            "study": ["study", "learn", "read", "research", "practice"],
            "exercise": ["exercise", "workout", "run", "gym", "fitness"],
            "social": ["call", "email", "message", "connect", "meet"],
            "chores": ["laundry", "dishes", "grocery", "shopping", "cook"],
            "creative": ["write", "draw", "create", "design", "make"]
        }
        
        task_lower = task.lower()
        detected_category = "general"
        
        for category, keywords in categories.items():
            if any(keyword in task_lower for keyword in keywords):
                detected_category = category
                break
                
        return {
            "category": detected_category,
            "complexity": self._assess_complexity(task),
            "estimated_difficulty": self._estimate_difficulty(task)
        }
    
    def _assess_complexity(self, task: str) -> str:
        """Assess task complexity"""
        word_count = len(task.split())
        if word_count <= 3:
            return "simple"
        elif word_count <= 6:
            return "moderate"
        else:
            return "complex"
    
    def _estimate_difficulty(self, task: str) -> int:
        """Estimate task difficulty on scale 1-10"""
        difficulty_keywords = {
            "easy": ["quick", "simple", "basic", "easy"],
            "medium": ["moderate", "normal", "standard"],
            "hard": ["hard", "difficult", "complex", "challenge"]
        }
        
        task_lower = task.lower()
        base_difficulty = 5  # Default medium
        
        for difficulty, keywords in difficulty_keywords.items():
            if any(keyword in Task_lower for keyword in keywords):
                if difficulty == "easy":
                    base_difficulty = 3
                elif difficulty == "medium":
                    base_difficulty = 5
                elif difficulty == "hard":
                    base_difficulty = 8
                break
                
        return base_difficulty
    
    async def generate_quest(self, task: str, analysis: Dict, 
                        motivation_profile: Dict, priority: str = "medium") -> Quest:
        """Generate a personalized quest from a boring task"""
        
        # Select quest theme based on user profile
        theme = motivation_profile.get("preferred_theme", "gaming")
        template = self.quest_templates.get(theme, self.quest_templates["gaming"])
        
        # Generate quest components
        quest_id = str(uuid.uuid4())
        
        # Select prefix and monster
        prefix = random.choice(template["prefixes"])
        monster = random.choice(template["monsters"])
        verb = random.choice(template["verbs"])
        reward_type = random.choice(template["rewards"])
        
        # Create quest title
        title = f"{prefix} Quest: {verb} the {monster} of {task.title()}"
        
        # Generate story
        story = self._generate_story(task, prefix, monster, verb, theme)
        
        # Calculate rewards based on difficulty and motivation score
        motivation_score = self._calculate_motivation_score(analysis, motivation_profile)
        rewards = self._generate_rewards(analysis, reward_type, motivation_score)
        
        # Set difficulty based on task complexity and priority
        difficulty = self._determine_difficulty(analysis, priority)
        estimated_time = self._estimate_time(analysis, difficulty)
        
        # Create description
        description = f"Transform the boring task {task} into an exciting adventure!"
        
        return Quest(
            quest_id=quest_id,
            title=title,
            description=description,
            story=story,
            difficulty=difficulty,
            estimated_time=estimated_time,
            rewards=rewards,
            motivation_score=motivation_score
        )
    
    def _generate_story(self, task: str, prefix: str, monster: str, 
                      verb: str, theme: str) -> str:
        """Generate a quest story based on theme"""
        
        if theme == "gaming":
            return f"""
🎮 QUEST STARTED 🎮

You stand at the entrance of the {prefix.lower()} Quest Chamber. 
Before you lies the dreaded {monster}, guard of unfinished tasks. 
This beast feeds on procrastination and grows stronger with each passing moment.

🗺️ Your Mission: {verb} the {monster}
📋 Task at stake: {task}

The chamber echoes with ancient power. You feel the energy of countless adventurers who came before you.
Will you succeed where others have procrastinated?

🎯 GLORY AWAITS THE BRAVE! 
"""
        elif theme == "fantasy":
            return f"""
🏰 FANTASY QUEST BEGINS 🏰

In the mystical realm of Productivity, the {prefix.lower()} {monster} has awakened. 
This ancient evil spreads the curse of "I will do it later" throughout the land.

⚔️ Your Noble Quest: {verb} the {monster}
📜 Ancient Task: {task}

The wise wizards of Motivation Tower have chosen you for this quest. 
Armed with the Sword of Focus and Shield of Discipline, you venture forth.

✨ Will you break the curse and restore productivity to the kingdom?

🏆 LEGEND AND GLORY AWAIT! 
"""
        else:
            return f"""
🚀 MISSION BRIEFING 🚀

OPERATION: {prefix.upper()} QUEST
TARGET: {monster}
OBJECTIVE: {verb}
PRIMARY TASK: {task}

The {monster} is causing system-wide productivity failure. 
Conventional methods have failed. Time for extraordinary measures.

🎯 EXECUTE WITH PRECISION
🎁 REWARD: Glory and Satisfaction

MISSION STATUS: ACTIVE
"""
    
    def _calculate_motivation_score(self, analysis: Dict, profile: Dict) -> float:
        """Calculate how motivating this quest will be"""
        base_score = 5.0
        
        # Boost for user preferences
        if profile.get("loves_stories", False):
            base_score += 2.0
        if profile.get("competitive", False):
            base_score += 1.5
        if profile.get("social_motivated", False):
            base_score += 1.0
            
        # Adjust for task characteristics
        if analysis["complexity"] == "simple":
            base_score += 1.0
        elif analysis["complexity"] == "complex":
            base_score -= 1.0
            
        return min(base_score, 10.0)
    
    def _generate_rewards(self, analysis: Dict, reward_type: str, 
                      motivation_score: float) -> List[str]:
        """Generate quest rewards"""
        base_rewards = [f"10 {reward_type}", "1 Achievement", "100 XP"]
        
        if motivation_score > 7.0:
            base_rewards.extend(["Rare Item Drop", "Streak Bonus"])
            
        if analysis["estimated_difficulty"] > 7:
            base_rewards.extend(["Boss Loot", "Title Upgrade"])
            
        return base_rewards
    
    def _determine_difficulty(self, analysis: Dict, priority: str) -> str:
        """Determine quest difficulty"""
        task_difficulty = analysis.get("estimated_difficulty", 5)
        
        priority_multiplier = {
            "low": 0.8,
            "medium": 1.0,
            "high": 1.3,
            "urgent": 1.5
        }
        
        adjusted_difficulty = task_difficulty * priority_multiplier.get(priority, 1.0)
        
        if adjusted_difficulty <= 3:
            return "Tutorial"
        elif adjusted_difficulty <= 5:
            return "Normal"
        elif adjusted_difficulty <= 7:
            return "Hard"
        else:
            return "Legendary"
    
    def _estimate_time(self, analysis: Dict, difficulty: str) -> int:
        """Estimate time to complete quest"""
        base_time = analysis.get("estimated_difficulty", 5) * 10  # 10 minutes per difficulty point
        
        difficulty_multiplier = {
            "Tutorial": 0.8,
            "Normal": 1.0,
            "Hard": 1.3,
            "Legendary": 1.6
        }
        
        return int(base_time * difficulty_multiplier.get(difficulty, 1.0))
    
    async def get_quest(self, quest_id: str) -> Optional[Quest]:
        """Get quest by ID (placeholder for demo)"""
        # In real implementation, this would query the database
        return None
    
    async def suggest_next_quest(self) -> str:
        """Suggest the next quest based on patterns"""
        suggestions = [
            "Quick 5-minute meditation quest",
            "Organize one small area quest",
            "Answer one pending email quest",
            "Water break mini-quest"
            "Stretch and movement quest"
        ]
        
        return random.choice(suggestions)