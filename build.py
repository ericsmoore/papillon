import hashlib
import os
import re
import shutil
import subprocess
from pathlib import Path

src = Path('src')
scenes = Path('src/scenes')
md_output = Path('out/md_hashed')
site_output = Path('out/site')
md_output.mkdir(parents=True, exist_ok=True)
site_output.mkdir(parents=True, exist_ok=True)

scene_map = {}


for s in scenes.rglob('*.md'):
    basename = os.path.basename(s)
    hash = hashlib.sha256(basename.encode('utf-8')).hexdigest()[:6]
    if basename == 'index.md':
        scene_map[basename] = basename
    else:
        scene_map[basename] = hash

assert len(scene_map) == len(set(scene_map.values())), 'no way'

link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]*?)([^/)]+)\.md\)')

for s in scenes.rglob('*.md'):
    content = s.read_text(encoding='utf-8')

    def replace_link(m):
        link_text, name = m.group(1), m.group(3)
        basename = f'{name}.md'
        if basename in scene_map:
            return f'[{link_text}](/{scene_map[basename]}/)'
        return m.group(0)

    new_content = link_pattern.sub(replace_link, content)

    basename = os.path.basename(s)
    out_path = md_output / scene_map[basename]
    out_path = out_path.with_suffix('.md')
    out_path.write_text(new_content, encoding='utf-8')

for md_file in md_output.glob('*.md'):
    md_name = md_file.relative_to(md_output).with_suffix('')

    if md_name.name == 'index':
        output_file = site_output / md_name.with_suffix('.html')
    else:
        output_file = site_output / md_name / 'index.html'

    output_file.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            'pandoc',
            str(md_file),
            '-s',
            '-o',
            str(output_file),
            '--from=markdown+markdown_attribute',
            '--template=src/template.html',
        ],
        check=True,
    )

shutil.copy2(src / 'style.css', site_output / 'style.css')
shutil.copytree(src / 'fonts', site_output / 'fonts', dirs_exist_ok=True)
