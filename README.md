# SmartyPants

A CLI tool for interacting with AI services

## Table of Contents

* [core](#core)
* [`smartypants core version`](#smartypants core-version)
* [plugins](#plugins)
* [`smartypants plugins disable`](#smartypants plugins-disable)
* [`smartypants plugins enable`](#smartypants plugins-enable)
* [`smartypants plugins install`](#smartypants plugins-install)
* [`smartypants plugins list`](#smartypants plugins-list)
* [`smartypants plugins uninstall`](#smartypants plugins-uninstall)
* [`smartypants plugins update`](#smartypants plugins-update)
* [Plugins](#plugins)
* [OpenAI](#OpenAI)
* [`smartypants OpenAI chat`](#smartypants OpenAI-chat)
* [`smartypants OpenAI models`](#smartypants OpenAI-models)
* [`smartypants OpenAI prompts`](#smartypants OpenAI-prompts)
* [`smartypants OpenAI send`](#smartypants OpenAI-send)
* [Installation](#installation)

* [Usage](#usage)

* [Examples](#examples)

## Installation

Replace `<version>` with the version you want to install.

You can install this package using pip, npm or homebrew:

### Homebrew:

```bash

brew install SmartyPants

```

### NPM:

```bash

npm install -g SmartyPants

```

### Pip:

```bash

pip install SmartyPants

```

## Usage

### core

#### Command: * [`smartypants core version`](#smartypants core-version)

Displays current version


Usage:

```bash

smartypants core version <arguments> <options>

```

### plugins

#### Command: * [`smartypants plugins disable`](#smartypants plugins-disable)

Disables a plugin


Arguments:

- `plugin`: Name of plugin


Usage:

```bash

smartypants plugins disable <arguments> <options>

```

#### Command: * [`smartypants plugins enable`](#smartypants plugins-enable)

Enables a plugin


Arguments:

- `plugin`: Name of plugin


Usage:

```bash

smartypants plugins enable <arguments> <options>

```

#### Command: * [`smartypants plugins install`](#smartypants plugins-install)

Installs a plugin


Arguments:

- `plugin`: Name of plugin


Usage:

```bash

smartypants plugins install <arguments> <options>

```

#### Command: * [`smartypants plugins list`](#smartypants plugins-list)

Lists all installed plugins


Usage:

```bash

smartypants plugins list <arguments> <options>

```

#### Command: * [`smartypants plugins uninstall`](#smartypants plugins-uninstall)

Uninstalls a plugin


Arguments:

- `plugin`: Name of plugin


Usage:

```bash

smartypants plugins uninstall <arguments> <options>

```

#### Command: * [`smartypants plugins update`](#smartypants plugins-update)

Updates a plugin


Arguments:

- `plugin`: Name of plugin


Usage:

```bash

smartypants plugins update <arguments> <options>

```

## Plugins

### OpenAI

#### Command: * [`smartypants OpenAI chat`](#smartypants OpenAI-chat)

An interactive session with OpenAI


Usage:

```bash

smartypants OpenAI chat <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat create`](#smartypants OpenAI chat-create)

Create a new chat


Arguments:

- `chat_name`: Name of the chat


Usage:

```bash

smartypants OpenAI chat create <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat delete`](#smartypants OpenAI chat-delete)

Delete a chat


Arguments:

- `chat_name`: Name of the chat


Usage:

```bash

smartypants OpenAI chat delete <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat export`](#smartypants OpenAI chat-export)

Export a chat to a prompt


Arguments:

- `chat_name`: Name of the chat


Usage:

```bash

smartypants OpenAI chat export <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat fork`](#smartypants OpenAI chat-fork)

Create a copy of a chat


Arguments:

- `chat_name`: Name of the chat


Usage:

```bash

smartypants OpenAI chat fork <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat list`](#smartypants OpenAI chat-list)

List all chats


Usage:

```bash

smartypants OpenAI chat list <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat open`](#smartypants OpenAI chat-open)

Open a chat


Arguments:

- `chat_name`: Name of the chat


Usage:

```bash

smartypants OpenAI chat open <arguments> <options>

```

#### Command: * [`smartypants OpenAI chat view`](#smartypants OpenAI chat-view)

Show the chat


Arguments:

- `chat_name`: Name of the chat


Usage:

```bash

smartypants OpenAI chat view <arguments> <options>

```

#### Command: * [`smartypants OpenAI models`](#smartypants OpenAI-models)

List available models


Usage:

```bash

smartypants OpenAI models <arguments> <options>

```

#### Command: * [`smartypants OpenAI prompts`](#smartypants OpenAI-prompts)

Preconfigured prompt to use with chats


Usage:

```bash

smartypants OpenAI prompts <arguments> <options>

```

#### Command: * [`smartypants OpenAI prompts create`](#smartypants OpenAI prompts-create)

Create a new prompt


Arguments:

- `prompt_name`: Name of the prompt


Usage:

```bash

smartypants OpenAI prompts create <arguments> <options>

```

#### Command: * [`smartypants OpenAI prompts delete`](#smartypants OpenAI prompts-delete)

Delete a prompt


Arguments:

- `prompt_name`: Name of the prompt


Usage:

```bash

smartypants OpenAI prompts delete <arguments> <options>

```

#### Command: * [`smartypants OpenAI prompts list`](#smartypants OpenAI prompts-list)

List available prompts


Usage:

```bash

smartypants OpenAI prompts list <arguments> <options>

```

#### Command: * [`smartypants OpenAI prompts view`](#smartypants OpenAI prompts-view)

View a prompt


Arguments:

- `prompt_name`: Name of the prompt


Usage:

```bash

smartypants OpenAI prompts view <arguments> <options>

```

#### Command: * [`smartypants OpenAI send`](#smartypants OpenAI-send)

Send one or more messages to OpenAI


Options:

- `attach`: File to include as message

- `live`: Stream the response as it is received

- `message`: Message to send

- `model`: Language model to use

- `raw`: Don't format the response


Usage:

```bash

smartypants OpenAI send <arguments> <options>

```

## Examples
