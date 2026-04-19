from pathlib import Path
import importlib

scenes = {}
for f in Path(__file__).parent.glob('*.py'):
    if f.stem != '__init__':
        mod = importlib.import_module(f'scenes.{f.stem}')
        scenes[f.stem] = mod.scene
