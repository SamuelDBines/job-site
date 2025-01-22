from django.test import TestCase
from skills.models import Skill
# Create your tests here.


class SkillTestCase(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name="new skill",
            description="A brand new skill"
        )
        # return super().setUp()
      
    def test_create_skill(self):
        """Test that a skill gets created"""
        skill = self.skill
        self.assertEqual(skill.id, 1)
        self.assertEqual(skill.name, "new skill")
        self.assertEqual(skill.description, "A brand new skill")

    def test_get_skill_by_id(self):
        skill = Skill.objects.first()
        self.assertEqual(skill.id, 1)

    def test_skills_length_of_one(self):
        skills = Skill.objects.all()
        self.assertEqual(len(skills), 1)
    
    def test_create_second_skill(self):
      self.skill2 = Skill.objects.create(
          name="new skill 2",
          description="Another skill"
      )
      self.assertEqual(self.skill2.id, 2)

    def test_remove_all_skills(self):
      Skill.objects.filter(id__in=[1, 2]).delete()
      skills = Skill.objects.all()
      self.assertEqual(len(skills), 0)

