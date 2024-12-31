# Python Sandbox

Welcome to the Python Sandbox repository!

This repository is a collection of small Python projects that I have created for fun and to explore new topics. Each project is a standalone piece of code that demonstrates a specific concept, technique, or idea in Python programming.

Feel free to browse through the projects :)

## Projects

- Project 1 (v0.1): PoolBounce
- Project 2 (v0.1): CalendarExport

## Projects description
### Project 1 - Pool Bounce Simulation
Ok, this one is a bit silly. We were playing pool when we wondered: would an infinite force allow us to make the ball reach a hole, no matter where or in which direction we hit it? I'm sure some math could help me figure it out, but spending too much time on such a simple Python project just sounded way more fun...

### Project 2 - Calendar Exporter
For my last semester of bachelor, the agenda given is global to all groups, and we have to manually enter our group for each course on a specific website, to access to our custom agenda. Because I prefer to use my own agenda app, I made this script to convert the global agenda given (in a JSON format provided by an HTTP request) to a custom ICS containing only appropriate class slots (depending on the option followed and the group). This script is used in an API to automatically create any custom agenda with the request parameters containing group choices.

## Getting Started

To run any of the projects, simply clone the repository and navigate to the project directory:

```bash
git clone https://github.com/valcrog/PythonSandbox.git
cd PythonSandbox/project-directory
```

Then, install the requirements using:

```bash
pip install -r requirements.txt
```

You're now all set to run the main project file `main.py` !