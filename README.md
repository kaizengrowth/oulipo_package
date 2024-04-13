
# Oulipo Variations

Oulipo Variations is a Python library for generating variations of text based on Oulipo text transformer logic. This library provides sophisticated text manipulations, including lemmatization, verb adjustments, and dynamic rhyming functionalities.

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

## Usage

### Main Script
The `main.py` script is the entry point to the package. It supports various operations which can be executed based on the provided command-line arguments.

#### Command-Line Arguments
- `--load [PATH]` - Load data from a specified JSON file and filter verbs.
- `--process [PATH]` - Process text from a specified file.
- `--lemmatize` - Apply lemmatization to the processed text (must be used in conjunction with `--process`).
- `--rhyme` - Replace every seventh word with a rhyme in the processed text (can be used after `--process`).

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

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://opensource.org/licenses/MIT)
