This project is a for of the [gym-http-api](https://github.com/openai/gym-http-api) open-source library (which is now archived), which includes newer version of the libraries and also replaces gym with the updated [gymnasium](https://github.com/Farama-Foundation/Gymnasium).

As of now, only the Go client is being updated but contributions of clients in other languages are welcome.

# Installation

To download the code and install the requirements, you can run the following shell commands:

    git clone https://github.com/rajin98/gymnasium-api
    cd gymnasium-api
    pip install -r requirements.txt

# Getting started

This code is intended to be run locally by a single user. The server runs in python. You can implement your own HTTP clients using any language.

To start the server from the command line, run this:

    python gym_http_server.py

# Testing

The integration tests have not yet been updated. Expect the tests to fail. A unit test suite for the classes in the server is currently being written.

# API specification

- POST `/v1/envs/`

  - Create an instance of the specified environment
  - param: `env_id` -- gym environment ID string, such as 'CartPole-v0'
  - returns: `instance_id` -- a short identifier (such as '3c657dbc')
    for the created environment instance. The instance_id is
    used in future API calls to identify the environment to be
    manipulated

- GET `/v1/envs/`

  - List all environments running on the server
  - returns: `envs` -- dict mapping `instance_id` to `env_id`
    (e.g. `{'3c657dbc': 'CartPole-v1'}`) for every env on the server

- POST `/v1/envs/<instance_id>/reset/`

  - Reset the state of the environment and return an initial
    observation.
  - param: `instance_id` -- a short identifier (such as '3c657dbc')
    for the environment instance
  - returns: `observation` -- the initial observation of the space

- POST `/v1/envs/<instance_id>/step/`

  - Step though an environment using an action.
  - param: `instance_id` -- a short identifier (such as '3c657dbc')
    for the environment instance
  - param: `action` -- an action to take in the environment
  - returns: `observation` -- agent's observation of the current
    environment
  - returns: `reward` -- amount of reward returned after previous action
  - returns: `terminated` -- whether the episode ended due to termination
  - returns: `truncated` -- whether the episode ended due to truncation
  - returns: `info` -- a dict containing auxiliary diagnostic information

- GET `/v1/envs/<instance_id>/action_space/`

  - Get information (name and dimensions/bounds) of the env's
    `action_space`
  - param: `instance_id` -- a short identifier (such as '3c657dbc')
    for the environment instance
  - returns: `info` -- a dict containing 'name' (such as 'Discrete'), and
    additional dimensional info (such as 'n') which varies from
    space to space

- GET `/v1/envs/<instance_id>/observation_space/`

  - Get information (name and dimensions/bounds) of the env's
    `observation_space`
  - param: `instance_id` -- a short identifier (such as '3c657dbc')
    for the environment instance
  - returns: `info` -- a dict containing 'name' (such as 'Discrete'), and
    additional dimensional info (such as 'n') which varies from
    space to space

- POST `/v1/envs/<instance_id>/monitor/start/`

  - Start recording video of the episode
  - param: `instance_id` -- a short identifier (such as '3c657dbc')
    for the environment instance
  - param: `directory` -- directory to store the video file on the locally run server
  - param: `interval` (default=50) -- the nth episode to be recorded

- POST `/v1/envs/<instance_id>/monitor/close/`

  - Flush all monitor data to disk
  - param: `instance_id` -- a short identifier (such as '3c657dbc')
    for the environment instance

- POST `/v1/upload/`

  - Flush all monitor data to disk
  - param: `training_dir` -- A directory containing the results of a
    training run.
  - param: `api_key` -- Your OpenAI API key
  - param: `algorithm_id` (default=None) -- An arbitrary string
    indicating the paricular version of the algorithm
    (including choices of parameters) you are running.

- POST `/v1/shutdown/`
  - Request a server shutdown
  - Currently used by the integration tests to repeatedly create and destroy fresh copies of the server running in a separate thread

> **Note**: All the endpoints have not yet been verified to be working. However, the endpoints used in example_agent.py are working.

# TODO

- Unit test suite for _Envs_ class in `gym_http_client.py`
- Verify the functionality of every API endpoint
- Resolve the `[WinError 10048]` bug when running the `example_agent_client.py`
- Update the Go client and demo
