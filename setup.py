from setuptools import setup

setup(
    name="Glide-Text-2-Image",
    packages=[
        "Glide_Text_2_Image",
        "Glide_Text_2_Image.clip",
        "Glide_Text_2_Image.tokenizer",
    ],
    package_data={
        "Glide_Text_2_Image.tokenizer": [
            "bpe_simple_vocab_16e6.txt.gz",
            "encoder.json.gz",
            "vocab.bpe.gz",
        ],
        "Glide_Text_2_Image.clip": ["config.yaml"],
    },
    install_requires=[
        "Pillow",
        "attrs",
        "torch",
        "filelock",
        "requests",
        "tqdm",
        "ftfy",
        "regex",
        "numpy",
    ],
    author="OpenAI",
)
