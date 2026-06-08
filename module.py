"""This module contains helper functions for tracking course grades, determining assignment priorities, and generating simple study plans."""

from datetime import datetime, date


def calculate_grade(scores):
    """Calculate the average grade.

    Parameters
    ----------
    scores : list
        A list of grade scores.

    Returns
    -------
    float
        The average score.
    """
    # Add all scores and divide by the number of scores.
    total = sum(scores)
    average = total / len(scores)
    return round(average, 2)


def days_left(due_date):
    """Calculate how many days are left.

    Parameters
    ----------
    due_date : str
        The due date in YYYY-MM-DD format.

    Returns
    -------
    int
        Number of days left before the due date.
    """
    # Get today's date and convert the due date string into a date object.
    today = date.today()
    due = datetime.strptime(due_date, "%Y-%m-%d").date()
    return (due - today).days


def task_priority(importance, days):
    """Calculate a simple priority score.

    Parameters
    ----------
    importance : int
        Task importance from 1 to 5.
    days : int
        Number of days left.

    Returns
    -------
    int
        Priority score.
    """
    # Higher importance and fewer days left give a higher priority score.
    score = importance * 10 - days
    return score


def make_study_plan(task_name, hours):
    """Make a simple study plan sentence.

    Parameters
    ----------
    task_name : str
        Name of the task.
    hours : int or float
        Estimated study hours.

    Returns
    -------
    str
        A simple study plan sentence.
    """
    # Return a simple sentence that tells the student what to study.
    return "Study " + task_name + " for about " + str(hours) + " hour(s)."
