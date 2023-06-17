# SmartyPants CLI Tool

Welcome to SmartyPants, a user-friendly CLI tool for interacting with AI services, featuring a powerful command and plugin system!

## Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Plugins](#plugins)
4. [Contributor Guidelines](#contributor-guidelines)
5. [Licenses and Legal](#licenses-and-legal)

## Setup

### Requirements

_no requirements specified_

### Installation

**Homebrew**

`brew install smartypants-cli`

or

**NPM**

`npm install -g smartypants-cli`

or

**PIP**

`pip install smartpants-cli`


## Usage

`smartypants <plugin_name> <plugin_command> [arguments] [options]`


## Plugins


### Plugins


Command: `disable` Disables a plugin

#### Parameters



`plugin` (Required): Name of plugin



#### Examples



**Disable a plugin**
```bash
smartypants plugins disable my_plugin
```




Command: `enable` Enables a plugin

#### Parameters



`plugin` (Required): Name of plugin



#### Examples



**Enable a plugin**
```bash
smartypants plugins enable my_plugin
```




Command: `install` Installs a plugin

#### Parameters



`plugin` (Required): Name of plugin



#### Examples



**Install a plugin**
```bash
smartypants plugins install my_plugin
```




Command: `list` Lists all installed plugins

#### Parameters



#### Examples



**List all installed plugins**
```bash
smartypants plugins list
```




Command: `uninstall` Uninstalls a plugin

#### Parameters



`plugin` (Required): Name of plugin



#### Examples



**Uninstall a plugin**
```bash
smartypants plugins uninstall my_plugin
```




Command: `update` Updates a plugin

#### Parameters



`plugin` : Name of plugin



#### Examples



**Update a plugin**
```bash
smartypants plugins update my_plugin
```





### Openai


Command: `chat` An interactive session with OpenAI

#### Parameters



#### Examples




Command: `models` List available models

#### Parameters



#### Examples



**List available models in OpenAI**
```bash
smartypants openai models
```




Command: `prompts` Preconfigured prompt to use with chats

#### Parameters



#### Examples




Command: `send` Send one or more messages to OpenAI

#### Parameters



#### Examples



**Send one or more messages to OpenAI**
```bash
smartypants openai send --message 'Hello OpenAI' --model 'gpt-3.5-turbo'
```






## Contributor Guidelines



## Licenses and Legal

