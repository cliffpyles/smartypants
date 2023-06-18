# SmartyPants CLI Tool

Welcome to SmartyPants, a user-friendly CLI tool for interacting with AI services, featuring a powerful command and plugin system!

## Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Plugins](#plugins)
    
    - [Plugins](#Plugins)
    
    - [OpenAI](#OpenAI)
    
4. [Contributor Guidelines](#contributor-guidelines)
5. [Licenses and Legal](#licenses-and-legal)

## Setup

### Requirements

_no requirements specified_

### Installation

**Homebrew**

`brew install smartypants-cli`

**NPM**

`npm install -g smartypants-cli`

**PIP**

`pip install smartpants-cli`


## Usage

`smartypants <plugin_name> <plugin_command> [arguments] [options]`


## Plugins


### Plugins


`disable` Disables a plugin

Usage: `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



**Disable a plugin**
```bash
smartypants plugins disable openai
```




`enable` Enables a plugin

Usage: `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



**Enable a plugin**
```bash
smartypants plugins enable openai
```




`install` Installs a plugin

Usage: `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



**Install a plugin**
```bash
smartypants plugins install openai
```




`list` Lists all installed plugins

Usage: `smartypants plugins`

#### Arguments



#### Options



#### Examples



**List all installed plugins**
```bash
smartypants plugins list
```




`uninstall` Uninstalls a plugin

Usage: `smartypants plugins <arguments>`

#### Arguments



`plugin` (Required): Name of plugin



#### Options



#### Examples



**Uninstall a plugin**
```bash
smartypants plugins uninstall openai
```




`update` Updates a plugin

Usage: `smartypants plugins <arguments>`

#### Arguments



`plugin` : Name of plugin



#### Options



#### Examples



**Update a plugin**
```bash
smartypants plugins update openai
```




`status` Shows state of a specific plugin

Usage: `smartypants plugins <arguments>`

#### Arguments



`plugin` : Name of plugin



#### Options



#### Examples



**Show status of a plugin**
```bash
smartypants plugins status openai
```





### OpenAI


`chat` An interactive session with OpenAI

Usage: `smartypants openai`

#### Arguments



#### Options



#### Examples




`models` List available models

Usage: `smartypants openai`

#### Arguments



#### Options



#### Examples



**List available models in OpenAI**
```bash
smartypants openai models
```




`prompts` Preconfigured prompt to use with chats

Usage: `smartypants openai`

#### Arguments



#### Options



#### Examples




`send` Send one or more messages to OpenAI

Usage: `smartypants openai [options]`

#### Arguments



#### Options



`attach` : File to include as message

`live` : Stream the response as it is received

`message` : Message to send

`model` (Default: gpt-3.5-turbo): Language model to use

`raw` : Don't format the response



#### Examples



**Send one or more messages to OpenAI**
```bash
smartypants openai send --message 'Hello OpenAI' --model 'gpt-3.5-turbo'
```






## Contributor Guidelines



## Licenses and Legal

