from django.core.management.base import BaseCommand
from vocabulary.load_skos import SKOSLoader
from optparse import make_option


class Command(BaseCommand):
    help = 'Import SKOS files'
    args = '<SKOS files>'
    option_list = BaseCommand.option_list + (
        make_option('-r', dest='recursive', action='store_true',
            help='Import all vocabularies recursively.'),
        )
    
    def handle(self, *args, **options):   
        if not args:
            parser.error("You must specify some SKOS files to import.")
        try:
            loader = SKOSLoader(request=False, log=True)
            if options.get('recursive', False):
                for a in args:
                    loader.load_recursive(a)
            else:
                for a in args:
                    loader.load_skos_vocab(a)
            loader.save_relationships()
        except:
            import traceback, sys
            traceback.print_exc()
    
            print >>sys.stderr, '''
                Exceptions have been raised.
                If the import was incomplete, you might want to reset the DB:
                $ python manage.py reset vocabulary'''
