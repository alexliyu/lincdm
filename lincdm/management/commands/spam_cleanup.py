"""Spam cleanup command module for blog"""
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import NoArgsCommand

from lincdm.entry.models import Entry


class Command(NoArgsCommand):
    """Command object for removing comments
    flagged as spam"""
    help = "Remove entry's comments flagged as spam."

    def handle_noargs(self, **options):
        verbosity = int(options.get('verbosity', 1))

        content_type = ContentType.objects.get_for_model(Entry)
        spams = Comment.objects.filter(is_public=False,
                                       content_type=content_type,
                                       flags__flag='spam')
        spams_count = spams.count()
        spams.delete()

        if verbosity:
            print '%i spam comments deleted.' % spams_count
