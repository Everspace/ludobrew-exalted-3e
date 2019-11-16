
# TODO: Make this a js thing from ludobrew for scaffolding stuff.

import frontmatter
import yaml
import sys
import os
import pathlib

config = None
with open("./make_templates.config.yaml") as f:
    config = yaml.safe_load(f)

charmsPerEssence = config["charmsPerEssence"]
categories = config["categories"]

for attribute, categoryNames in categories.items():
    for category in categoryNames:
        basePath = os.path.join("./", attribute, category)
        os.makedirs(basePath, exist_ok=True)
        for essence, numberOf in enumerate(charmsPerEssence, start=1):
            for count in range(1, numberOf+1):
                fileName = f".e{essence} - charm {count}.md"
                metadata = {
                    "splat": "Second Sunrise",
                    "name": f"{attribute} e{essence} Charm {count}",
                    "essence": essence,
                    "trait": attribute,
                    "tree": category,
                    "rating": essence,
                    "cost": "something",
                    "requires": [],
                }

                post = frontmatter.Post("Hello **world**!\n\n", **metadata)
                post.metadata["content"] = "charm"

                with open(os.path.join(basePath, fileName), "wb") as f:
                    frontmatter.dump(post, f)
                    f.write("\n".encode("utf-8"))
