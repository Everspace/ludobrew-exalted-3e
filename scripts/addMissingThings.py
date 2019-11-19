import os
# frontmatter package, since python-frontmatter doesn't like the content key
import frontmatter
import yaml


defaultMetadata = {
    "splat": "Second Sunrise",
    "name": "Unknown Charm",
    "cost": None,
    "type": "Simple",
    "duration": "Instant",
    "shortDescription": None,
    "essence": 1,
    "rating": 1,
    "trait": "Universal",
    "tree": None,
    "requires": None,
    "tags": []
}


def fullpath(root, f):
    return os.path.realpath(
        os.path.join(root, f)
    )


def walkSimple(dir):
    for root, _, files in os.walk(dir):
        for path in [fullpath(root, f) for f in files]:
            yield path


def postToText(post):
    return "".join([
        "---\n",
        yaml.dump(post['attributes'], default_flow_style=False),
        "---\n",
        "\n",
        post.get('body', "Hello world!\n")
    ])


for path in walkSimple('homebrew/ex3/Splats'):
    post = frontmatter.Frontmatter.read_file(path)
    if not (post.get('attributes', {}).get('content') == "charm"):
        continue

    metadata = {}
    metadata.update(defaultMetadata)
    metadata.update(post.get('attributes', {}))
    toWrite = postToText({
        "attributes": metadata,
        "body": post.get("body")
    })

    # frontmatter.load(path)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(toWrite)
