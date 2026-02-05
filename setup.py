from setuptools import setup, find_packages

setup(
    name="telegram-keyboard-expert",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["telegram_keyboard"], # Aapki main file ka naam
    install_requires=[
        "requests",
    ],
    author="Airdrop Wala",
    description="A complete Telegram keyboard library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
