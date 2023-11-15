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

<h3 align="center">Challenge Task HS23: E-commerce</h3>


  <p align="center">
    Group 1: Ülkü Karagöz, Maximilian Huwyler, Vincent Stadler
    <br />
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
This website is a simple E-commerce app where you can view and order clothes. The goal of the project is to make the app more secure against malicious attacks. 

<!-- GETTING STARTED -->
## Getting Started

The application is meant to be run in Docker containers using a Docker compose setup. 

### Prerequisites


* Install Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ukarag/E-commerce.git
   ```
2. Start the Docker daemon: [https://docs.docker.com/config/daemon/start/](https://docs.docker.com/config/daemon/start/)
   
3. On first start build and start the containers
   ```sh
   docker compose up --build
   ```
   When built images are present simply run the containers
   ```sh
   docker compose up
   ```
4. Access the application frontend on local port 8080. A default account is configured:
   ```
   username: testuser
   password: testpassword
   ```

5. A default admin account is configured (no extra functionality in frontend implemented):
   ```
   username: admin
   password: your_superuser_password
   ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* eCommerce Application: [https://github.com/SteinOveHelset](https://github.com/SteinOveHelset)
* README Template: [https://github.com/othneildrew](https://github.com/othneildrew)
