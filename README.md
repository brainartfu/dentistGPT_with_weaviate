
# Weaviate DentistGPT

Weaviate DentistGPT is a natural language processing (NLP) project that generates responses to dental questions. This project is built using [Weaviate](https://www.semi.technology/developers/weaviate/current).

## Setup

### Prerequisites

Before getting started with this project, make sure that you have the following software installed on your machine:

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/get-started)
* [Python 3](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/en/download/)

### Install

To get started with the project, follow these steps:

1. Clone the GitHub repository:

    ```
    git clone https://github.com/brainartfu/dentistGPT.git
    ```

2. Navigate into the project folder:

    ```
    cd dentistGPT
    ```

3. Install and start Docker using the following command:

    ```
    docker-compose up
    ```

    Verify that the Docker container is running.

4. Import the dentistry data. Run the following command:

    ```
    cd data
    python3 add_data.py
    ```

5. Install all the required Node modules:

    ```
    npm install
    ```

6. Start the project:

    ```
    node index.js
    ```

7. Navigate to the demo page at [http://localhost:4000/](http://localhost:4000/){:target="_blank"}

## Usage

To use Weaviate DentistGPT, follow these steps:

1. Select a category from the list of available categories.
2. Enter a question in the search box.
3. Click "Search" to generate a response.

## Demo

To see Weaviate DentistGPT in action, watch this demo:

[![Demo of Weaviate DentistGPT](https://img.youtube.com/vi/abc123xyz45/0.jpg)](https://www.youtube.com/watch?v=abc123xyz45)

## Contributions

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a branch for your changes.
3. Make your changes and commit them to your branch.
4. Create a pull request from your branch to the main branch of this repository.

## Credits

Weaviate DentistGPT was created by BrainArt. Find us at:

* Website: https://brainartfu.github.io/
* GitHub: https://github.com/brainartfu

The following open source projects were used in the creation of Weaviate DentistGPT:

* [Weaviate](https://www.semi.technology/developers/weaviate/current)
* [GPT-2](https://openai.com/api/gpt-2/)


Please let me know if you have any other questions or concerns about the README file.

---

