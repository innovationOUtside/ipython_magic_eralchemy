from IPython.core.magic import (
    magics_class, line_magic, line_cell_magic, Magics)
from IPython.core.display import Image, HTML, SVG

from argparse import ArgumentParser
import shlex

from csv import reader
from eralchemy import render_er

@magics_class
class EralchemyMagic(Magics):
    def __init__(self, shell, cache_display_data=False):
        super(EralchemyMagic, self).__init__(shell)
        self.cache_display_data = cache_display_data

    @line_cell_magic
    def erd(self,line, cell=''):
        '''Format.'''
        
        parser = ArgumentParser()
        parser.add_argument('-o', '--output_type', default='svg')
        parser.add_argument('-f', '--filestub', default='erd_from_db')
        parser.add_argument('-c', '--connection_string', default=None)
        parser.add_argument('-i', '--include_tables', default=None)
        parser.add_argument('-x', '--exclude_tables', default=None)
        
        args = parser.parse_args(shlex.split(line))
        
        if args.connection_string is None: return
        fname='{}.{}'.format(args.filestub,args.output_type)
        
        include_tables = [i for i in reader([args.include_tables])][0] if args.include_tables is not None else None
        exclude_tables = [i for i in reader([args.exclude_tables])][0] if args.exclude_tables is not None else None
        retval  = render_er(args.connection_string, fname, 
                            include_tables = include_tables,
                            exclude_tables = exclude_tables) 
        #return SVG(filename=fname)
        #retval is a graphviz object with a _repr_svg_() method
        return retval

def load_ipython_extension(ipython):
    ipython.register_magics(EralchemyMagic)
    
ip = get_ipython()
ip.register_magics(EralchemyMagic)