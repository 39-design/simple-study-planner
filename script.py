"""A short script to demonstrate the study planner project."""

import module

scores = [85, 90, 95]
average_grade = module.calculate_grade(scores)
print("Average grade:", average_grade)


due_date = "2026-06-15"
days = module.days_left(due_date)
print("Days left before due date:", days)


priority = module.task_priority(5, 3)
print("Task priority score:", priority)


plan = module.make_study_plan("final project", 4)
print(plan)

