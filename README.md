
# Oulipo Variations

Oulipo Variations is a Python library for generating variations of text based on Oulipo text transformer logic. This library provides sophisticated text manipulations, including lemmatization, verb adjustments, and dynamic rhyming functionalities.

To use the minimal web GUI, go to: [http://poetryplux.xyz](http://poetryplux.xyz)

## Installation

### From GitHub

To install the latest version directly from GitHub:
```bash
pip install git+https://github.com/kaizengrowth/oulipo_package.git
```

### From Source

Clone this repository to your local machine using:
```bash
git clone https://github.com/kaizengrowth/oulipo_package.git
```

Navigate to the cloned directory:
```bash
cd oulipo_package
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Make sure to have installed this version of the spaCy NLP model (already installed if using Docker package):
```bash
python -m spacy download en_core_web_sm
```

### Using Docker
To use the Docker container for Oulipo Variations, first ensure you are logged into GitHub Packages:

```bash
echo "YOUR_GITHUB_TOKEN" | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```

You can access this package along with instructions here: https://github.com/kaizengrowth/oulipo_package/pkgs/container/oulipo_package%2Foulipo


## Usage

### Main Script
The `main.py` script is the entry point to the package. It supports various operations which can be executed based on the provided command-line arguments.

#### Command-Line Arguments
- `--load [PATH]` - Load data from a specified JSON file and filter verbs.
- `--process [PATH]` - Process text from a specified file.
- `--lemmatize` - Apply lemmatization to the processed text (must be used in conjunction with `--process`).
- `--rhyme` - Replace every seventh word with a rhyme in the processed text (can be used after `--process`).
-- '--generate_music' - Generate a music sequence from the text (must be used in conjunction with --process).
-- '--scramble_stanzas' - Scramble the text to create random variations (must be used in conjunction with --process).

### Examples

Load and process data:
```bash
python main.py --load path/to/your/data.json
```

Process text with lemmatization:
```bash
python main.py --process path/to/your/text.txt --lemmatize
```

Replace every seventh word with a rhyme:
```bash
python main.py --process path/to/your/text.txt --rhyme
```

Generate music from poem:
```bash
python main.py --process path/to/your/text.txt --generate_music
```

Scramble stanzas:
```bash
python main.py --process path/to/your/text.txt --scramble_text
```



## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://opensource.org/licenses/MIT)
