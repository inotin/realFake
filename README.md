<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
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
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/inotin/realFake">
    <img src="images/logo.png" alt="Logo" height="80">
  </a>

  <p align="center">
    Choose the next best post
    <br />
    <br />
    <a href="https://github.com/inotin/realFake">View Demo</a>
    ·
    <a href="https://github.com/inotin/realFake/issues">Report Bug</a>
    ·
    <a href="https://github.com/inotin/realFake/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com). -->


The primary goal of this project is to build a logistic regression model based on features generated from textual information capable of prediction whether given article (piece of text) represents fake or real news. In order to reduce amount of used features, i.e. reduce dimensionality of the model, principal component analysis (PCA) was applied. The obtained results demonstrate that using PCA helps to reduce number of used features by 99,4% without signiﬁcant decrease of the model accuracy.

### Data

Fake and real news dataset from [kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset).

Initially there were two separate ﬁles with real and fake news. I merged them with adding the target variable column **tr**.

##### Features:
**title**   - The title of the article  
**text**    - The text of the article  
**subject** - The subject of the article  
**date**    - The date at which the article was posted

##### Target variable
**tr**      - fake, if 0; real, if 1

The final data frame which I used for model fitting contains 500 variables representing one hot encoded words and ngrams (as a result of vectorization) from article texts for each article. The last column of this data frame (tr) has values 0, when article is fake and 1 when it is real. The data frame consists of 44898 records and was subsequently split into train and test dataset with proportions of 70/30 using randomized choice.


### To Do List
- [x] Initial commit
- [ ] Dockerize (create docker image)
- [ ] Define and remove outliers
- [ ] Apply Regularization
- [ ] Introduce additional available data and generate new features (e.g., text lengths)
- [ ] Apply MCA (Multiple Correspondence Analysis) / CATPCA



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/inotin/realFake/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Ilia Notin - ilia@notin.it

Project Link: [https://github.com/inotin/realFake](https://github.com/inotin/realFake)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Template for README.md](https://github.com/othneildrew/Best-README-Template/graphs/contributors)








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/inotin/realFake.svg?style=flat-square
[contributors-url]: https://github.com/inotin/realFake/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/inotin/realFake.svg?style=flat-square
[forks-url]: https://github.com/inotin/realFake/network/members
[stars-shield]: https://img.shields.io/github/stars/inotin/realFake.svg?style=flat-square
[stars-url]: https://github.com/inotin/realFake/stargazers
[issues-shield]: https://img.shields.io/github/issues/inotin/realFake.svg?style=flat-square
[issues-url]: https://github.com/inotin/realFake/issues
[license-shield]: https://img.shields.io/github/license/inotin/realFake.svg?style=flat-square
[license-url]: https://github.com/inotin/realFake/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/inotin/
[product-screenshot]: images/screenshot.png
