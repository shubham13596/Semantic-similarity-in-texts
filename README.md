# Semantic Similarity in Texts

## Overview

In distributed work environments, it's common for multiple individuals to work on the same topic or dataset, resulting in the need to collate insights and inputs from various sources. Manually identifying and removing duplicate points from a corpus of sentences can be time-consuming and error-prone. To streamline this process, I developed a program that leverages [Cohere embeddings](https://docs.cohere.com/docs/embeddings) to automatically identify and eliminate duplicate points among a collection of sentences.

This program calculates the **semantic similarity** (similarity in meaning) between sentences and outputs a similarity percentage. A similarity percentage of 100% indicates exact similarity in meaning. By utilizing this similarity metric, the tool helps identify and flag duplicate points, contributing to enhanced productivity and streamlined content aggregation.

## Features

- Automatic identification of duplicate points among a set of sentences.
- Utilizes Cohere embeddings to measure semantic similarity.
- Outputs a similarity percentage to quantify the degree of similarity.
- Enhances productivity by reducing the need for manual duplicate removal.
- Easy integration into your existing workflow.

## Getting Started and Usage

1. Visit the [live demo](https://text-semantic-similarity-09c609803f19.herokuapp.com/).
2. Upload your Excel file containing sentences in a column named 'Text'.
3. Let the program calculate semantic similarity and generate a similarity matrix.
4. Review the similarity percentages to identify and address duplicate points.

## Example

Input Sentences:

1. "The quick brown fox jumps over the lazy dog."
2. "A fast brown fox jumps over a lazy canine."
3. "An agile fox leaps over the inactive dog."

Output Similarity Matrix:

|               | Sentence 1 | Sentence 2 | Sentence 3 |
|---------------|------------|------------|------------|
| Sentence 1    | 100.00     | 82.53      | 78.90      |
| Sentence 2    | 82.53      | 100.00     | 84.22      |
| Sentence 3    | 78.90      | 84.22      | 100.00     |

## Contribution

Contributions are welcome! If you find any issues or have suggestions, feel free to submit a pull request or create an issue.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Disclaimer: This project is for educational purposes and not intended for production use.*

