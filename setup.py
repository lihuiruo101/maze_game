from setuptools import setup, find_packages

setup(
    name='maze_game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'maze-game=maze_game.maze:start_game',
        ],
    },
    author='Your Name',
    author_email='your@email.com',
    description='A terminal maze game using curses',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lihuiruo10/maze_game',
)
