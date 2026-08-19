<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FeriCodes/coin-watcher">
    <img src="images/icon.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Coin Watcher</h3>

  <p align="center">
    A short program to get my coins' prices.
    <br />
    <a href="https://github.com/FeriCodes/coin-watcher"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://coinwatcher-bgwk.onrender.com/">View Demo</a>
    &middot;
    <a href="https://github.com/FeriCodes/coin-watcher/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/FeriCodes/coin-watcher/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://coinwatcher-bgwk.onrender.com/)

Coin Watcher is a simple Python web app that tracks live cryptocurrency prices. It's built with FastAPI on the backend and Jinja2 templates on the frontend, showing a clean, dark-themed table of coin prices with a "last updated" timestamp.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-badge]][Python-url]
* [![FastAPI][FastAPI-badge]][FastAPI-url]
* [![Uvicorn][Uvicorn-badge]][Uvicorn-url]
* [![Jinja][Jinja-badge]][Jinja-url]
* [![SQLite][SQLite-badge]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.10+
* pip

### Installation

1. Get a free API Key at [CoinGecko](https://www.coingecko.com/en/api)
2. Clone the repo
```sh
git clone https://github.com/FeriCodes/coin-watcher.git
cd coin-watcher
```
3. Create a virtual environment
```sh
python -m venv venv
```
4. Install Python packages
```sh
pip install -r requirements.txt
```
5. Create a `.env` file in the root directory and add your CoinGecko API key:
```sh
COINGECKO_API_KEY=your_api_key_here
```
6. Initialize the SQLite database with your initial tokens:
```sh
   python scripts/db_setup.py
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the app locally with:
```sh
uvicorn main:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the live price table. A `/health` route is also available for uptime checks.

_For more examples, please refer to the [Documentation](https://github.com/FeriCodes/coin-watcher)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Auto-refresh prices without a page reload
- [ ] Add 24h price change %
- [ ] Add a search/filter box for coins
    - [ ] Sort by price or name

See the [open issues](https://github.com/FeriCodes/coin-watcher/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion to improve this project, please fork the repo and create a pull request. You can also open an issue with the tag "enhancement". 
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/FeriCodes/coin-watcher/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=FeriCodes/coin-watcher" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

FeriCodes - [GitHub Profile](https://github.com/FeriCodes)
Hossein Bigdeli  - [Email](mailto:hosseinbigdeli335@gmail.com)

Project Link: [https://github.com/FeriCodes/coin-watcher](https://github.com/FeriCodes/coin-watcher)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Shields.io](https://shields.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FeriCodes/coin-watcher.svg?style=for-the-badge
[contributors-url]: https://github.com/FeriCodes/coin-watcher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/FeriCodes/coin-watcher.svg?style=for-the-badge
[forks-url]: https://github.com/FeriCodes/coin-watcher/network/members
[stars-shield]: https://img.shields.io/github/stars/FeriCodes/coin-watcher.svg?style=for-the-badge
[stars-url]: https://github.com/FeriCodes/coin-watcher/stargazers
[issues-shield]: https://img.shields.io/github/issues/FeriCodes/coin-watcher.svg?style=for-the-badge
[issues-url]: https://github.com/FeriCodes/coin-watcher/issues
[license-shield]: https://img.shields.io/github/license/FeriCodes/coin-watcher.svg?style=for-the-badge
[license-url]: https://github.com/FeriCodes/coin-watcher/blob/main/LICENSE
[product-screenshot]: images/coin_watcher.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python-badge]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[FastAPI-badge]: https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[Uvicorn-badge]: https://img.shields.io/badge/uvicorn-2A2A2A?style=for-the-badge&logo=gunicorn&logoColor=white
[Uvicorn-url]: https://www.uvicorn.org/
[Jinja-badge]: https://img.shields.io/badge/jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white
[Jinja-url]: https://jinja.palletsprojects.com

[SQLite-badge]: [https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white](https://img.shields.io/badge/sqlite-%2307405e.svg?
[SQLite-badge]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/index.html