import logging
from typing import List, Dict, Any
from collections import Counter
from datetime import datetime
import json

class GTDMetaHandler:
    """
    A meta-handler for implementing the Getting Things Done (GTD) methodology
    across multiple projects and cybernetic selves/organizations.
    """

    def __init__(self):
        """
        Initializes the GTDMetaHandler instance.
        """
        self.projects = {}
        self.contexts = {}
        self.next_actions = []
        self.reviews = []
        
        # Set up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        self.logger.info("GTDMetaHandler initialized")

    def add_project(self, project_name: str, tasks: List[Dict[str, Any]]):
        """
        Adds a new project with its associated tasks.

        Parameters:
        - project_name (str): The name of the project.
        - tasks (List[Dict[str, Any]]): A list of tasks associated with the project.
        """
        self.projects[project_name] = tasks
        self.logger.info(f"Added project '{project_name}' with {len(tasks)} tasks.")
        
        # Derive intermediate forms
        self._update_project_statistics()

    def add_context(self, context_name: str, tasks: List[Dict[str, Any]]):
        """
        Adds a new context with its associated tasks.

        Parameters:
        - context_name (str): The name of the context (e.g., @work, @home).
        - tasks (List[Dict[str, Any]]): A list of tasks associated with the context.
        """
        self.contexts[context_name] = tasks
        self.logger.info(f"Added context '{context_name}' with {len(tasks)} tasks.")
        
        # Derive intermediate forms
        self._update_context_statistics()

    def add_next_action(self, task: Dict[str, Any]):
        """
        Adds a task to the next actions list.

        Parameters:
        - task (Dict[str, Any]): A dictionary containing task information.
        """
        self.next_actions.append(task)
        self.logger.info(f"Added task to next actions: {task['title']}")
        
        # Derive intermediate forms
        self._update_next_action_statistics()

    def add_review(self, review_type: str, review_details: Dict[str, Any]):
        """
        Adds a review (weekly or monthly) with its details.

        Parameters:
        - review_type (str): The type of review (weekly or monthly).
        - review_details (Dict[str, Any]): A dictionary containing review details.
        """
        self.reviews.append({"type": review_type, "details": review_details})
        self.logger.info(f"Added {review_type} review.")
        
        # Derive intermediate forms
        self._update_review_statistics()

    def get_project_tasks(self, project_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves tasks for a specific project.

        Parameters:
        - project_name (str): The name of the project.

        Returns:
        - List[Dict[str, Any]]: A list of tasks associated with the project.
        """
        tasks = self.projects.get(project_name, [])
        self.logger.info(f"Retrieved {len(tasks)} tasks for project '{project_name}'")
        return tasks

    def get_context_tasks(self, context_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves tasks for a specific context.

        Parameters:
        - context_name (str): The name of the context.

        Returns:
        - List[Dict[str, Any]]: A list of tasks associated with the context.
        """
        tasks = self.contexts.get(context_name, [])
        self.logger.info(f"Retrieved {len(tasks)} tasks for context '{context_name}'")
        return tasks

    def get_next_actions(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of next actions.

        Returns:
        - List[Dict[str, Any]]: A list of next actions.
        """
        self.logger.info(f"Retrieved {len(self.next_actions)} next actions")
        return self.next_actions

    def get_reviews(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of reviews.

        Returns:
        - List[Dict[str, Any]]: A list of reviews.
        """
        self.logger.info(f"Retrieved {len(self.reviews)} reviews")
        return self.reviews

    def integrate_with_calendar(self, calendar_api):
        """
        Integrates tasks with a calendar application for scheduling.

        Parameters:
        - calendar_api: An instance of a calendar API to interact with.
        """
        scheduled_tasks = 0
        for task in self.next_actions:
            calendar_api.schedule_task(task)
            scheduled_tasks += 1
            self.logger.info(f"Scheduled task '{task['title']}' in calendar.")
        self.logger.info(f"Total tasks scheduled in calendar: {scheduled_tasks}")

    def set_reminders(self, reminder_api):
        """
        Sets reminders for due tasks using a reminder application.

        Parameters:
        - reminder_api: An instance of a reminder API to interact with.
        """
        reminders_set = 0
        for task in self.next_actions:
            if 'due_date' in task:
                reminder_api.set_reminder(task)
                reminders_set += 1
                self.logger.info(f"Set reminder for task '{task['title']}' due on {task['due_date']}.")
        self.logger.info(f"Total reminders set: {reminders_set}")

    def generate_dashboard(self) -> Dict[str, Any]:
        """
        Generates a dashboard overview of tasks and projects.

        Returns:
        - Dict[str, Any]: A dictionary containing the dashboard overview.
        """
        dashboard = {
            "projects": self._get_project_summary(),
            "contexts": self._get_context_summary(),
            "next_actions": self._get_next_action_summary(),
            "reviews": self._get_review_summary()
        }
        self.logger.info("Generated dashboard overview.")
        return dashboard

    def _update_project_statistics(self):
        """
        Updates project statistics for visualization and analysis.
        """
        self.project_stats = {
            "total_projects": len(self.projects),
            "total_tasks": sum(len(tasks) for tasks in self.projects.values()),
            "avg_tasks_per_project": sum(len(tasks) for tasks in self.projects.values()) / len(self.projects) if self.projects else 0,
            "project_sizes": {name: len(tasks) for name, tasks in self.projects.items()}
        }
        self.logger.info(f"Updated project statistics. Total projects: {self.project_stats['total_projects']}")

    def _update_context_statistics(self):
        """
        Updates context statistics for visualization and analysis.
        """
        self.context_stats = {
            "total_contexts": len(self.contexts),
            "total_tasks": sum(len(tasks) for tasks in self.contexts.values()),
            "avg_tasks_per_context": sum(len(tasks) for tasks in self.contexts.values()) / len(self.contexts) if self.contexts else 0,
            "context_sizes": {name: len(tasks) for name, tasks in self.contexts.items()}
        }
        self.logger.info(f"Updated context statistics. Total contexts: {self.context_stats['total_contexts']}")

    def _update_next_action_statistics(self):
        """
        Updates next action statistics for visualization and analysis.
        """
        self.next_action_stats = {
            "total_next_actions": len(self.next_actions),
            "priority_distribution": Counter(task.get('priority', 'None') for task in self.next_actions),
            "due_date_distribution": Counter(task.get('due_date', 'None') for task in self.next_actions)
        }
        self.logger.info(f"Updated next action statistics. Total next actions: {self.next_action_stats['total_next_actions']}")

    def _update_review_statistics(self):
        """
        Updates review statistics for visualization and analysis.
        """
        self.review_stats = {
            "total_reviews": len(self.reviews),
            "review_type_distribution": Counter(review['type'] for review in self.reviews),
            "review_dates": [review['details'].get('date', 'None') for review in self.reviews]
        }
        self.logger.info(f"Updated review statistics. Total reviews: {self.review_stats['total_reviews']}")

    def _get_project_summary(self) -> Dict[str, Any]:
        """
        Generates a summary of projects for the dashboard.

        Returns:
        - Dict[str, Any]: A dictionary containing the project summary.
        """
        summary = {
            "total_projects": self.project_stats["total_projects"],
            "total_tasks": self.project_stats["total_tasks"],
            "avg_tasks_per_project": self.project_stats["avg_tasks_per_project"],
            "project_sizes": self.project_stats["project_sizes"]
        }
        self.logger.info("Generated project summary for dashboard.")
        return summary

    def _get_context_summary(self) -> Dict[str, Any]:
        """
        Generates a summary of contexts for the dashboard.

        Returns:
        - Dict[str, Any]: A dictionary containing the context summary.
        """
        summary = {
            "total_contexts": self.context_stats["total_contexts"],
            "total_tasks": self.context_stats["total_tasks"],
            "avg_tasks_per_context": self.context_stats["avg_tasks_per_context"],
            "context_sizes": self.context_stats["context_sizes"]
        }
        self.logger.info("Generated context summary for dashboard.")
        return summary

    def _get_next_action_summary(self) -> Dict[str, Any]:
        """
        Generates a summary of next actions for the dashboard.

        Returns:
        - Dict[str, Any]: A dictionary containing the next action summary.
        """
        summary = {
            "total_next_actions": self.next_action_stats["total_next_actions"],
            "priority_distribution": self.next_action_stats["priority_distribution"],
            "due_date_distribution": self.next_action_stats["due_date_distribution"]
        }
        self.logger.info("Generated next action summary for dashboard.")
        return summary

    def _get_review_summary(self) -> Dict[str, Any]:
        """
        Generates a summary of reviews for the dashboard.

        Returns:
        - Dict[str, Any]: A dictionary containing the review summary.
        """
        summary = {
            "total_reviews": self.review_stats["total_reviews"],
            "review_type_distribution": self.review_stats["review_type_distribution"],
            "review_dates": self.review_stats["review_dates"]
        }
        self.logger.info("Generated review summary for dashboard.")
        return summary