# SmartyPants CLI Tool

Welcome to SmartyPants, a user-friendly CLI tool for interacting with AI services, featuring a powerful command and plugin system!

## Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Commands](#commands)
3. [References](#references)

## Setup

### Requirements

_no requirements specified_

### Installation

Homebrew

`brew install smartypants-cli`

NPM

`npm install -g smartypants-cli`

PIP

`pip install smartpants-cli`


## Usage

`smartypants <plugin_name> <plugin_command> [arguments] [options]`


## Commands


### OpenAI

Adds support for OpenAI interaction

_Usage:_ `smartypants openai <command> [arguments] [options]`

#### Commands


**chat** An interactive session with OpenAI

_Usage:_ `smartypants openai chat`

##### Arguments


None



##### Options


None




---


**models** List available models

_Usage:_ `smartypants openai models`

##### Arguments


None



##### Options


None




##### Examples


_List available models in OpenAI_
```bash
smartypants openai models
```



---


**prompts** Preconfigured prompt to use with chats

_Usage:_ `smartypants openai prompts`

##### Arguments


None



##### Options


None




---


**send** Send one or more messages to OpenAI

_Usage:_ `smartypants openai send [options]`

##### Arguments


None



##### Options



`attach` (String)   : File to include as message

_Format:_ filepath



`live` (Boolean)   : Stream the response as it is received



`message` (String)   : Message to send



`model` (String) (Default: gpt-3.5-turbo)  : Language model to use


_Allowed Values:_ `gpt-3.5-turbo, gpt-4, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k, gpt-4-0613`


`raw` (Boolean)   : Don't format the response







##### Examples


_Send one or more messages to OpenAI_
```bash
smartypants openai send --message 'Hello OpenAI' --model 'gpt-3.5-turbo'
```







### Plugins

Adds support for managing plugins

_Usage:_ `smartypants plugins <command> [arguments] [options]`

#### Commands


**disable** Disables a plugin

_Usage:_ `smartypants plugins disable <arguments>`

##### Arguments



`plugin` (Required) : Name of plugin






##### Options


None




##### Examples


_Disable a plugin_
```bash
smartypants plugins disable openai
```



---


**enable** Enables a plugin

_Usage:_ `smartypants plugins enable <arguments>`

##### Arguments



`plugin` (Required) : Name of plugin






##### Options


None




##### Examples


_Enable a plugin_
```bash
smartypants plugins enable openai
```



---


**install** Installs a plugin

_Usage:_ `smartypants plugins install <arguments>`

##### Arguments



`plugin` (Required) : Name of plugin






##### Options


None




##### Examples


_Install a plugin_
```bash
smartypants plugins install openai
```



---


**list** Lists all installed plugins

_Usage:_ `smartypants plugins list`

##### Arguments


None



##### Options


None




##### Examples


_List all installed plugins_
```bash
smartypants plugins list
```



---


**uninstall** Uninstalls a plugin

_Usage:_ `smartypants plugins uninstall <arguments>`

##### Arguments



`plugin` (Required) : Name of plugin






##### Options


None




##### Examples


_Uninstall a plugin_
```bash
smartypants plugins uninstall openai
```



---


**update** Updates a plugin

_Usage:_ `smartypants plugins update <arguments>`

##### Arguments



`plugin`  : Name of plugin






##### Options


None




##### Examples


_Update a plugin_
```bash
smartypants plugins update openai
```



---


**status** Shows state of a specific plugin

_Usage:_ `smartypants plugins status <arguments>`

##### Arguments



`plugin` (Required) : Name of plugin






##### Options


None




##### Examples


_Show status of a plugin_
```bash
smartypants plugins status openai
```








## Contributor Guidelines



## Licenses and Legal



## References

### Formats

| Format  | Definition |
| ------------- | ------------- |
| `filetype`  | A valid Mac, Linux, or Windows filepath  |