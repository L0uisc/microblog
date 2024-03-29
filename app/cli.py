import os
import click


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass


    def extract_text():
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')


    @translate.command()
    def update():
        """Update all languages"""
        extract_text()
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')


    @translate.command()
    def compile():
        """Compile all languages"""
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')


    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language"""
        extract_text()
        if os.system(
                'pybabel init -i messages.pot -d app/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')
