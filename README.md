<div id="top"></div>
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




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">GPU Scraper</h3>

  <p align="center">
    A Script to receive news about cheap GPUs through telegram
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project started as a friend of mine asked me to write a script to get him a GPU cheaper than average.
GPU Scraper got written within 2 hours, so not one of the biggest projects.

This scraper makes use of the following telegram group to receive all GPUs:
  * [HWL GPU Verfuegbarkeitshinweise](https://t.me/s/HWL_GPU_Verfuegbarkeitshinweise)


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* bs4
  ```sh
  pip install bs4
  ```
* requests
  ```sh
  pip install requests
  ``` 
  

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/LaurenzJ/gpuScraper.git
   ```
2. Create a `secret.py` file

3. Enter your TOKEN and CHAT_ID (from Telegram) in `secret.py`
   ```js
   TOKEN = '123456789'
   CHAT_ID = '-123456789'
   ```
4. Use the following instructions to get the CHAT_ID from your preferred chat.
['https://sean-bradley.medium.com/get-telegram-chat-id-80b575520659']
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this script to receive cheapest GPUs around Germany. 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Brand Laurent - [@DailyLaurenzJ](https://twitter.com/DailyLaurenzJ) - [laurentbrand.com](https://laurentbrand.com)

Project Link: [https://github.com/LaurenzJ/gpuScraper.git](https://github.com/LaurenzJ/gpuScraper.git)

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
