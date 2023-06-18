# SmartyPants CLI Tool

Welcome to SmartyPants, a user-friendly CLI tool for interacting with AI services, featuring a powerful command and plugin system!

## Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Plugins](#plugins)
    
    - [OpenAI](#OpenAI)
    
    - [Plugins](#Plugins)
    
4. [Contributor Guidelines](#contributor-guidelines)
5. [Licenses and Legal](#licenses-and-legal)

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


## Plugins


### OpenAI

Adds support for OpenAI interaction

_Usage:_ `smartypants openai <command> [arguments] [options]`


**chat** An interactive session with OpenAI

_Usage:_ `smartypants openai chat `








**models** List available models

_Usage:_ `smartypants openai models `







#### Examples


_List available models in OpenAI_
```bash
smartypants openai models
```




**prompts** Preconfigured prompt to use with chats

_Usage:_ `smartypants openai prompts `








**send** Send one or more messages to OpenAI

_Usage:_ `smartypants openai send  [options]`





#### Options


`attach` : File to include as message

`live` : Stream the response as it is received

`message` : Message to send

`model` (Default: gpt-3.5-turbo): Language model to use

`raw` : Don't format the response





#### Examples


_Send one or more messages to OpenAI_
```bash
smartypants openai send --message 'Hello OpenAI' --model 'gpt-3.5-turbo'
```





### Plugins

Adds support for managing plugins

_Usage:_ `smartypants plugins <command> [arguments] [options]`


**disable** Disables a plugin

_Usage:_ `smartypants plugins disable  <arguments>`



#### Arguments


`plugin` (Required): Name of plugin







#### Examples


_Disable a plugin_
```bash
smartypants plugins disable openai
```




**enable** Enables a plugin

_Usage:_ `smartypants plugins enable  <arguments>`



#### Arguments


`plugin` (Required): Name of plugin







#### Examples


_Enable a plugin_
```bash
smartypants plugins enable openai
```




**install** Installs a plugin

_Usage:_ `smartypants plugins install  <arguments>`



#### Arguments


`plugin` (Required): Name of plugin







#### Examples


_Install a plugin_
```bash
smartypants plugins install openai
```




**list** Lists all installed plugins

_Usage:_ `smartypants plugins list `







#### Examples


_List all installed plugins_
```bash
smartypants plugins list
```




**uninstall** Uninstalls a plugin

_Usage:_ `smartypants plugins uninstall  <arguments>`



#### Arguments


`plugin` (Required): Name of plugin







#### Examples


_Uninstall a plugin_
```bash
smartypants plugins uninstall openai
```




**update** Updates a plugin

_Usage:_ `smartypants plugins update  <arguments>`



#### Arguments


`plugin` : Name of plugin







#### Examples


_Update a plugin_
```bash
smartypants plugins update openai
```




**status** Shows state of a specific plugin

_Usage:_ `smartypants plugins status  <arguments>`



#### Arguments


`plugin` : Name of plugin







#### Examples


_Show status of a plugin_
```bash
smartypants plugins status openai
```






## Contributor Guidelines



## Licenses and Legal

