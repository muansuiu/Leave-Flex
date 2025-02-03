from django.core.management.base import BaseCommand

from leaveTracker.models import Team


class Command(BaseCommand):

    def handle(self, *args, **options):
        team_names = ['HR', 'Admin', 'Executives', 'Design', 
                      'Frontend', 'Backend', 'DevOps','ML/AI', 'QA']
        self.create_team(teams=team_names)

    def create_team(self, teams: list):
        # checks if the teams are already exists in the db, if not then proceeds to create new teams
        
        existing_teams = Team.objects.filter(team_name__in=teams).values_list('team_name', flat=True)
        new_teams = [Team(team_name=new_team) for new_team in teams if new_team not in existing_teams]

        if new_teams:
            Team.objects.bulk_create(new_teams)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {len(new_teams)} teams'))
        else:
            self.stdout.write(self.style.WARNING('No new teams were added, all teams already exist.'))
