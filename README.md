# Fullstack Boilerplate with Docker

A full-stack application with separate frontend, backend, and database components, all managed with Docker.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Folder Structure](#folder-structure)
- [License](#license)

## Overview

This repository contains the code for a full-stack application:

- **Frontend**: Built using modern web technologies and frameworks.
- **Backend**: Built using Python.
- **Database**: Configured in the `db` folder.
- **Docker**: Used to containerize and manage the application.

## Getting Started

Follow the instructions below to clone the repository, build the Docker image, and start the application.

### Prerequisites

Ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PratapBodimalla/Docker-boilerplate-fullstack.git
   cd .\Docker-boilerplate-fullstack\
   ```

2. Build the Docker images:

   ```bash
   docker-compose build
   ```

### Running the Application

Start the application using Docker Compose:

```bash
docker-compose up
```

This will:

- Build and run the frontend service.
- Build and run the backend service.
- Set up the database container.

Access the application via your browser at `http://localhost:<frontend-port>`.

## Folder Structure

```plaintext
/
├── frontend/      # Contains the frontend code and DockerFile
│   └── DockerFile
├── backend/       # Contains the backend code and DockerFile
│   └── DockerFile
├── db/            # Contains database configurations and migrations
│    └── DockerFile
└──  docker-compose.yml
```

## License

This project is licensed under the [MIT License](LICENSE).
